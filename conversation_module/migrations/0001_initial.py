# Generated by Django 4.1.7 on 2023-03-21 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group_module', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='PrivateConversation',
            fields=[
                ('conversation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='conversation_module.conversation')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('conversation_module.conversation',),
        ),
        migrations.CreateModel(
            name='GroupConversation',
            fields=[
                ('conversation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='conversation_module.conversation')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='group_module.groupmodel')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('conversation_module.conversation',),
        ),
    ]
