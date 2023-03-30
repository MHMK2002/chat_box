from account_module.models import User
from django.db import models


class Conversation(models.Model):
    is_active = models.BooleanField(default=True)
