from django.urls import path

from . import views


app_name = 'application'

urlpatterns = [
    path('get/', views.get, name='get'),
    path('post/', views.post, name='post'),
]