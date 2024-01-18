# Generated by Django 4.2.3 on 2024-01-08 04:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=8)),
                ('percent', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.FloatField(default=0.0, max_length=8)),
                ('details', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.CharField(blank=True, max_length=100)),
                ('billed', models.FloatField(default=0.0)),
                ('paid', models.FloatField(default=0.0)),
                ('details', models.TextField(max_length=500)),
                ('fufiled', models.BooleanField(default=False)),
                ('due_date', models.DateField(blank=True, default=datetime.date(2024, 1, 7))),
                ('open_date', models.DateField(auto_now=True)),
                ('status', models.CharField(default='draft', max_length=30)),
                ('payment_link', models.URLField(blank=True, null=True)),
                ('payment_type', models.CharField(max_length=30)),
                ('credit_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.credit')),
                ('cupon_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.coupon')),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.project')),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateField(auto_created=True)),
                ('amount', models.FloatField(default=5.0)),
                ('receipt', models.CharField(blank=True, max_length=400)),
                ('item_id', models.CharField(blank=True, max_length=400)),
                ('billing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.invoice')),
            ],
        ),
    ]
