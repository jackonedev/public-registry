from django.urls import path

from . import views


urlpatterns = [
    path('all/', views.getPerson, name='person_list'),
]