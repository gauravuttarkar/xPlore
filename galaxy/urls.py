from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    path('modify',views.modify),
    path('modify_submit',views.modify_submit),
    path('delete',views.delete),
    path('<str:galaxy_name>',views.galaxyFunction),

   
]
