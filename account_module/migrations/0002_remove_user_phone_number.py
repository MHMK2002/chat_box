# Generated by Django 4.1.7 on 2023-03-21 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
