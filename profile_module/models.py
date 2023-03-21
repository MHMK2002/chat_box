from django.conf import settings
from django.db import models

from account_module.models import User


class UserStatus(models.TextChoices):
    ACTIVE = 'active'
    AWAY = 'away'
    DO_NOT_DISTURB = 'do not disturb'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(default=f'{settings.BASE_DIR}\\media\\user\\user-default.png',
                               upload_to='user/',
                               blank=True,
                               null=True)
    last_seen = models.BooleanField(default=False)
    about_me = models.TextField()
    short_about_me = models.CharField(max_length=300, blank=False, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=20, choices=UserStatus.choices, default=UserStatus.ACTIVE)
    contacts = models.ManyToManyField(User, related_name='contacts', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    # TODO: add field for media and attachments files
