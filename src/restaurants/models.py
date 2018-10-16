from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save, post_save
from general.functions import *
from foods.models import Food
from informations.models import City


class RestaurantManager(models.Manager):
    def all(self):
        return self.filter(is_active=True)




class Restaurant(models.Model):
    # Basic
    title 	    	   = models.CharField(max_length=500, blank=False, null=False)
    slug               = models.SlugField(blank=True, unique=True)
    phone	   		   = models.CharField(max_length=128, blank=False, null=False)
    email      		   = models.CharField(max_length=252, blank=True, null=True, default='')
    # minimum
    min_serve_time     = models.IntegerField(default=30, blank=False, verbose_name='Minimum Serve Time')
    min_order_tk 	   = models.FloatField(default=150.00, blank=False, verbose_name='Minimum Order')
    service_charge     = models.FloatField(default=30.00, blank=False, verbose_name='Service Charge')
    vat_tax            = models.FloatField(default=0.0, blank=True, verbose_name='Vat/Tax')
    # location/contact
    city               = models.ForeignKey(City, on_delete=models.CASCADE)
    address			   = models.CharField(max_length=1024, blank=False, null=False)
    environment		   = models.CharField(max_length=512, blank=False, null=False)
    map_embed_url      = models.TextField(blank=False, default='https://maps.google.com/')
    
    # Photos
    logo 	 		   = models.ImageField(
                            'logo',
                            upload_to="restaurant_logo/",
                            null=True, blank=True,
                            width_field="logo_width_field",
                            height_field="logo_height_field",
                        )
    logo_height_field  = models.IntegerField(default=0)
    logo_width_field   = models.IntegerField(default=0)
    pp    	 		   = models.ImageField(
							'profile photo',
							upload_to="restaurant_pp/",
							null=True, blank=True,
							width_field="pp_width_field",
							height_field="pp_height_field",
						)
    pp_height_field    = models.IntegerField(default=0)
    pp_width_field     = models.IntegerField(default=0)

    

    # Others
    is_active          = models.BooleanField(default=False)
    is_orderable       = models.BooleanField(default=False)
    created_at 		   = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at		   = models.DateTimeField(auto_now=True)
    extra_info         = models.TextField(blank=True, null=True)
    food_items         = models.ManyToManyField(Food, blank=True)
    # Restaurant qs manager
    objects = RestaurantManager()

    def __str__(self):
        return self.title + " - " + self.slug

    def get_absolute_url(self):
        return reverse("restaurants:detail", kwargs={"slug": self.slug})

    def get_review_page_url(self):
        return reverse("restaurants:review", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']










class RestaurantReview(models.Model):
    restaurant         = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food               = models.FloatField(default=0.0, blank=True)
    price              = models.FloatField(default=0.0, blank=True)
    service            = models.FloatField(default=0.0, blank=True)
    environment        = models.FloatField(default=0.0, blank=True)
    reviewed_people_no = models.IntegerField(default=0, blank=True)
    average            = models.FloatField(default=0.00, blank=True)
    status             = models.CharField(max_length=50, default='N/A', blank=True, null=True)    
    star1              = models.CharField(max_length=50, default='fa-star-o text-secondary')
    star2              = models.CharField(max_length=50, default='fa-star-o text-secondary')
    star3              = models.CharField(max_length=50, default='fa-star-o text-secondary')
    star4              = models.CharField(max_length=50, default='fa-star-o text-secondary')
    star5              = models.CharField(max_length=50, default='fa-star-o text-secondary')

    created_at         = models.DateTimeField(auto_now=True)
    updated_at         = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.restaurant.title + ": " + self.status + " - " + str(self.average)


















class ServiceTime(models.Model):
    restaurant         = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    open_at            = models.TimeField(blank=True, default='08:00:00')
    close_at           = models.TimeField(blank=True, default='20:00:00')
    saturday           = models.BooleanField(default=True, blank=True)
    sunday             = models.BooleanField(default=True, blank=True)    
    monday             = models.BooleanField(default=True, blank=True)
    tuesday            = models.BooleanField(default=True, blank=True)
    wednesday          = models.BooleanField(default=True, blank=True)
    thursday           = models.BooleanField(default=True, blank=True)
    friday             = models.BooleanField(default=True, blank=True)
    created_at         = models.DateTimeField(auto_now=True)
    updated_at         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.restaurant.title












def restaurant_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def restaurant_post_save_receiver(sender, instance, *args, **kwargs):
    qs = RestaurantReview.objects.filter(restaurant=instance)
    if not qs.exists():    
        rr = RestaurantReview()
        rr.restaurant = instance
        rr.save()
    qs = ServiceTime.objects.filter(restaurant=instance)
    if not qs.exists():
        st = ServiceTime()
        st.restaurant = instance
        st.save()

pre_save.connect(restaurant_pre_save_receiver, sender=Restaurant)
post_save.connect(restaurant_post_save_receiver, sender=Restaurant)
