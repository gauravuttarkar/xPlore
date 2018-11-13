from django.shortcuts import render

from django.http import HttpResponse
from satellites.models import satellite, naturalSatellite, artificialSatellite


def index(request):
	print("Hitting satellites Page Successfull")
	satellites = satellite.objects.all()
	#print(galaxies)
	li = []
	a=''
	for i in satellites:
		di = {}
		#print(i.star)

		di['satelliteName'] = i.satelliteName
		di['orbitingBody'] = i.orbitingBody
		di['description'] = i.description

		li.append(di)
	print(li)	
	#return HttpResponse("Done and dusted")

	return render(request,'satellites/templates/satellites.html',{'satellites':li})


def satelliteFunction(request,satellite):
	print(satellite)
	print("Hitting satellite page Successfully")
	artificialsatellite = artificialSatellite.objects.get(satelliteName=satellite)
	print(str(artificialsatellite.satelliteName))
	print(artificialsatellite.origin)
	di = {}
	di['satelliteName'] = str(artificialsatellite.satelliteName)[str(artificialsatellite.satelliteName).find('(')+1:str(artificialsatellite.satelliteName).find(')')]
	di['origin'] = artificialsatellite.origin 
	di['users'] = artificialsatellite.users
	di['classOfOrbit'] = artificialsatellite.classOfOrbit
	di['typeOfOrbit'] = artificialsatellite.typeOfOrbit
	di['period'] = artificialsatellite.period
	di['dateOfLaunch'] =  artificialsatellite.dateOfLaunch
	di['launchSite'] =  artificialsatellite.launchSite
	di['launchVehicle'] =  artificialsatellite.launchVehicle


	return render(request,'satellites/templates/individualSatellite.html',{'satellite':di})

	# classOfOrbit = models.CharField(max_length=100, null=False,default=None) #7
	# typeOfOrbit = models.CharField(max_length=100, null=False,default=None) #8
	# period = models.CharField(max_length=100, null=False,default=None) #14
	# dateOfLaunch = models.CharField(max_length=100, null=False,default=None) #18
	# launchSite = models.CharField(max_length=100, null=False,default=None) #22
	# launchVehicle = models.CharField(max_length=100, null=False,default=None)