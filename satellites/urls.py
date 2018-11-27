from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    path('search',views.search),
    path('modify_natural',views.modify_natural),
    path('modify_artificial',views.modify_artificial),
    path('modify_natural_submit',views.modify_natural_submit),
    path('modify_artificial_submit',views.modify_artificial_submit),
    path('delete_natural',views.delete_natural),
    path('delete_artificial',views.delete_artificial),
    path('<str:satellite>',views.satelliteFunction),

   
]
