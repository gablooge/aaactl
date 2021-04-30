# Generated by Django 2.2.20 on 2021-04-23 12:24

import account.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_grainy.fields
import django_handleref.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20210423_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalAPIKey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', django_handleref.models.CreatedDateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', django_handleref.models.UpdatedDateTimeField(auto_now=True, verbose_name='Updated')),
                ('version', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('ok', 'Ok'), ('pending', 'Pending'), ('deactivated', 'Deactivated'), ('failed', 'Failed'), ('expired', 'Expired')], default='ok', max_length=12)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('key', models.CharField(default=account.models.generate_api_key, max_length=255, unique=True)),
                ('managed', models.BooleanField(default=True, help_text='Is the API Key managed by the owner')),
            ],
            options={
                'verbose_name': 'Internal API Key',
                'verbose_name_plural': 'Internal API Keys',
                'db_table': 'account_internal_api_key',
            },
            managers=[
                ('handleref', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='apikey',
            options={'verbose_name': 'Personal API Key', 'verbose_name_plural': 'Personal API Keys'},
        ),
        migrations.CreateModel(
            name='InternalAPIKeyPermission',
            fields=[
                ('namespace', models.CharField(help_text="Permission namespace (A '.' delimited list of keys", max_length=255)),
                ('permission', django_grainy.fields.PermissionField(default=1)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', django_handleref.models.CreatedDateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', django_handleref.models.UpdatedDateTimeField(auto_now=True, verbose_name='Updated')),
                ('version', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('ok', 'Ok'), ('pending', 'Pending'), ('deactivated', 'Deactivated'), ('failed', 'Failed'), ('expired', 'Expired')], default='ok', max_length=12)),
                ('api_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grainy_permissions', to='account.InternalAPIKey')),
            ],
            options={
                'verbose_name': 'Internal API Key Permission',
                'verbose_name_plural': 'Internal API Key Permissions',
                'db_table': 'account_internal_api_key_permission',
            },
        ),
    ]
