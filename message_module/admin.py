from django.contrib import admin

from message_module.models import Message


# Register your models here.
@admin.register(Message)
class MessageModelAdmin(admin.ModelAdmin):
    pass
