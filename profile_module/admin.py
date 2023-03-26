from django.contrib import admin

from profile_module.models import UserProfile, UserStatus, UserMedia, UserAttachment


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(UserMedia)
class UserMediaAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAttachment)
class UserAttachmentAdmin(admin.ModelAdmin):
    pass
