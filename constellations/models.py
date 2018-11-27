from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class constellation(models.Model):

    constellationName = models.CharField(max_length=100, null=False,default=None,primary_key=True)
    origin =  models.CharField(max_length=200, null=True,default=None)
    meaning =  models.CharField(max_length=200, null=True,default=None)
    #brightestStar =  models.CharField(max_length=100, null=True,default=None)
