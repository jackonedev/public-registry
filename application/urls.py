from django.urls import path

from . import views


app_name = 'application'

urlpatterns = [
    path('', views.app_home, name='home'),
    path('get/', views.get, name='get'),
    path('post/', views.post, name='post'),
    path('put/', views.id_form, name='put'),
    path('search/', views.id_form, name='search'),
    path('delete/', views.delete, name='delete-person'),
    path('update/', views.update, name='update-person'),
    path('person/download/', views.download, name='download'),
]