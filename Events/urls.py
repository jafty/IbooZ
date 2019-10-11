from django.urls import path, re_path
from . import views

urlpatterns = [
	path('/', views.event_list, name='event_list'),
	path('/<int:pk>', views.event_detail, name='event_detail'),
	path('/<int:pk>/request', views.event_request, name='event_request'),
	path('/new', views.event_new, name='event_new'),
	path('/<int:pk>/<cand>/accept', views.accept_event_request, name='accept_event_request'),
	re_path(r'^(?P<pk>[0-9]+)/(?P<cand>[\w-]+)/deny$', views.deny_event_request, name='deny_event_request'),
	path('/<int:pk>/edit_my_event', views.edit_my_event, name='edit_my_event'),

]
