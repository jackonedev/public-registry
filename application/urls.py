from django.urls import path

from . import views


urlpatterns = [
    path('all/', views.person_list, name='person_list'),
]