from django.shortcuts import render
from restaurants.models import Restaurant
from django.views.generic import ListView

# Here will be added restaurant from PartnerRestaurant Model
# instead of Restaurant
def index_view(request):
	if request.is_ajax() and request.method == "POST":
		requested_data = int(request.POST['dataNo'])
		partner_restaurants = Restaurant.objects.all().filter(is_active=True).filter(is_orderable=True)[requested_data:(requested_data+5)]
		return render(request, 'more_restraurant.html', {'partner_restaurants':partner_restaurants})

	partner_restaurants = Restaurant.objects.all().filter(is_active=True).filter(is_orderable=True)[:5] or None
	template_name 		= 'base.html'
	contex = {
		'partner_restaurants':partner_restaurants
	}
	return render(request, template_name, contex)

def error_404_view(request):
	template_name = '404.html'
	message       = ''
	contex		  = {
		'message': message
	}
	return render(request, template_name, contex)