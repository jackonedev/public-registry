from django.urls import path

from . import views


urlpatterns = [
    path('all/', views.getAllPerson, name='person_list'),
    path('get/', views.getPerson, name='person_list'),
]