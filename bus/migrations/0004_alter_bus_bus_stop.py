# Generated by Django 4.1.5 on 2023-01-11 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_alter_bus_bus_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='bus_stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.busstop'),
        ),
    ]
