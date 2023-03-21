from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20, blank=True, null=False)

    def __str__(self):
        if self.get_full_name() != '':
            return self.get_full_name()
        else:
            return self.username
