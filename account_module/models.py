from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


# Create your models here.
class UserStatus(models.TextChoices):
    ACTIVE = 'active'
    AWAY = 'away'
    DO_NOT_DISTURB = 'do not disturb'


class User(AbstractUser):
    avatar = models.ImageField(default=f'{settings.BASE_DIR}\\media\\user\\user-default.png',
                               upload_to='user',
                               blank=True,
                               null=True)
    about_user = models.TextField()
    last_seen = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=UserStatus.choices, default=UserStatus.ACTIVE)
    location = models.CharField(max_length=300, blank=True, null=True)
    short_description = models.CharField(max_length=300, blank=False, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=False)

    def __str__(self):
        if self.get_full_name() != '':
            return self.get_full_name()
        else:
            return self.username
