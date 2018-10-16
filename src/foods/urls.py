from django.conf.urls import url, include
from . import views

app_name = 'foods'

urlpatterns = [
	url(r'^$', views.list_view, name='list'),
	url(r'^(?P<slug>[\w-]+)/', views.detail_view, name='profile'),
]