from django.shortcuts import render, redirect
import mysql.connector
from django.http import HttpResponse
from galaxy.models import galaxy

def index(request):
	print("Hitting Galaxies Page Successfull")
	galaxies = galaxy.objects.all() #select * from galaxy;
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

def galaxyFunction(request,galaxy_name):
	galaxyObj = galaxy.objects.get(galaxyName=galaxy_name) # select * from galaxy where galaxyName = galaxy_name
	print(galaxyObj)
	i = galaxyObj
	#return HttpResponse("Done and dusted")
	di = {}  #Creates a dictionary
	di['galaxyName'] = i.galaxyName
	di['image'] = i.image
	di['origin'] = i.origin
	di['constellation'] = i.constellation
	di['notes'] = i.notes
	di['distance'] = i.distance


	return render(request,'galaxy/templates/individualGalaxy.html',{'galaxy':di})


def modify(request):
	print("Done")
	return render(request,'galaxy/templates/modify.html')

def modify_submit(request):

	galaxyName = request.POST.get('galaxyName')
	origin = request.POST.get('origin')
	constellation = request.POST.get('constellation')
	image = request.POST.get('image')
	notes = request.POST.get('notes')
	distance = request.POST.get('distance')

	obj = galaxy.objects.create(galaxyName=galaxyName,
										origin=origin,
										constellation=constellation,
										image=image,
										notes=notes,
										distance=distance)
	obj.save()

	return redirect("/galaxies")	

def delete(request):
	galaxyname = request.POST.get('galaxyName')
	obj = galaxy.objects.get(galaxyName=galaxyname)
	obj.delete()

	return redirect("/galaxies")	

def nearest(request):
	distance = request.POST.get("nearest")
	print(distance)
	distance = distance
	conn = mysql.connector.connect(user='gaurav', database='xplore', password='root123')

	cursor = conn.cursor()	
	print(cursor.execute("CALL nearestGalaxy(" + distance + ");"))
	li = cursor.fetchall()
	data = []
	for i in li:
		print(type(i))
		print(i)
		data.append(galaxy.objects.get(galaxyName=i[0]))

	print(data)
	li = []

	for i in data:
		di = {}
		di['galaxyName'] = i.galaxyName
		di['image'] = i.image
		di['origin'] = i.origin
		li.append(di)
	print(li)	
	#return HttpResponse("Done and dusted")
	return render(request,'galaxy/templates/jumbotron.html',{'galaxies':li})