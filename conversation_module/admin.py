from django.contrib import admin

from conversation_module.models import Conversation, GroupConversation, PrivateConversation


# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupConversation)
class GroupConversationAdmin(admin.ModelAdmin):
    pass


@admin.register(PrivateConversation)
class PrivateConversationAdmin(admin.ModelAdmin):
    pass
