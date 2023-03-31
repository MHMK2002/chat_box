from django.conf import settings
from django.db import models

from account_module.models import User
from conversation_module.models import Conversation


# Create your models here.
class Channel(models.Model):
    avatar = models.ImageField(upload_to='channel/', default=f'{settings.MEDIA_ROOT}/channel/channel-default.png')
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(User)
    conversation = models.OneToOneField(Conversation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.conversation = Conversation.objects.create()
        super().save(force_insert, force_update, using, update_fields)



