# Generated by Django 4.2.3 on 2024-01-08 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('strip_id', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=10, verbose_name='Contact Phone Number')),
                ('email', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('address_1', models.CharField(max_length=255, verbose_name='Street Address/PO Box')),
                ('address_2', models.CharField(max_length=255, verbose_name='Apt/Suite')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('zip_code', models.CharField(max_length=255, verbose_name='Zipcode')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('hexkey', models.CharField(max_length=32)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(default='Pending Deposit', max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client')),
                ('documents', models.ManyToManyField(to='site_app.document')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Project Name')),
                ('date', models.CharField(max_length=10)),
                ('scope', models.CharField(max_length=255, verbose_name='Project-Type/Scope')),
                ('details', models.CharField(max_length=3000, verbose_name='Project Details')),
                ('slug', models.SlugField(max_length=32, unique=True)),
                ('location', models.CharField(max_length=255, verbose_name='Location type')),
                ('status', models.CharField(default='pending', max_length=25)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='RequestReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=3000)),
                ('date_posted', models.DateField(auto_now=True)),
                ('read', models.BooleanField(default=False)),
                ('project_request_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.projectrequest')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scope', models.CharField(max_length=255)),
                ('services', models.TextField(blank=True, max_length=5000)),
                ('project_cost', models.FloatField(default='600.00')),
                ('deposit', models.FloatField(default='0.00')),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.project')),
                ('project_request_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.projectrequest')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=3000)),
                ('date_posted', models.DateField(auto_now=True)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.project')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
