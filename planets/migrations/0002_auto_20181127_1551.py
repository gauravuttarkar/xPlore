# Generated by Django 2.1.2 on 2018-11-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarplanets',
            name='density',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarplanets',
            name='equatorialRadius',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarplanets',
            name='escapeVelocity',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarplanets',
            name='meanDistanceFromSuninAU',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarplanets',
            name='moons',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarplanets',
            name='orbitalPeriod',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarplanets',
            name='rings',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarplanets',
            name='surfaceArea',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarplanets',
            name='temperature',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarplanets',
            name='volume',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
