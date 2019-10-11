from django.contrib import admin
from .models import Event, Participation, Notification
# Register your models here.

admin.site.register(Event)
admin.site.register(Participation)
admin.site.register(Notification)

