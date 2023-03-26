from django.contrib import admin

from profile_module.models import UserProfile
from . import models


# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'password',
              'profile']
    list_display = ['username', 'email', 'profile']

    def save_form(self, request, form, change):
        user = super().save_form(request, form, change)
        if not user.profile:
            profile = UserProfile(see_user=self)
            profile.save()
            user.profile = profile
        user.set_password(form.cleaned_data['password'])
        user.save()
        return user
