from django.http import HttpResponse
from django.shortcuts import render
from . import templates

def index(request):
	print("Hitting Home Page Successfull")

	#return HttpResponse("Done and dusted")
	return render(request,'xPlore/templates/home.html')

def video(request):
	return render(request,'xPlore/templates/video.html')
