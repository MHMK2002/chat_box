# Generated by Django 4.1.7 on 2023-03-26 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_module', '0006_userprofile_see_avatar_userprofile_see_groups_and_more'),
        ('account_module', '0003_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='profile_module.userprofile'),
        ),
    ]