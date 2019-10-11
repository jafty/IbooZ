from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.index, name='index'),
	path('register', views.register, name='register'),
	#path('login', auth_views.login, name='login'),
	path('profile', views.profile, name='profile'),
	path('notifications', views.notifications, name='notifications'),
	path('edit_profile', views.edit_profile, name='edit_profile'),
	path('<username>/profile', views.profile, name='profile'),
]
