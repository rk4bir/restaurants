from django.conf.urls import url
from . import views

app_name = 'accounts'
#(?P<slug>[\w-]+)/

urlpatterns = [
	url(r'^activate/$', views.activate_view, name='activate'),
    url(r'^change-password/$', views.changePassword_view, name='change-password'),
    url(r'^delete/$', views.delete_view, name='delete'),
    url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^account-notices/$', views.accountNotices_view, name='account-notices'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^send-code/$', views.sendCode_view, name='send-code'),
    url(r'^update/$', views.updateBasicInfo, name='update'),
    
    url(r'^(?P<username>[\w-]+)/$', views.profile_view, name='profile'),
    url(r'^(?P<username>[\w-]+)/favourites/$', views.favourites_view, name='favourites'),
    url(r'^(?P<username>[\w-]+)/orders/$', views.orders_view, name='orders'),
    url(r'^(?P<username>[\w-]+)/reviews/$', views.reviews_view, name='reviews'),
    url(r'^(?P<username>[\w-]+)/settings/$', views.settings_view, name='settings'),
]