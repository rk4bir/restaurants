from django.conf.urls import url
from .views import *
app_name = 'restaurants'

urlpatterns = [
	url(r'^$', restaurant_list, name='list'),
	url(r'^restaurant-json-data', restauranJson_view, name='restauran-json'),
    url(r'^(?P<slug>[\w-]+)/$', restaurant_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/review/$', restaurant_review, name='review'),
]
