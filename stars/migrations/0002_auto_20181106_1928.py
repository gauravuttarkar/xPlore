# Generated by Django 2.1.2 on 2018-11-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='age',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='apparentMagnitude',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='confirmedPlanets',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='declination',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='distance',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='mass',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='notes',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='rightAscension',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='spectralType',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='star',
            name='temperature',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]