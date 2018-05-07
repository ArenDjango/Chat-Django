# Generated by Django 2.0.3 on 2018-04-17 11:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_userprofile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='zayavkadruzya',
            field=models.ManyToManyField(blank=True, related_name='addingfriend', to=settings.AUTH_USER_MODEL),
        ),
    ]
