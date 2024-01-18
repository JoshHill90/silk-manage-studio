# Generated by Django 4.2.3 on 2024-01-08 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_projectevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispaly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('portrait_format', models.CharField(default='square', max_length=50)),
                ('private', models.BooleanField(default=False)),
                ('image_link', models.URLField(blank=True, default=' ')),
                ('cloudflare_id', models.CharField(blank=True, max_length=255)),
                ('silk_id', models.CharField(default='CB01', max_length=50)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client')),
                ('display', models.ManyToManyField(blank=True, null=True, to='gallery.dispaly')),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.project')),
                ('tag', models.ManyToManyField(blank=True, null=True, to='gallery.tag')),
            ],
        ),
    ]