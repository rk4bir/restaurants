from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponse
from restaurants.models import Restaurant
from .models import Cart, Order, Discount
from foods.models import Food
from accounts.models import Account
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

@login_required
def myOrders_view(request):
	orders = Order.objects.all().filter(account=Account.objects.get(user=request.user)).filter(is_active=True)
	template_name = 'orders/myorders_list.html'
	contex = {
		'orders': orders
	}
	return render(request, template_name, contex)


@login_required
def orderManage_view(request):
	template_name = 'orders/management_index.html'
	if not request.user.is_staff or not request.user.is_superuser:
		return HttpResponseRedirect('/404notfound/')
	
	orders = Order.objects.all()
	contex = {
		'orders': orders
	}
	return render(request, template_name, contex)	


def OrderDetail_view(request, order_id):
	template_name = 'orders/detail.html'
	try:
		order = Order.objects.get(order_id=order_id)
		cart  = order.cart
		products = Food.objects.all().filter(cart=cart)
		quantities = cart.quantities.split(',')
		proQuantities = zip(products, quantities)
		quantities.remove('')
		if order.is_active == False:
			return HttpResponseRedirect('/404notfound/')
	except:
		return HttpResponseRedirect('/404notfound/')
	contex = {
		'restaurant': cart.restaurant,
		'proQuantities': proQuantities,
		'order': order,
	}
	return render(request, template_name, contex)


def addToCart_view(request):
	template_name = 'orders/confirm-order.html'
	if request.is_ajax():
		restaurant = Restaurant.objects.get(pk=request.POST['restaurant'])
		subtotal   = request.POST['totalCost']
		quantity   = request.POST['totalquantity']
		slugs      = request.POST['slugs'].split(',')
		slugs.remove('')
		grandtotal = float(subtotal) + restaurant.service_charge + restaurant.vat_tax 
		quantities = request.POST['quantities']
		products = []
		for slug in slugs:
			try:
				foodObj = Food.objects.get(slug=slug)
				products.append(foodObj)
			except:
				pass
		
		cart       		= Cart()
		cart.restaurant = restaurant
		cart.save()
		cart.products 	= [obj for obj in products]
		cart.subtotal 	= subtotal
		cart.total 		= grandtotal
		cart.quantities = quantities
		cart.save()
		
	contex = {
		'subtotal': subtotal,
		'quantity': quantity,
		'restaurant': restaurant,
		'grandtotal': grandtotal,
		'cart': cart
	}
	return render(request, template_name, contex)




def newOrder_view(request):
	template_name = 'orders/confirmed-page.html'
	if request.method == "POST":
		cartKey  = request.POST['cart']
		phone    = request.POST['cell']
		order_type= request.POST['orderType']
		account = None
		if request.user.is_authenticated:
			account = Account.objects.get(user=request.user)
		else:
			qs = Account.objects.filter(phone=phone).exists()
			if qs:
				account = Account.objects.get(phone=phone)
		order = Order()
		order.account = account
		try:
			cart = Cart.objects.get(key=cartKey)
			cart.is_active = True
			cart.save()
			order.cart = cart
		except:
			messages.warning(request, "Order request failed! Please try again.")
			return HttpResponseRedirect('/restaurants/'+cart.restaurant.slug+'/')
		_discount = 0.00
		try:
			dObj = Discount.objects.get(key=request.POST['promoCode'])
			if dObj.used == False:
				_discount = int( float(cart.subtotal * dObj.percentage) / 100.00 )
				dObj.used = True
				dObj.save()
		except:
			pass
		order.name 			   = request.POST['name']
		order.phone 		   = phone
		order.shipping_address = request.POST['location']
		order.order_type 	   = order_type
		order.payment_method   = request.POST['paymentMethod']
		order.expected_time    = request.POST['time']

		if order_type == 'home':
			order.cost = cart.total - _discount + 30.00 # Shipping cost
		else:
			order.cost = cart.total - _discount
		order.discount = _discount
		order.save()
		# SEND NOTIFICATION
		if account != None:
			notification 		 = Notification()
			notification.account = account
			notification.content = "You order <span class='font-weight-bold'>#" + str(order.order_no) + "</span> has been added. We will confirm it in minutes."
			notification.link    = '/orders/' + order.order_id + '/'
			notification.save()
		return HttpResponseRedirect('/orders/'+order.order_id+'/')
	messages.warning(request, "Something went wrong. Please try again.")
	return HttpResponseRedirect('/restaurants/'+cart.restaurant.slug+'/')



def checkDiscountCode_view(request):
	if request.is_ajax():
		qs = Discount.objects.filter(key=request.POST['promoCode'])
		if qs.exists():
			obj = Discount.objects.get(key=request.POST['promoCode'])
			if obj.used == True:
				msg = '<span class="text-warning">Sorry! This code was used before.</span>'
			else:
				msg = '<span class="text-success">Congrats! You will enjoy ' + str(obj.percentage) + "% discount.</span>"
		else:
			msg = '<span class="text-warning">Sorry! No offer for this code.</span>'
		return HttpResponse(msg)
	return HttpResponse("Bad request!")











# UPDATE VISIBILITY STATUS
@login_required
def updateVisibility_view(request, order_id):
	try:
		order = Order.objects.get(order_id=order_id)
	except:
		return HttpResponseRedirect('/404notfound/')
	if not request.user.is_staff or not request.user.is_superuser:
		if request.user != order.account.user or request.method != "POST":
			return HttpResponseRedirect('/404notfound/')
	try:
		if order.is_active == True:
			order.is_active = False
		elif order.is_active == False:
			order.is_active = True
		order.save()
	except:
		messages.success(request, "Couldn't execute the request.")
		pass
	
	if request.user.is_staff or request.user.is_superuser:
		return HttpResponseRedirect('/orders/management/')
	messages.success(request, "Order has been removed from your list.")
	return HttpResponseRedirect('/orders/mylist/')




# UPDATE PAYMENT STATUS
@login_required
def updatePaymentStatus_view(request, order_id):
	if not request.user.is_staff or not request.user.is_superuser or request.method != "POST":
		return HttpResponseRedirect('/404notfound/')
	try:
		order = Order.objects.get(order_id=order_id)
		if order.payment_status == True:
			order.payment_status = False
			notf  = "Payment for your order #" + str(order.order_no) + " is pending."
		elif order.payment_status == False:
			order.payment_status = True
			notf = "Payment for your order #" + str(order.order_no) + " is accepted."
		order.save()
	except:
		messages.success(request, "Couldn't change payment status.")
		pass

	# SEND NOTIFICATION
	if order.account != None:
		notification 		 = Notification()
		notification.account = order.account
		notification.content = notf
		notification.link    = '/orders/' + order.order_id + '/'
		notification.save()
	return HttpResponseRedirect('/orders/management/')


# UPDATE STATUS
@login_required
def updateStatus_view(request, order_id):
	if not request.user.is_staff or not request.user.is_superuser or request.method != "POST":
		return HttpResponseRedirect('/404notfound/')
	try:
		order = Order.objects.get(order_id=order_id)
		if order.status == True:
			order.status = False
			notf = "Order #" + str(order.order_no) + " is pending."
		elif order.status == False:
			order.status = True
			notf = "Order #" + str(order.order_no) + " is accepted."
		order.save()
	except:
		messages.success(request, "Couldn't change status.")
		pass

	# SEND NOTIFICATION
	if order.account != None:
		notification 		 = Notification()
		notification.account = order.account
		notification.content = notf
		notification.link    = '/orders/' + order.order_id + '/'
		notification.save()
	
	return HttpResponseRedirect('/orders/management/')


# DELETE ORDER
@login_required
def DeleteOrder_view(request, order_id):
	if not request.user.is_staff or not request.user.is_superuser or request.method != "POST":
		return HttpResponseRedirect('/404notfound/')
	try:
		order = Order.objects.get(order_id=order_id)
		# SEND NOTIFICATION
		if order.account != None:
			notification 		 = Notification()
			notification.account = order.account
			notification.content = "Order #" + str(order.order_no) + " has been deleted."
			notification.link    = '/orders/' + order.order_id + '/'
			notification.save()
		order.delete()
	except:
		messages.success(request, "Couldn't change status.")
		pass

	return HttpResponseRedirect('/orders/management/')