# Generated by Django 4.1.5 on 2023-01-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0009_alter_bus_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]