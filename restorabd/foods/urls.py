from django.urls import path, include, re_path
from . import views

app_name = 'foods'

urlpatterns = [
	re_path(r'^$', views.list_view, name='list'),
	re_path(r'^(?P<slug>[\w-]+)/', views.detail_view, name='profile'),
]