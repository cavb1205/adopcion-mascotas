from django.contrib import admin
from django.urls import path, include
from django.conf import settings




from . import views

app_name = 'voluntario'
urlpatterns = [
    path('', views.home, name='home'),
    path('solicitud/', views.solicitud_voluntariado, name='solicitud_voluntariado'),
    
] 

 