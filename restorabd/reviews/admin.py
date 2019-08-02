from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = [
    	'restaurant','average', 'title'
    ]
    list_editable = [
    	'average', 'title'
    ]
    list_display_links = [
    	'restaurant'
    ]
    class Meta:
        model = Review

admin.site.register(Review, ReviewAdmin)