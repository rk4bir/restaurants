from django.db import models
from django.contrib.auth.models import User
from foods.models import Food
from restaurants.models import Restaurant
from django.shortcuts import reverse
from django.db.models.signals import post_save
from general.functions import getRandomCode

class AccountManager(models.Manager):
	pass

class Account(models.Model):
	user  			= models.ForeignKey(User, on_delete=models.CASCADE)
	name 	    	= models.CharField(max_length=1000, blank=False, default='')
	phone 			= models.CharField(max_length=20, blank=False, null=False)
	city  			= models.CharField(max_length=128, default='',blank=True)
	address		    = models.CharField(max_length=256, default='', blank=True)
	pp    			= models.ImageField(
						'profile_photo',
						upload_to="profile_photos/",
						null=True, blank=True,
						width_field="width_field",
						height_field="height_field",
					)
	width_field  	= models.IntegerField(default=0)
	height_field 	= models.IntegerField(default=0)
	fav_foods    	= models.ManyToManyField(Food, blank=True)
	fav_restaurants = models.ManyToManyField(Restaurant, blank=True)
	notice_offer 	= models.TextField(blank=True, default='')
	about_me	 	= models.TextField(blank=True, default=' ')
	is_active       = models.BooleanField(default=False, blank=True)
	activation_code = models.CharField(max_length=32, blank=True, null=True)
	pass_change_code= models.CharField(max_length=32, blank=True, null=True)
	created_at      = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at	    = models.DateTimeField(auto_now=True, auto_now_add=False)
	
	objects         = AccountManager()
	def get_profile_url(self):
		return reverse('accounts:profile', kwargs={'username': self.user.username})
	
	def get_traced_position(self):
		return self.longitude + ', ' + self.lattitude


	def __str__(self):
		return self.user.username + " - " + self.city + " - " + str(self.phone)




def create_accountObj(sender, instance, *args, **kwargs):
	if instance == User.objects.get(username='root', is_staff=True, is_superuser=True):
		return
	qs = Account.objects.filter(user=instance)
	if not qs.exists():
		account       = Account()
		account.user  = instance
		account.name  = instance.first_name
		account.phone = instance.last_name
		account.activation_code = getRandomCode()
		account.pass_change_code= getRandomCode(size=6)
		account.save()

post_save.connect(create_accountObj, sender=User)