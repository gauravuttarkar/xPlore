from django.shortcuts import render

from django.http import HttpResponse
from constellations.models import constellation

def index(request):
	print("Hitting Galaxies Page Successfull")
	constellations = constellation.objects.all()
	#print(galaxies)
	li = []

	for i in constellations:
		di = {}
		di['constellationName'] = i.constellationName
		di['meaning'] = i.meaning
		di['origin'] = i.origin
		di['brightestStar'] = i.brightestStar
		li.append(di)
	print(li)	
	#return HttpResponse("Done and dusted")
	return render(request,'constellations/templates/constellations.html',{'constellations':li})

