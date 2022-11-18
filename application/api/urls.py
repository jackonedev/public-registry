from django.urls import path

from . import views

app_name = 'application'

urlpatterns = [
    path('person/', views.getAllPerson, name='all'),
    path('get/person/', views.getPerson, name='filter'),
    path('get/person/id/', views.getPersonById, name='id'),
]
