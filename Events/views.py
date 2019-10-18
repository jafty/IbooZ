from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Event, Notification, Participation
from home.models import UserProfile
from django.contrib.auth.models import User
from .forms import EventForm, NotificationForm
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
# Create your views here.

#affichage de tous les événements
def event_list(request):
	now = datetime.today()
	events=Event.objects.filter(date__gte=now).order_by('date')
	return render(request, 'events/event_list.html', {'events':events})

#affichage du détail d'un événement
def event_detail(request, pk):
	my_event=False
	event = get_object_or_404(Event, pk=pk)
	event_author = event.author
	profile = get_object_or_404(UserProfile, user=event_author)
	if event_author == request.user:
		my_event=True
	return render(request, 'events/event_detail.html', {'event':event, 'profile':profile, 'my_event':my_event})

#Création d'un nouvel event
@login_required
def event_new(request):
	current_user = request.user
	profile = UserProfile.objects.get(user = current_user)
	if request.method == "POST":
		form = EventForm(request.POST, request.FILES or None)
		if form.is_valid():
			event = form.save(commit=False)
			event.author = current_user
			event.save()
			return HttpResponseRedirect(reverse('event_list'))
	else:
		form = EventForm()
	return render(request, 'events/event_new.html', {'form':form})

#Demande de participation à un événement
@login_required
def event_request(request, pk):
	event = get_object_or_404(Event, pk=pk)
	if request.method == "POST":
		form = NotificationForm(request.POST or None)
		if form.is_valid():
			ev_request = form.save(commit=False)
			ev_request.event = event
			ev_request.category = 'DM'
			ev_request.receiver = event.author
			ev_request.sender = request.user
			ev_request.save()
			return HttpResponseRedirect(reverse('event_list'))
	else:
		form = NotificationForm()

	return render(request, 'events/event_request.html', {'form':form})

#Validation de la participation à un événement
@login_required
def accept_event_request(request, pk, cand):
	current_user=request.user
	candidate=User.objects.get(username=cand)
	event = Event.objects.get(pk=pk)
	Participation.objects.create(member=candidate, event=event)
	Notification.objects.create(category='AC', sender=current_user, receiver=candidate, event=event, msg_content="Vous avez été autorisé à participer à l'évènement.")
	Notification.objects.filter(event=event, sender=candidate).delete()

	return render(request, 'events/refuse.html')

#Refus de la participation à un événement
@login_required
def deny_event_request(request, pk, cand):
	current_user=request.user
	candidate=User.objects.get(username=cand)
	event = Event.objects.get(pk=pk)

	Notification.objects.create(category='DE', sender=current_user, receiver=candidate, event=event, msg_content="Vous n'avez pas été autorisé à participer à l'évènement")
	Notification.objects.filter(event=event, sender=candidate).delete()

	return render(request, 'events/refuse.html')

#Editer son propre événement
@login_required
def edit_my_event(request, pk):
	current_user=request.user
	event=Event.objects.get(pk=pk)
	if current_user!=event.author:
		HttpResponseRedirect(reverse('event_list'))
	event = Event.objects.get(pk=pk)
	if request.method == "POST":
		form = EventForm(request.POST, request.FILES, instance=event)
		if form.is_valid():
			event = form.save(commit=False)
			event.save()
			return HttpResponseRedirect(reverse('event_list'))
	else:
		form = EventForm(instance=event)
	return render(request, 'events/edit_my_event.html', {'form':form, 'pk':pk})
