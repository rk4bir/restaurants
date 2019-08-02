from django.urls import re_path
from .views import *
app_name = 'restaurants'

urlpatterns = [
	re_path(r'^$', restaurant_list, name='list'),
	re_path(r'^restaurant-json-data', restauranJson_view, name='restauran-json'),
    re_path(r'^(?P<slug>[\w-]+)/$', restaurant_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/review/$', restaurant_review, name='review'),
]
