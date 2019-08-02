from django.db import models
from django.contrib.auth.models import AbstractUser
from foods.models import Food
from restaurants.models import Restaurant
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from general.functions import getRandomCode



class Account(AbstractUser):
	
	name = models.CharField(max_length=100, default='')
	phone = models.CharField(max_length=20, blank=False, null=False)
	city = models.CharField(max_length=128, default='',blank=True)
	address	= models.CharField(max_length=256, default='', blank=True)
	
	pp = models.ImageField(
		'profile_photo',
		upload_to="profile_photos/",
		null=True, blank=True,
		width_field="width_field",
		height_field="height_field",
	)
	
	width_field = models.IntegerField(default=0)
	height_field = models.IntegerField(default=0)
	fav_foods = models.ManyToManyField(Food, blank=True)
	fav_restaurants = models.ManyToManyField(Restaurant, blank=True)
	notice_offer = models.TextField(blank=True, default='')
	about_me = models.TextField(blank=True, default=' ')
	activation_code = models.CharField(max_length=32, blank=True, null=True)
	pass_change_code = models.CharField(max_length=32, blank=True, null=True)


	def get_profile_url(self):
		return reverse('accounts:profile', kwargs={'pk': self.pk})

	def __str__(self):
		return self.username + " - " + self.city + " - " + self.phone

	class Meta:
		verbose_name = 'account'



def pre_save_receiver(sender, instance, *args, **kwargs):
	pass

pre_save.connect(pre_save_receiver, sender=Account)