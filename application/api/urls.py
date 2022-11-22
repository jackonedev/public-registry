from django.urls import path

from . import views

app_name = 'api-rest'

urlpatterns = [
    path('person/1/', views.getAllPerson, name='all'),
    path('person/2/', views.getPerson, name='filter'),
    path('person/id/', views.getPersonById, name='id'),
    path('person/create/', views.createPerson, name='create'),
    path('person/<str:id>/edit/', views.updatePerson, name='edit'),
    path('person/<str:id>/delete/', views.deletePerson, name='delete'),
]
