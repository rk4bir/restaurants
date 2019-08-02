from django.urls import re_path
from . import views
app_name = 'orders'

urlpatterns = [
	re_path(r'^cart-add/$', views.addToCart_view, name='cart-add'),
	re_path(r'^check-discount/$', views.checkDiscountCode_view, name='check-discount'),
	re_path(r"^mylist/$", views.myOrders_view, name='mylist'),
	re_path(r'^management/$', views.orderManage_view, name='management'),
	re_path(r'^order-add/$', views.newOrder_view, name='order-add'),
	re_path(r'^(?P<order_id>[0-9A-Za-z]+)/$', views.OrderDetail_view, name='detail'),
	re_path(r'^(?P<order_id>[0-9A-Za-z]+)/delete/$', views.DeleteOrder_view, name='delete' ),
	re_path(r'^(?P<order_id>[0-9A-Za-z]+)/update-status/$', views.updateStatus_view, name='update-status' ),
	re_path(r'^(?P<order_id>[0-9A-Za-z]+)/update-visibility/$', views.updateVisibility_view, name='update-visibility' ),
	re_path(r'^(?P<order_id>[0-9A-Za-z]+)/update-payment-status/$', views.updatePaymentStatus_view, name='update-payment-status' ),
]