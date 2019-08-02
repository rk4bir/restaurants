from django.db import models
from django.db.models.signals import pre_save, post_save
from general.functions import unique_order_id_generator, unique_slug_generator, unique_key_generator
from django.shortcuts import reverse



class FoodCategory(models.Model):
	title	  = models.CharField(max_length=200, blank=False, null=False)
	is_active = models.BooleanField(default=True, blank=True)

	def __str__(self):
		return self.title + " - " + "status: " + str(self.is_active)
	class Meta:
		ordering = ['title']


class Food(models.Model):
	category		     = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
	title			     = models.CharField(max_length=512, blank=False, null=False)
	slug                 = models.SlugField(blank=True, unique=True)
	photo    		     = models.ImageField(
							'item_photo',
							upload_to="item_photos/",
							null=True, blank=True,
							width_field="width_field",
							height_field="height_field",
						  )
	key      			  = models.CharField(default='', blank=True, max_length=128)
	width_field  	      = models.IntegerField(default=0)
	height_field 	      = models.IntegerField(default=0)
	price 			      = models.FloatField(default=0.00, blank=True)
	ratio   		      = models.CharField(max_length=50, default='1:1', blank=False, null=False)
	is_active             = models.BooleanField(default=True, blank=True)
	ordered_in_restaurant = models.IntegerField(default=0, blank=True)
	ordered_in_home    	  = models.IntegerField(default=0, blank=True)
	created_at   	      = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at		      = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.category.title + " -> " + self.title + " - " + str(self.price)



	def get_profile_url(self):
		return reverse('foods:profile', kwargs={'slug':self.slug})
	class Meta:
		ordering = ['title']


















def food_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.key:
		instance.key = unique_key_generator(instance)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)



pre_save.connect(food_pre_save_receiver, sender=Food)
