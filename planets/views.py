from django.shortcuts import render

from django.http import HttpResponse
from planets.models import planet

def index(request):
	print("Hitting planets Page Successfull")
	planets = planet.objects.all()
	#print(galaxies)
	li = []
	a=''
	for i in planets:
		di = {}
		#print(i.star)

		di['planetName'] = i.planetName
		di['star'] = i.star
		if (i.mass.find(chr(9824)) > -1):
			di['mass']=i.mass[i.mass.find(chr(9824))+1:]
		else:
			di['mass'] = i.mass
		if (i.radius.find(chr(9824)) > -1):
			di['radius']=i.radius[i.radius.find(chr(9824))+1:]
		else:
			di['radius'] = i.radius
		if (i.rotationPeriod.find(chr(9824)) > -1):	
			di['rotationPeriod']=i.rotationPeriod[i.rotationPeriod.find(chr(9824))+1:]
		else:
			di['rotationPeriod'] = i.rotationPeriod

		li.append(di)
	#print(li)	
	#return HttpResponse("Done and dusted")
	print(type(a))
	print('sdfs'.find(chr(9824)))
	for i in a:
		print(i,ord(i))
	return render(request,'planets/templates/planets.html',{'planets':li})

