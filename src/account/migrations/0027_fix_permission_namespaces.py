# Generated by Django 3.2.13 on 2022-07-13 11:01

from django.db import migrations

PERMISSION_CHANGES = [
    ("pfxmon", "prefix_monitor"),
    ("pfxset", "prefix_set"),
    ("rsconf", "config.routeserver"),
    ("rs", "routeserver"),
    ("phyport", "physical_port"),
    ("logport", "logical_port"),
    ("virtport", "virtual_port"),
    ("orgkey", "org_key"),
]


def _rename_forward(qset):
    for mperm in qset:
        for old_ns, new_ns in PERMISSION_CHANGES:
            if mperm.namespace.startswith(f"{old_ns}."):
                mperm.namespace = mperm.namespace.replace(f"{old_ns}.", f"{new_ns}.")
                mperm.save()


def _rename_backward(qset):
    for mperm in qset:
        for new_ns, old_ns in PERMISSION_CHANGES:
            if mperm.namespace.startswith(f"{old_ns}."):
                mperm.namespace = mperm.namespace.replace(f"{old_ns}.", f"{new_ns}.")
                mperm.save()


def forwards(apps, schema_editor):

    models = [
        apps.get_model("account", "ManagedPermission"),
        apps.get_model("account", "APIKeyPermission"),
        apps.get_model("account", "OrganizationAPIKeyPermission"),
        apps.get_model("django_grainy", "UserPermission"),
        apps.get_model("django_grainy", "GroupPermission"),
    ]

    for model in models:
        _rename_forward(
            getattr(model, "objects", getattr(model, "handleref", None)).all()
        )


def backwards(apps, schema_editor):

    models = [
        apps.get_model("account", "ManagedPermission"),
        apps.get_model("account", "APIKeyPermission"),
        apps.get_model("account", "OrganizationAPIKeyPermission"),
        apps.get_model("django_grainy", "UserPermission"),
        apps.get_model("django_grainy", "GroupPermission"),
    ]

    for model in models:
        _rename_backward(
            getattr(model, "objects", getattr(model, "handleref", None)).all()
        )


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0026_reftag_pass_2"),
        ("django_grainy", "0001_initial"),
    ]

    operations = [migrations.RunPython(forwards, backwards)]
