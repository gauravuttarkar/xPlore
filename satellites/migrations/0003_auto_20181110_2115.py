# Generated by Django 2.1.2 on 2018-11-10 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satellites', '0002_auto_20181110_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='artificalsatellite',
            name='classOfOrbit',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='artificalsatellite',
            name='dateOfLaunch',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='artificalsatellite',
            name='launchSite',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='artificalsatellite',
            name='launchVehicle',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='artificalsatellite',
            name='period',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='artificalsatellite',
            name='purpose',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='artificalsatellite',
            name='typeOfOrbit',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='artificalsatellite',
            name='users',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
