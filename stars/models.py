from django.db import models
from django.contrib.auth.models import User
from constellations.models import constellation
# Create your models here.
class star(models.Model):
	starName = models.CharField(max_length=100, null=False,default=None,primary_key=True)
	constellationName = models.ForeignKey(constellation,on_delete=models.CASCADE)
	rightAscension = models.CharField(max_length=100, null=True,default=None)
	declination = models.CharField(max_length=100, null=True,default=None)
	apparentMagnitude = models.CharField(max_length=100, null=True,default=None)
	distance = models.CharField(max_length=100, null=True,default=None)
	spectralType = models.CharField(max_length=100, null=True,default=None)
	mass = models.CharField(max_length=100, null=True,default=None)
	temperature = models.CharField(max_length=100, null=True,default=None)
	age = models.CharField(max_length=100, null=True,default=None)
	confirmedPlanets = models.CharField(max_length=100, null=True,default=None)
	notes = models.CharField(max_length=100, null=True,default=None)





