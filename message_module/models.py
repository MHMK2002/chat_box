from django.db import models

from account_module.models import User
from group_module.models import GroupModel


# Create your models here.
class MessageModel(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, related_name='group')

    def __str__(self):
        return self.message

