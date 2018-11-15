from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    # <a style="color:white" href='/stars/{{star.starName}}'>
    path('search',views.search),
    path('starsFromAConstellation/<str:constellation>',views.starsFromAConstellation),
    path('<str:star_name>',views.starFunction),
    
   
]
