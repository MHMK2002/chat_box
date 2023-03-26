# Generated by Django 4.1.7 on 2023-03-25 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_module', '0004_remove_userprofile_user'),
        ('account_module', '0002_remove_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='profile_module.userprofile'),
        ),
    ]
