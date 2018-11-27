from django.shortcuts import render, redirect

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
		#di['brightestStar'] = i.brightestStar
		li.append(di)
	print(li)	
	#return HttpResponse("Done and dusted")
	return render(request,'constellations/templates/constellations.html',{'constellations':li})

def modify(request):
	return render(request,'constellations/templates/modify.html')

def modify_submit(request):
	constellationName = request.POST.get('constellationName')
	origin = request.POST.get('origin')
	meaning = request.POST.get('meaning')
	obj = constellation.objects.create(constellationName=constellationName,origin=origin,meaning=meaning)
	obj.save()

	return redirect("/constellations")	

def delete(request):
	constellationName = request.POST.get('constellationName')
	obj = constellation.objects.get(constellationName=constellationName)
	obj.delete()

	return redirect("/constellations")	