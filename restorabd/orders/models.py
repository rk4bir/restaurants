from django.db import models
from accounts.models import Account
from foods.models import Food
from restaurants.models import Restaurant
from django.db.models.signals import pre_save
from general.functions import unique_key_generator, unique_order_id_generator, unique_order_no_generator
from random import randint
from django.shortcuts import reverse


PAYMENT_METHODS = (
    ('pod', 'Pay On Delivery'),
    ('bkash', 'bKash'),
    ('dbbl', 'DBBL'),
)

DELIVERY_TYPES = (
	('home', 'Home'),
	('hestaurant', 'Restaurant')
)

class Cart(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True)
	key        = models.CharField(max_length=128, blank=True, default='')
	products   = models.ManyToManyField(Food, blank=True)
	quantities = models.CharField(max_length=512, default='', blank=True)
	subtotal   = models.FloatField(default=0.00, blank=True)
	total      = models.FloatField(default=0.00, blank=True)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	is_active  = models.BooleanField(default=False, blank=True)
	def __str__(self):
		return self.restaurant.title + ' - ' + str(self.total)

class Order(models.Model):
	account       = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
	cart          = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
	order_id      = models.CharField(blank=True, max_length=256, default='')
	order_no      = models.CharField(blank=True, max_length=256, default='')
	name          = models.CharField(max_length=100, default='', blank=False)
	phone	   	  = models.CharField(max_length=20, default='', blank=False)
	shipping_address = models.CharField(max_length=200, default='', blank=False)
	status		 = models.BooleanField(default=False, blank=True)
	payment_status = models.BooleanField(default=False, blank=True)
	shipping_charge  = models.FloatField(default=30.00, blank=True)
	order_type    = models.CharField(max_length=100, default='home', blank=False, choices=DELIVERY_TYPES)
	payment_method= models.CharField(max_length=100, default="pod", choices=PAYMENT_METHODS)
	expected_time = models.TimeField(blank=True, null=True, default='')
	discount      = models.FloatField(default=0.00, blank=True)
	cost		  = models.FloatField(default=0.00, blank=True)
	is_active     = models.BooleanField(default=True, blank=True)
	created_at    = models.DateTimeField(auto_now=False, auto_now_add=True)

	def get_absolute_url(self):
		return reverse('orders:detail', kwargs={'order_id': self.order_id})
		
	def __str__(self):
		return self.name + " - " +  self.phone + " - " + self.shipping_address + " - " + str(self.cost)

	class Meta:
		ordering = ['-created_at']

class Discount(models.Model):
	percentage = models.FloatField(default=0.00, blank=True)
	key        = models.CharField(max_length=100, blank=True, default='')
	used       = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return str(self.percentage) + " - " + str(self.used)
















# PRE SAVE MODEL STUFFs
def add_key_to_CartObj(sender, instance, *args, **kwargs):
	if not instance.key:
		instance.key = unique_key_generator(instance, size=12)

pre_save.connect(add_key_to_CartObj, sender=Cart)



def add_key_to_DiscountObj(sender, instance, *args, **kwargs):
	if not instance.key:
		instance.key = unique_key_generator(instance, size=randint(6, 10))

pre_save.connect(add_key_to_DiscountObj, sender=Discount)




def add_order_id_to_OrderObj(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_id_generator(instance)
	if not instance.order_no:
		instance.order_no = unique_order_no_generator(instance)

pre_save.connect(add_order_id_to_OrderObj, sender=Order)