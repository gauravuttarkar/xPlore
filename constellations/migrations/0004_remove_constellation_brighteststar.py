# Generated by Django 2.1.2 on 2018-11-26 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constellations', '0003_auto_20181106_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constellation',
            name='brightestStar',
        ),
    ]
