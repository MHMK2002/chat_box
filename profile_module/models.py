from django.conf import settings
from django.db import models


class UserStatus(models.TextChoices):
    ACTIVE = 'active'
    AWAY = 'away'
    DO_NOT_DISTURB = 'do not disturb'


class UserProfile(models.Model):
    avatar = models.ImageField(default=f'{settings.BASE_DIR}\\media\\user\\user-default.png',
                               upload_to='user/',
                               blank=True,
                               null=True)
    last_seen = models.BooleanField(default=False)
    about_me = models.TextField(blank=True, null=True)
    short_about_me = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=20, choices=UserStatus.choices, default=UserStatus.ACTIVE)
    contacts = models.ManyToManyField('account_module.User', related_name='contacts', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    # TODO: add field for media and attachments files

    def __str__(self):
        return f'{self.user.username} profile'