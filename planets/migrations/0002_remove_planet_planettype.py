# Generated by Django 2.1.2 on 2018-11-08 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planet',
            name='planetType',
        ),
    ]