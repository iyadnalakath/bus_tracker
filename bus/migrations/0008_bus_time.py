# Generated by Django 4.1.5 on 2023-01-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0007_busstop_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]