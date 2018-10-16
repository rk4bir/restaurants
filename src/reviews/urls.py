from django.conf.urls import url
from . import views
app_name = 'reviews'
urlpatterns = [
	url(r'^create/', views.create_view, name='create'),
	url(r'^(?P<pk>[0-9]+)/delete/', views.delete_view, name='delete'),
]