# Generated by Django 4.2.3 on 2024-02-17 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_dispalykey_expire'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DispalyKey',
            new_name='DisplayKey',
        ),
    ]
