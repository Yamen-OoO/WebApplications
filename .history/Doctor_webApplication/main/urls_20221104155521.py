from django.urls import include, path

from . import views
urlpatterns = [
    path('', views.index, name = 'index'),    
    path('main/', views.main, name = 'main'),
    path()
]
#! mostly done here!