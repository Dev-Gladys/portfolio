# Generated by Django 5.2 on 2025-05-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GladysOro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
