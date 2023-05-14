"""presalesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import index
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='Home'),
    path('rates/', include('rates.urls')),
    path('design/', include('design.urls')),
    path('examination/', include('examination.urls')),
    path('poc/', include('poc.urls')),
    path('output/', include('output.urls')),
    path('registration/', include('registration.urls')),  
    path('install/', include('install.urls')), 
    path('commissioning/', include('commissioning.urls')), 
    path('accept/', include('accept.urls')), 
    path('', LoginView.as_view(), name='login'),

]
