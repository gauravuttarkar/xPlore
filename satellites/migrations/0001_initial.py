# Generated by Django 2.1.2 on 2018-11-10 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planets', '0002_remove_planet_planettype'),
    ]

    operations = [
        migrations.CreateModel(
            name='artificalSatellite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='naturalSatellite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default=None, max_length=300)),
                ('discoveredBy', models.CharField(default=None, max_length=100)),
                ('discoveredIn', models.CharField(default=None, max_length=10)),
                ('meanRadius', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='satellite',
            fields=[
                ('satelliteName', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=100, null=True)),
                ('orbitingBody', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='planets.planet')),
            ],
        ),
        migrations.AddField(
            model_name='naturalsatellite',
            name='satelliteName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='satellites.satellite'),
        ),
        migrations.AddField(
            model_name='artificalsatellite',
            name='satelliteName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='satellites.satellite'),
        ),
    ]