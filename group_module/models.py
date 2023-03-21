from django.conf import settings
from django.db import models

from account_module.models import User


# Create your models here.
class GroupModel(models.Model):
    avatar = models.ImageField(upload_to='group/', default=f'{settings.MEDIA_ROOT}/group/group-default.png')
    group_name = models.CharField(max_length=100, null=False, blank=False)
    group_description = models.TextField(null=False, blank=False)
    group_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')

    def __str__(self):
        return self.group_name

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        self.save()

    class Meta:
        db_table = 'group'
