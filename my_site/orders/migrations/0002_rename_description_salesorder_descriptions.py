# Generated by Django 4.1.2 on 2022-10-31 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="salesorder",
            old_name="description",
            new_name="descriptions",
        ),
    ]