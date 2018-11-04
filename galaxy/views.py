from django.shortcuts import render

from django.http import HttpResponse
from galaxy.models import galaxy

def index(request):
	print("Hitting Galaxies Page Successfull")
	galaxies = galaxy.objects.all()
	print(galaxies)
	li = []

	for i in galaxies:
		di = {}
		di['galaxyName'] = i.galaxyName
		di['image'] = i.image
		di['origin'] = i.origin
		li.append(di)
	print(li)	
	#return HttpResponse("Done and dusted")
	return render(request,'galaxy/templates/jumbotron.html',{'galaxies':li})

