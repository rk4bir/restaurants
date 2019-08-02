from django.urls import re_path, path
from . import views

app_name = 'accounts'
#(?P<slug>[\w-]+)/

urlpatterns = [
    path('activate/', views.activate_view, name='activate'),
    path('change-password/', views.changePassword_view, name='change-password'),
    path('delete/', views.delete_view, name='delete'),
    path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
    path('account-notices/', views.accountNotices_view, name='account-notices'),
    path('register/', views.register_view, name='register'),
    path('send-code/', views.sendCode_view, name='send-code'),
    path('update/', views.updateBasicInfo, name='update'),
    
    path('<int:pk>/', views.profile_view, name='profile'),
    path('<int:pk>/favourites/', views.favourites_view, name='favourites'),
    path('<int:pk>/orders/', views.orders_view, name='orders'),
    path('<int:pk>/reviews/', views.reviews_view, name='reviews'),
    path('<int:pk>/settings/', views.settings_view, name='settings'),
]