from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from Events.models import Event, Notification, Participation
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import urllib.request
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from .forms import RegistrationForm, UserProfileForm

# Create your views here.

#affichage de tous les événements
def index(request):
	return HttpResponseRedirect('/events')

#liste des événements
def event_list(request):
	now = datetime.today()
	events=Event.objects.filter(date__gte=now).order_by('date')
	return render(request, 'home/event_list.html', {'events':events})

#créer un compte
def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			events = Event.objects.all()
			return HttpResponseRedirect(reverse('login'))
	else:
		form = RegistrationForm()
	return render(request, 'home/register.html', {'form':form})

#accéder à son profil
@login_required
def profile(request, username):
	my_profile=False
	current_user=request.user
	if username!="me":
		profile_user=get_object_or_404(User, username=username)
	else:
		profile_user=current_user
	if current_user==profile_user:
		my_profile=True
	events_organized=Event.objects.filter(author=profile_user)
	print(profile_user.username)
	events_attended=Participation.objects.filter(member=profile_user)
	e_count=events_organized.count()
	if my_profile:
		profile=current_user.profile
	else:
		profile=profile_user.profile
	notifications=Notification.objects.filter(receiver=current_user)
	# On affiche les informations relatives à ce mec
	return render(request, 'home/profile.html', {'profile': profile, 'events_organized':events_organized, 'events_attended':events_attended, 'e_count':e_count, 'my_profile':my_profile, 'notifications':notifications})

#Modifier son profil
@login_required
def edit_profile(request):
	current_user = request.user
	profile = UserProfile.objects.get(user=current_user)
	if request.method == "POST":
		form = UserProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.save()
			return HttpResponseRedirect(reverse('profile', kwargs={'username': current_user.username}))
	else:
		form = UserProfileForm(instance=profile)
	return render(request, 'home/edit_profile.html', {'form':form})

@login_required
def notifications(request):
	current_user=request.user
	notifications=Notification.objects.filter(receiver=current_user)
	return render(request, 'home/notifications.html', {'notifications':notifications})
