from django.db import models
from polymorphic.models import PolymorphicModel

from account_module.models import User
from group_module.models import GroupModel


class Conversation(PolymorphicModel):
    is_active = models.BooleanField(default=True)
    members = models.ManyToManyField(User, related_name='members', blank=True)

    def get_avatar(self):
        pass

    def get_name(self):
        pass


class GroupConversation(Conversation):
    group = models.OneToOneField(GroupModel, on_delete=models.CASCADE)

    def get_avatar(self):
        return self.group.avatar

    def get_name(self):
        return self.group.group_name


class PrivateConversation(Conversation):
    def __init__(self, member_id):
        super().__init__()
        self.member_id = member_id
        self.user = self.members.exclude(id=self.member_id).first()

    def get_avatar(self):
        return self.user.avatar

    def get_name(self):
        return self.user.__str__()
