# Generated by Django 2.1 on 2019-10-09 17:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('hour', models.TimeField(default=datetime.datetime.now)),
                ('bonus_place', models.CharField(default='Sonette, bâtiment, position GPS...', max_length=200)),
                ('carry', models.TextField(default='Exemple : Ramenez du pain, du coca, etc... ')),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=500)),
                ('free', models.BooleanField(default=True)),
                ('picture', models.ImageField(upload_to='events')),
                ('private', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
