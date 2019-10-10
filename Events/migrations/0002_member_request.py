# Generated by Django 2.1 on 2019-10-09 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='member_event', to='Events.Event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_content', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='request_event', to='Events.Event')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='request_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='request_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
