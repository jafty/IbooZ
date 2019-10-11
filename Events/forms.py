import re
from django import forms
from django.contrib.auth.models import User
from .models import Event, Notification
from django.utils.translation import ugettext_lazy as _



class EventForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = ('title', 'picture', 'date', 'description', 'address', 'bonus_place', 'hour')

		labels = {
			'title': _('Nom de ton événement'),
			'picture': _("Image de ton événement"),
			'date': _('Date (YYYY-MM-DD)'),
			'description': _('Description'),
			'address': _('Adresse'),
			'hour': _('Heure de début'),
			'bonus_place': _('Précisions sur le lieu'),
		}



class NotificationForm(forms.ModelForm):

	class Meta:
		model = Notification
		fields = ('msg_content',)

		labels = {
			'msg_content': _("Dites deux trois mots à l'organisateur pour avoir plus de chances d'être accepté !"),
		}
