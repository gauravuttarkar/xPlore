from django.shortcuts import render, redirect
from stars.models import star
from constellations.models import constellation
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
	print("Hitting stars Page Successfull")
	stars = star.objects.all()

	li = []
	
	for i in stars:
		di = {}
		#print(i.star)
		di['starName'] = i.starName
		di['constellationName'] =str(i.constellationName)[str(i.constellationName).find('(')+1:str(i.constellationName).find(')')]
		di['rightAscension'] = i.rightAscension
		di['declination'] = i.declination
		di['apparentMagnitude'] = i.apparentMagnitude
		di['distance'] = i.distance
		di['mass'] = i.mass
		di['temperature'] = i.temperature
		di['age'] = i.age
		di['confirmedPlanets'] = i.confirmedPlanets
		di['notes'] = i.notes

		li.append(di)
	#print(li)	
	paginator = Paginator(li, 25)

	page = request.GET.get('page')
	stars= paginator.get_page(page)
	#return HttpResponse("Done and dusted")

	return render(request,'stars/templates/stars.html',{'stars':stars})


def starFunction(request,star_name):
	starObj = star.objects.get(starName=star_name) 
	print(starObj)
	i = starObj
	di={}
	di['starName'] = i.starName
	di['constellationName'] = str(i.constellationName)[str(i.constellationName).find('(')+1:str(i.constellationName).find(')')]
	di['rightAscension'] = i.rightAscension
	di['declination'] = i.declination
	di['apparentMagnitude'] = i.apparentMagnitude
	di['distance'] = i.distance
	di['mass'] = i.mass
	di['temperature'] = i.temperature
	di['age'] = i.age
	di['confirmedPlanets'] = i.confirmedPlanets
	di['notes'] = i.notes
	return render(request,'stars/templates/individualStar.html',{'star':di})
	#return HttpResponse("Done and dusted")



def starsFromAConstellation(request,constellation):
	print(constellation)	
	stars = star.objects.all().filter(constellationName=constellation)#select * from stars where constellationName=constellation
	li = []
	for i in stars:
		di = {}
		di['starName'] = i.starName
		di['constellationName'] = str(i.constellationName)[str(i.constellationName).find('(')+1:str(i.constellationName).find(')')]
		di['rightAscension'] = i.rightAscension
		di['declination'] = i.declination
		di['apparentMagnitude'] = i.apparentMagnitude
		di['distance'] = i.distance
		di['mass'] = i.mass
		di['temperature'] = i.temperature
		di['age'] = i.age
		di['confirmedPlanets'] = i.confirmedPlanets
		di['notes'] = i.notes
		li.append(di)
	print(li)	
	paginator = Paginator(li, 25)

	page = request.GET.get('page')
	stars= paginator.get_page(page)
	#return HttpResponse("Done and dusted")

	return render(request,'stars/templates/stars.html',{'stars':stars})	


	return HttpResponse("Done and dusted")

def search(request):
	print(request)
	search_query = request.GET.get('Search')
	star_results = star.objects.filter(starName__icontains=search_query)
	print(star_results)
	li=[]
	for i in star_results:
		di = {}
		#print(i.star)

		di['starName'] = i.starName
		di['constellationName'] = str(i.constellationName)[str(i.constellationName).find('(')+1:str(i.constellationName).find(')')]
		di['rightAscension'] = i.rightAscension
		di['declination'] = i.declination
		di['apparentMagnitude'] = i.apparentMagnitude
		di['distance'] = i.distance
		di['mass'] = i.mass
		di['temperature'] = i.temperature
		di['age'] = i.age
		di['confirmedPlanets'] = i.confirmedPlanets
		di['notes'] = i.notes

		li.append(di)
	print(li)	
	paginator = Paginator(li, 25)

	page = request.GET.get('page')
	stars= paginator.get_page(page)
	#return HttpResponse("Done and dusted")

	return render(request,'stars/templates/stars.html',{'stars':stars})	

def modify(request):
	print("Done")
	return render(request,'stars/templates/modify.html')

def modify_submit(request):

	starName = request.POST.get('starName')
	declination = request.POST.get('declination')

	constellationName = request.POST.get('constellationName')
	rightAscension = request.POST.get('rightAscension')
	notes = request.POST.get('notes')
	distance = request.POST.get('distance')
	confirmedPlanets = request.POST.get('confirmedPlanets')
	age = request.POST.get('age')
	temperature = request.POST.get('temperature')
	mass = request.POST.get('mass')
	apparentMagnitude = request.POST.get('apparentMagnitude')

	constellationName = constellation.objects.get(constellationName=constellationName)
	obj = star.objects.create(starName=starName,
										declination=declination,
										constellationName=constellationName,
										rightAscension=rightAscension,
										notes=notes,
										distance=distance,
										confirmedPlanets=confirmedPlanets,
										age=age,
										temperature=temperature,
										mass=mass,
										apparentMagnitude=apparentMagnitude)
	obj.save()

	return redirect("/stars")	

def delete(request):
	starName = request.POST.get('starName')
	obj = star.objects.get(starName=starName)
	obj.delete()

	return redirect("/stars")		