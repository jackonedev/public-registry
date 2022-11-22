from django.urls import path

from . import views


app_name = 'application'

urlpatterns = [
    path('', views.app_home, name='home'),
    path('get/', views.get, name='get'),
    path('post/', views.post, name='post'),
    path('person/download/', views.download, name='download'),
]