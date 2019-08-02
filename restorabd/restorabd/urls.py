from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from general.views import *
from reviews.views import create_view
from notifications.views import notificationList_view, seenStatus_view


urlpatterns = [
    url(r'^$', index_view, name='homepage'),
    url(r'^404notfound/', error_404_view, name='404NotFound'),
    #url(r'^500servererror/', error_500_view, name='error500'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^notifications/$', notificationList_view, name='notifications'),
    url(r'^orders/', include('orders.urls')),
    url(r'^restaurants/', include('restaurants.urls')),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^review/create/', create_view, name='review-create'),
    url(r'^notifications/seen-status/$', seenStatus_view, name='notf-seen'),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
