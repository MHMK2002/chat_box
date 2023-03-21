from django.contrib import admin

from group_module.models import GroupModel


# Register your models here.
@admin.register(GroupModel)
class GroupModelAdmin(admin.ModelAdmin):
    pass
