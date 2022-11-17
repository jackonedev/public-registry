from django.urls import path

from . import views


urlpatterns = [
    path('all/', views.getAllPerson, name='get_person_list'),
    path('get/', views.getPerson, name='get_person_filter'),
    path('id/', views.getPersonById, name='get_person_id'),
]