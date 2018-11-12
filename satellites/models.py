from django.db import models
from django.contrib.auth.models import User
from planets.models import planet

class satellite(models.Model):
	satelliteName = models.CharField(max_length=100, null=False,default=None,primary_key=True)
	orbitingBody = models.ForeignKey(planet,on_delete=models.CASCADE,default='')
	description = models.CharField(max_length=100, null=True,default='')

class artificialSatellite(models.Model):
	satelliteName = models.ForeignKey(satellite,on_delete=models.CASCADE)
	origin = models.CharField(max_length=100, null=False,default=None) #3
	users = models.CharField(max_length=100, null=False,default=None) #4
	#purpose = models.CharField(max_length=100, null=False,default=None) #5
	classOfOrbit = models.CharField(max_length=100, null=False,default=None) #7
	typeOfOrbit = models.CharField(max_length=100, null=False,default=None) #8
	period = models.CharField(max_length=100, null=False,default=None) #14
	dateOfLaunch = models.CharField(max_length=100, null=False,default=None) #18
	launchSite = models.CharField(max_length=100, null=False,default=None) #22
	launchVehicle = models.CharField(max_length=100, null=False,default=None) #23


class naturalSatellite(models.Model):
	satelliteName = models.ForeignKey(satellite,on_delete=models.CASCADE)
	image = models.CharField(max_length=300, null=False,default=None)
	discoveredBy = models.CharField(max_length=100, null=False,default=None)
	discoveredIn = models.CharField(max_length=100, null=False,default=None)
	meanRadius = models.CharField(max_length=200, null=False,default=None)




