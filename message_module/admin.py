from django.contrib import admin

from message_module.models import MessageModel


# Register your models here.
@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    pass
