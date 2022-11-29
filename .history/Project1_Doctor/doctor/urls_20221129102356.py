"""doctor URL Configuration

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
from django.urls import path
from django.urls import re_path, include
from django.contrib import admin
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('main/', include('main.urls')),    
    #! testing url mappgin again to get it working
    #! debugging mode!
    path('index.html', include('main.urls')),
    path('login', include('main.urls')),
]
