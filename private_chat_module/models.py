from django.db import models

from account_module.models import User
from conversation_module.models import Conversation


# Create your models here.
class PrivateChat(models.Model):
    members = models.ManyToManyField(User)
    conversation = models.OneToOneField(Conversation, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.conversation = Conversation.objects.create()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.members.all()[0]} - {self.members.all()[1]}'