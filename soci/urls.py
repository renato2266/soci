# urls.py dell'APP soci

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
 	    
