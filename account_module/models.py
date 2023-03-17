from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(default='/media/user/default.png', upload_to='user', blank=True, null=True)
    about_user = models.TextField()
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.username

