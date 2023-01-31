# Generated by Django 3.2.16 on 2023-01-30 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0016_organizationproduct_notes'),
        ('account', '0034_impersonation'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationmanagedpermission',
            name='product',
            field=models.ForeignKey(blank=True, help_text='Perimission management enabled through product', null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.organizationproduct'),
        ),
    ]
