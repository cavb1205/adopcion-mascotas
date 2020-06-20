from django.urls import path

from . import views

app_name = 'adoption'
urlpatterns = [
    path('', views.adoption_list, name='adopcion_list'),
    #path('adoptados/', views.adoptados_list, name='adoptados_list'),
]
