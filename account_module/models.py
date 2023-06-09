from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from profile_module.models import UserProfile


# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=True)
    email_activation_code = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        if self.get_full_name() != '':
            return self.get_full_name()
        else:
            return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.profile.save()

    def set_email_activation_code(self):
        self.email_activation_code = User.objects.make_random_password(length=100)
        self.save()

    def unread_messages(self) -> int:
        count = 0
        for chat in self.privatechat_set.all():
            count += chat.conversation.unread_messages()

        for chat in self.channel_set.all():
            count += chat.conversation.unread_messages()

        return count
