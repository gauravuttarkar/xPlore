from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	print("Hitting Satellites Page Successfull")


	return HttpResponse("Done and dusted")