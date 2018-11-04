from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class galaxy(models.Model):

    galaxyName = models.CharField(max_length=100, null=False,default=None)
    image = models.CharField(max_length=500, null=False,default=None)
    constellation = models.CharField(max_length=100, null=False,default=None)
    origin = models.CharField(max_length=3000, null=False,default=None)
    notes = models.CharField(max_length=3000, null=True,default=None)
    distance = models.DecimalField(max_digits=10,decimal_places=5, null=True,default=None)
