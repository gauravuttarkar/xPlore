from django.shortcuts import render

from django.http import HttpResponse
from stars.models import star

def index(request):
	print("Hitting Stars Page Successfull")
	stars = star.objects.all()
	#print(galaxies)
	li = []

	for i in stars:
		print(i.starName,i.age,i.notes)
		
	print(li)	
	return HttpResponse("Done and dusted")
	#return render(request,'/templates/jumbotron.html',{'galaxies':li})
