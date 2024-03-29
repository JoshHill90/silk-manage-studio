# Generated by Django 4.2.3 on 2024-01-08 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file_path', models.CharField(blank=True, max_length=255, null=True)),
                ('doc_type', models.CharField(blank=True, choices=[('site', 'site'), ('client', 'client')], max_length=50, null=True)),
                ('doc_content', models.TextField(blank=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('kind', models.CharField(blank=True, choices=[('pdf', 'pdf'), ('docx', 'docx')], max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
