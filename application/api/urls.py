from django.urls import path

from . import views

app_name = 'application'

urlpatterns = [
    path('all/', views.getAllPerson, name='all'),
    path('get/', views.getPerson, name='filter'),
    path('id/', views.getPersonById, name='id'),
]
