from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    path('search',views.search),
    path('modify_solar',views.modify_solar),
    path('modify_exo',views.modify_exo),
    path('modify_solar_submit',views.modify_solar_submit),
    path('modify_exo_submit',views.modify_exo_submit),
    path('delete_solar',views.delete_solar),
    path('delete_exo',views.delete_exo),
    path('planetsFromAStar/<str:starName>',views.planetsFromAStar),
    path('<str:planet>',views.planetFunction),
   
]
