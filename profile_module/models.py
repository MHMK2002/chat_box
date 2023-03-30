from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


class UserStatus(models.TextChoices):
    ACTIVE = 'active'
    AWAY = 'away'
    DO_NOT_DISTURB = 'do not disturb'


class UserPrivacy(models.TextChoices):
    EVERYONE = 'Everyone'
    CONTACTS = 'Contacts'
    NOBODY = 'Nobody'


class UserMedia(models.Model):
    profile = models.ForeignKey('profile_module.UserProfile', on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='user/media/', validators=[FileExtensionValidator(['jpg', 'png', 'mp4', 'mkv'])])

    def __str__(self):
        file_name = self.file.name.split('/')[-1]
        return f'{self.profile.user.username} media: {file_name}'


class UserAttachment(models.Model):
    profile = models.ForeignKey('profile_module.UserProfile', on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='user/attachments/',
                            validators=[
                                FileExtensionValidator(['doc', 'docx', 'pdf', 'txt', 'xls', 'xlsx', 'zip', 'rar'])])

    def __str__(self):
        file_name = self.file.name.split('/')[-1]
        return f'{self.profile.user.username} attachment: {file_name}'


class UserProfile(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    avatar = models.ImageField(default=f'{settings.BASE_DIR}\\media\\user\\user-default.png',
                               upload_to='user/',
                               blank=True,
                               null=True)
    last_seen = models.CharField(choices=UserPrivacy.choices, default=UserPrivacy.EVERYONE, max_length=20)
    about_me = models.TextField(blank=True, null=True)
    short_about_me = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=20, choices=UserStatus.choices, default=UserStatus.ACTIVE)
    contacts = models.ManyToManyField('account_module.User', related_name='contacts', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    see_avatar = models.CharField(choices=UserPrivacy.choices, default=UserPrivacy.EVERYONE, max_length=20)
    see_status = models.CharField(choices=UserPrivacy.choices, default=UserPrivacy.EVERYONE, max_length=20)
    see_channels = models.CharField(choices=UserPrivacy.choices, default=UserPrivacy.EVERYONE, max_length=20)

    def __str__(self):
        return f'{self.user.username} profile'
