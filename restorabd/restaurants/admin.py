from django.contrib import admin
from .models import Restaurant, ServiceTime, RestaurantReview
class ServiceTimeAdmin(admin.ModelAdmin):
    list_display = [
    	'__str__', 'saturday', 'sunday', 
    	'monday', 'tuesday', 'wednesday', 'thursday', 
    	'friday'
    ]
    list_editable = [
    	'saturday', 'sunday', 'monday', 
        'tuesday', 'wednesday', 'thursday', 
    	'friday'
    ]
    class Meta:
        model = Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'is_active', 'is_orderable']
    list_editable = ['is_active', 'is_orderable']
    class Meta:
        model = Restaurant



admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(ServiceTime, ServiceTimeAdmin)
admin.site.register(RestaurantReview)