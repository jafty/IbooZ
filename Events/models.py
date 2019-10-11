from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

#Classe événement
class Event(models.Model):
	title = models.CharField(max_length=30)
	author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
	date = models.DateField(default=datetime.now)
	hour = models.TimeField(default=datetime.now)
	bonus_place = models.CharField(default="Sonette, bâtiment, position GPS...", max_length=200)
	description = models.TextField()
	address = models.CharField(max_length=500)
	picture = models.ImageField(upload_to="events", max_length=100)



	@property
	def is_past_due(self):
		return (date.today()+timedelta(hours=6)) > self.date

	@property
	def this_week(self):
		return self.date < (date.today()+timedelta(days=7))


	def __str__(self):
		return self.title

#Gestion des notifications
class Notification(models.Model):
	category = models.CharField(max_length=2);
	event = models.ForeignKey(Event, related_name="notification_event", on_delete=models.PROTECT)
	sender = models.ForeignKey('auth.User', related_name="request_sender", on_delete=models.PROTECT)
	receiver = models.ForeignKey('auth.User', related_name="request_receiver", on_delete=models.PROTECT)
	msg_content = models.TextField()
	test = models.BooleanField(default=False)

	def __str__(self):
		return self.sender.username


#Participant à un événement
class Participation(models.Model):
	member = models.ForeignKey(User, related_name="member", on_delete=models.PROTECT)
	event = models.ForeignKey(Event, related_name="member_event", on_delete=models.PROTECT)

	def __str__(self):
		return self.member.username


