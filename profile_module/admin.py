from django.contrib import admin

from profile_module.models import UserProfile, UserStatus


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

