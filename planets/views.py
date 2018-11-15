from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from planets.models import planet, solarPlanets, exoPlanets

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
		di['star'] = str(i.star)[str(i.star).find('(')+1:str(i.star).find(')')]
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
	paginator = Paginator(li, 25)

	page = request.GET.get('page')
	planets= paginator.get_page(page)
	return render(request,'planets/templates/planets.html',{'planets':planets})


def planetsFromAStar(request,starName):
		
	planets = planet.objects.all().filter(star=starName)
	li = []
	for i in planets:
		di = {}
		#print(i.star)

		di['planetName'] = i.planetName
		di['star'] = str(i.star)[str(i.star).find('(')+1:str(i.star).find(')')]
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
		
	print(li)	
	paginator = Paginator(li, 25)

	page = request.GET.get('page')
	planets= paginator.get_page(page)
	#return HttpResponse("Done and dusted")

	return render(request,'planets/templates/planets.html',{'planets':planets})

def search(request):
	print(request)
	search_query = request.GET.get('Search')
	planet_results = planet.objects.filter(planetName__icontains=search_query)
	print(planet_results)
	li=[]
	for i in planet_results:
		di = {}
		#print(i.star)

		di['planetName'] = i.planetName
		di['star'] = str(i.star)[str(i.star).find('(')+1:str(i.star).find(')')]
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
	print(li)	
	paginator = Paginator(li, 25)

	page = request.GET.get('page')
	planets= paginator.get_page(page)
	return render(request,'planets/templates/planets.html',{'planets':planets})


def planetFunction(request,planet):
	exoplanets = None
	solarplanets = None

	try:
		exoplanets = exoPlanets.objects.get(planetName=planet)
	except:
		solarplanets = solarPlanets.objects.get(planetName=planet)

	if exoplanets:
		print(str(exoplanets.planetName))
	
		di = {}
		di['planetName'] = str(exoplanets.planetName)[str(exoplanets.planetName).find('(')+1:str(exoplanets.planetName).find(')')]
		di['distanceFromEarth'] = exoplanets.distanceFromEarth 
		di['flag'] = 1
	if solarplanets:	
		di = {}
		di['planetName'] = str(solarplanets.planetName)[str(solarplanets.planetName).find('(')+1:str(solarplanets.planetName).find(')')]
		di['meanDistanceFromSuninAU'] = solarplanets.meanDistanceFromSuninAU 
		di['equatorialRadius'] = solarplanets.equatorialRadius
		di['surfaceArea'] = solarplanets.surfaceArea
		di['volume'] = solarplanets.volume
		di['density'] = solarplanets.density
		di['escapeVelocity'] = solarplanets.escapeVelocity
		di['orbitalPeriod'] = solarplanets.orbitalPeriod
		di['temperature'] = solarplanets.temperature
		di['moons'] = solarplanets.volume
		di['rings'] = solarplanets.rings
		di['flag'] = 0


	return render(request,'planets/templates/individualPlanet.html',{'planet':di})

	#return HttpResponse("Done and dusted")