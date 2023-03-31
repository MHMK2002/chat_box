from account_module.models import User
from django.db import models


class Conversation(models.Model):
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Conversation {self.id}'

    def unread_messages(self, user):
        count = 0
        for message in self.messagemodel_set.all().order_by('-created_at'):
            if message.seen_by.filter(id=user.id).exists():
                break
            count += 1
        return count
