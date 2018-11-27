from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from satellites.models import satellite, naturalSatellite, artificialSatellite
from planets.models import planet

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
	#print(li)	
	paginator = Paginator(li, 25)

	page = request.GET.get('page')
	satellites= paginator.get_page(page)
	#return HttpResponse("Done and dusted")

	return render(request,'satellites/templates/satellites.html',{'satellites':satellites})


def satelliteFunction(request,satellite):
	print(satellite)

	print("Hitting satellite page Successfully")
	artificialsatellite = None
	naturalsatellite = None

	try:
		artificialsatellite = artificialSatellite.objects.get(satelliteName=satellite)
	except:
		naturalsatellite = naturalSatellite.objects.get(satelliteName=satellite)

	if artificialsatellite:
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
		di['flag'] = 1
	if naturalsatellite:
		di = {}
		di['satelliteName'] = str(naturalsatellite.satelliteName)[str(naturalsatellite.satelliteName).find('(')+1:str(naturalsatellite.satelliteName).find(')')]
		di['image'] = naturalsatellite.image 
		di['discoveredBy'] = naturalsatellite.discoveredBy
		di['discoveredIn'] = naturalsatellite.discoveredIn
		di['meanRadius'] = naturalsatellite.meanRadius
		di['flag'] = 0


	return render(request,'satellites/templates/individualSatellite.html',{'satellite':di})
		

def search(request):
	print(request)
	search_query = request.GET.get('Search')
	satellite_results = satellite.objects.filter(satelliteName__icontains=search_query)
	print(satellite_results)
	li=[]
	for i in satellite_results:
		di = {}
		#print(i.star)

		di['satelliteName'] = i.satelliteName
		di['orbitingBody'] = i.orbitingBody
		di['description'] = i.description

		li.append(di)
	print(li)	
	paginator = Paginator(li, 25)

	page = request.GET.get('page')
	satellites= paginator.get_page(page)
	#return HttpResponse("Done and dusted")

	return render(request,'satellites/templates/satellites.html',{'satellites':satellites})



def modify_natural(request):
	print("Done")
	return render(request,'satellites/templates/modify_natural.html')

def modify_natural_submit(request):


	satelliteName = request.POST.get('satelliteName')
	orbitingBody = request.POST.get('orbitingBody')
	image = request.POST.get('image')
	discoveredBy = request.POST.get('discoveredBy')
	discoveredIn = request.POST.get('discoveredIn')
	meanRadius = request.POST.get('meanRadius')

	orbitingBody = planet.objects.get(planetName=orbitingBody)

	obj = satellite.objects.create(satelliteName=satelliteName,
										orbitingBody=orbitingBody)

	obj.save()
	
	obj = naturalSatellite.objects.create(satelliteName=obj,
											image=image,
											discoveredBy=discoveredBy,
											discoveredIn=discoveredIn,
											meanRadius=meanRadius
											)

	obj.save()



	return redirect("/satellites")	

def delete_natural(request):
	satelliteName = request.POST.get('satelliteName')

	obj = naturalSatellite.objects.get(satelliteName=satelliteName)
	obj.delete()

	obj = satellite.objects.get(satelliteName=satelliteName)
	obj.delete()


	return redirect("/satellites")	

def modify_artificial(request):
	print("Done")
	return render(request,'satellites/templates/modify_artificial.html')

def modify_artificial_submit(request):

	
	satelliteName = request.POST.get('satelliteName')
	orbitingBody = request.POST.get('orbitingBody')
	dateOfLaunch = request.POST.get('dateOfLaunch')
	launchSite = request.POST.get('launchSite')
	launchVehicle = request.POST.get('launchVehicle')

	orbitingBody = planet.objects.get(planetName=orbitingBody)

	obj = satellite.objects.create(satelliteName=satelliteName,
										orbitingBody=orbitingBody)

	obj.save()
	
	obj = artificialSatellite.objects.create(satelliteName=obj,
											dateOfLaunch=dateOfLaunch,
											launchSite=launchSite,
											launchVehicle=launchVehicle,
											)

	obj.save()



	return redirect("/satellites")	


def delete_artificial(request):
	satelliteName = request.POST.get('satelliteName')
	print(satelliteName)
	obj = artificialSatellite.objects.get(satelliteName=satelliteName)
	obj.delete()

	obj = satellite.objects.get(satelliteName=satelliteName)
	obj.delete()

	return redirect("/satellites")	