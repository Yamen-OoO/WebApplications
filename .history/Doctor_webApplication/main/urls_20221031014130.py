from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.text, name = 'text'),
]
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE
#! MAPPING IS NOT DONE YET.. DO NOT TOUCH THIS FILE