from django.conf.urls import url
from . import views
app_name = 'orders'

urlpatterns = [
	url(r'^cart-add/$', views.addToCart_view, name='cart-add'),
	url(r'^check-discount/$', views.checkDiscountCode_view, name='check-discount'),
	url(r"^mylist/$", views.myOrders_view, name='mylist'),
	url(r'^management/$', views.orderManage_view, name='management'),
	url(r'^order-add/$', views.newOrder_view, name='order-add'),
	url(r'^(?P<order_id>[0-9A-Za-z]+)/$', views.OrderDetail_view, name='detail'),
	url(r'^(?P<order_id>[0-9A-Za-z]+)/delete/$', views.DeleteOrder_view, name='delete' ),
	url(r'^(?P<order_id>[0-9A-Za-z]+)/update-status/$', views.updateStatus_view, name='update-status' ),
	url(r'^(?P<order_id>[0-9A-Za-z]+)/update-visibility/$', views.updateVisibility_view, name='update-visibility' ),
	url(r'^(?P<order_id>[0-9A-Za-z]+)/update-payment-status/$', views.updatePaymentStatus_view, name='update-payment-status' ),
]