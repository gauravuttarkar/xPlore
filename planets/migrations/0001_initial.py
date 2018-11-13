# Generated by Django 2.1.2 on 2018-11-12 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='exoPlanets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distanceFromEarth', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='planet',
            fields=[
                ('planetName', models.CharField(default=None, max_length=100, primary_key=True, serialize=False)),
                ('mass', models.CharField(default=None, max_length=100)),
                ('radius', models.CharField(default=None, max_length=100)),
                ('rotationPeriod', models.CharField(default=None, max_length=100)),
                ('star', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stars.star')),
            ],
        ),
        migrations.CreateModel(
            name='solarPlanets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meanDistanceFromSuninAU', models.CharField(default=None, max_length=100)),
                ('equatorialRadius', models.CharField(default=None, max_length=100)),
                ('surfaceArea', models.CharField(default=None, max_length=100)),
                ('volume', models.CharField(default=None, max_length=100)),
                ('density', models.CharField(default=None, max_length=100)),
                ('escapeVelocity', models.CharField(default=None, max_length=100)),
                ('orbitalPeriod', models.CharField(default=None, max_length=100)),
                ('temperature', models.CharField(default=None, max_length=100)),
                ('moons', models.CharField(default=None, max_length=100)),
                ('rings', models.CharField(default=None, max_length=100)),
                ('planetName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planets.planet')),
            ],
        ),
        migrations.AddField(
            model_name='exoplanets',
            name='planetName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planets.planet'),
        ),
    ]
