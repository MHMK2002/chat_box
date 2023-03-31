# Generated by Django 4.1.7 on 2023-03-31 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userattachment',
            name='bookmark',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermedia',
            name='type',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video')], default=None, max_length=20),
            preserve_default=False,
        ),
    ]
