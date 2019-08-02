from django.urls import path, include, re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from general.views import *
from reviews.views import create_view
from notifications.views import notificationList_view, seenStatus_view


urlpatterns = [
    re_path(r'^$', index_view, name='homepage'),
    re_path(r'^404notfound/', error_404_view, name='404NotFound'),
    #url(r'^500servererror/', error_500_view, name='error500'),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^notifications/$', notificationList_view, name='notifications'),
    re_path(r'^orders/', include('orders.urls')),
    re_path(r'^restaurants/', include('restaurants.urls')),
    re_path(r'^reviews/', include('reviews.urls')),
    re_path(r'^review/create/', create_view, name='review-create'),
    re_path(r'^notifications/seen-status/$', seenStatus_view, name='notf-seen'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
