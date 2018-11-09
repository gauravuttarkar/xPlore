from django.shortcuts import render

from django.http import HttpResponse
from planets.models import planet

def index(request):
	print("Hitting Planets Page Successfull")
	planet1 = planet.objects.all()
	print(planet1)
	#print(planet1.planetName)
	#return HttpResponse("Done and dusted")
	return HttpResponse('Planets hit')