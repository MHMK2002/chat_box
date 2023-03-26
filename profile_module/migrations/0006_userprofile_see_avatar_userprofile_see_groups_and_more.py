# Generated by Django 4.1.7 on 2023-03-26 01:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_module', '0005_alter_userprofile_about_me_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='see_avatar',
            field=models.CharField(choices=[('Everyone', 'Everyone'), ('Contacts', 'Contacts'), ('Nobody', 'Nobody')], default='Everyone', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='see_groups',
            field=models.CharField(choices=[('Everyone', 'Everyone'), ('Contacts', 'Contacts'), ('Nobody', 'Nobody')], default='Everyone', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='see_status',
            field=models.CharField(choices=[('Everyone', 'Everyone'), ('Contacts', 'Contacts'), ('Nobody', 'Nobody')], default='Everyone', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_seen',
            field=models.BooleanField(choices=[('Everyone', 'Everyone'), ('Contacts', 'Contacts'), ('Nobody', 'Nobody')], default='Everyone'),
        ),
        migrations.CreateModel(
            name='UserMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='user/media/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'mp4', 'mkv'])])),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='profile_module.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='UserAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='user/attachments/', validators=[django.core.validators.FileExtensionValidator(['doc', 'docx', 'pdf', 'txt', 'xls', 'xlsx', 'zip', 'rar'])])),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='profile_module.userprofile')),
            ],
        ),
    ]