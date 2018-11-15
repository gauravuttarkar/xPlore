"""SpaceX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from satellites import urls as satellites_urls
from planets import urls as planets_urls
from galaxy import urls as galaxy_urls
from stars import urls as stars_urls
from constellations import urls as constellations_urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('planets/',include(planets_urls)),
    path('galaxies/',include(galaxy_urls)),
    path('stars/',include(stars_urls)),
    path('satellites/',include(satellites_urls)),
    path('constellations/',include(constellations_urls)),
    path('video/',views.video)
]
