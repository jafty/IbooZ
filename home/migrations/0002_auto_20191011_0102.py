# Generated by Django 2.1 on 2019-10-10 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_pic_url',
            new_name='profile_pic',
        ),
    ]
