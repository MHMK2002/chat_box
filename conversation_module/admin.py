from django.contrib import admin

from conversation_module.models import Conversation


# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass
