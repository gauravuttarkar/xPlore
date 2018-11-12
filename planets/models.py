from django.db import models
from django.contrib.auth.models import User
from stars.models import star

# Create your models here.
class planet(models.Model):

	planetName = models.CharField(max_length=100, null=False,default=None,primary_key=True)
	#planetType = models.CharField(max_length=100,null=False, default= None)
	star = models.ForeignKey(star,on_delete=models.CASCADE,default='')
	mass = models.CharField(max_length=100,null=False, default= None)
	radius = models.CharField(max_length=100,null=False,default=None)
	rotationPeriod = models.CharField(max_length=100,null=False, default= None)

class solarPlanets(models.Model):
	planetName = models.ForeignKey(planet,on_delete=models.CASCADE) 
	meanDistanceFromSuninAU = models.CharField(max_length=100,null=False, default= None)
	equatorialRadius = models.CharField(max_length=100,null=False, default= None)
	surfaceArea = models.CharField(max_length=100,null=False, default= None)    
	volume = models.CharField(max_length=100,null=False, default= None)
	density = models.CharField(max_length=100,null=False, default= None)
	escapeVelocity = models.CharField(max_length=100,null=False, default= None)
	orbitalPeriod = models.CharField(max_length=100,null=False, default= None)
	temperature = models.CharField(max_length=100,null=False, default= None)
	moons = models.CharField(max_length=100,null=False, default= None)
	rings = models.CharField(max_length=100,null=False, default= None)
	


class exoPlanets(models.Model):
	planetName = models.ForeignKey(planet,on_delete=models.CASCADE) 
	distanceFromEarth = models.CharField(max_length=100,null=False, default= None)
	


    	