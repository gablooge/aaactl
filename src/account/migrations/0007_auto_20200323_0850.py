# Generated by Django 2.2.11 on 2020-03-23 08:50

from django.db import migrations, models

import account.models


class Migration(migrations.Migration):
    dependencies = [("account", "0006_organization_user")]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="name",
            field=models.CharField(
                default=account.models.generate_org_name, max_length=255, unique=True
            ),
        )
    ]
