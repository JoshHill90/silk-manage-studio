# Generated by Django 4.2.3 on 2024-01-18 06:28

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_dispaly_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispaly',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
    ]