# Generated by Django 3.0.7 on 2020-06-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200617_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='parturation',
            name='breed',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='parturation',
            name='vet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
