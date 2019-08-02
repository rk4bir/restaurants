from django.contrib import admin
from .models import Account, User


class AccountAdmin(admin.ModelAdmin):
	list_display = ['user', 'name', 'phone', 'city', 'is_active', 'activation_code', 'pass_change_code']
	list_display_links = ["user", 'phone', 'name']
	list_filter = ['user', 'city', 'name', 'is_active']
	fields = []
	search_fields = ['name', 'city', 'phone']

admin.site.register(Account, AccountAdmin)
