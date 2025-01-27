"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.db import connection
from django.shortcuts import render
from . import views

 


# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('actors/', views.actors_list),
    path('login/',views.login),
    path('stud_list/',views.name),
    path('stud_details/',views.stud_details),
    # Corrected function reference
]
