from django.contrib import admin
from .models import Cart, Order, Discount

class CartAdmin(admin.ModelAdmin):
	pass

class OrderAdmin(admin.ModelAdmin):
	pass
class DiscountAdmin(admin.ModelAdmin):
	pass
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)