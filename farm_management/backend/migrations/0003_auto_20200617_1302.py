# Generated by Django 3.0.7 on 2020-06-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_parturation_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parturation',
            name='date_served',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='parturation',
            name='expected_date',
            field=models.DateTimeField(),
        ),
    ]