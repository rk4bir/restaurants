from django.db import models
from restaurants.models import Restaurant
from foods.models import Food

class PartnerRestaurant(models.Model):
	restaurant 	 	= models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	home_sell_count = models.IntegerField(default=0, blank=True)
	rest_sell_count = models.IntegerField(default=0, blank=True)
	total_sell_tk	= models.FloatField(default=0.0, blank=True)

class Sell(models.Model):
	restaurant    = models.ForeignKey(PartnerRestaurant, on_delete=models.CASCADE)
	foods		  = models.ManyToManyField(Food)
	total_price   = models.FloatField(default=0.0, blank=False, null=False)
	delivery_type = models.CharField(max_length=100, blank=False, null=False)
	destination   = models.CharField(max_length=256, default='', blank=True)
	created_at	  = models.DateTimeField(auto_now=False, auto_now_add=True) 
	