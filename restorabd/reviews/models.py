from django.db import models
from restaurants.models import Restaurant
from django.db.models.signals import pre_save
from accounts.models import Account

class Review(models.Model):
	restaurant  = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	account     = models.ForeignKey(Account, on_delete=models.CASCADE)
	title       = models.CharField(max_length=160, default='', blank=False)
	content 	= models.TextField()
	food        = models.IntegerField(default=0, blank=False)
	price       = models.IntegerField(default=0, blank=False)
	service     = models.IntegerField(default=0, blank=False)
	environment = models.IntegerField(default=0, blank=False)
	# (food + price + service + envoronment) / 4.0
	average     = models.FloatField(default=0.0, blank=False)

	star1	    = models.CharField(max_length=50, default='fa-star')
	star2	    = models.CharField(max_length=50, default='fa-star')
	star3	    = models.CharField(max_length=50, default='fa-star')
	star4	    = models.CharField(max_length=50, default='fa-star')
	star5	    = models.CharField(max_length=50, default='fa-star')

	created_at  = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.restaurant.title + ": " + self.account.user.username + " - " + self.title

	class Meta:
		ordering = ['-created_at']
	
	