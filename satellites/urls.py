from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    path('search',views.search),
    path('<str:satellite>',views.satelliteFunction),

   
]
