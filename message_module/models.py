from django.db import models

from account_module.models import User
from conversation_module.models import Conversation


# Create your models here.
class MessageModel(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    seen_by = models.ManyToManyField(User, related_name='seen_by')

    def __str__(self):
        return self.message
