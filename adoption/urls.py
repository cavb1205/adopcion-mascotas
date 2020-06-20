from django.urls import path

from . import views

app_name = 'adoption'
urlpatterns = [
    path('', views.adoption_list, name='adopcion_list'),
    path('<int:id>/', views.adoption_detail, name = 'adopcion_detail'),
    #path('adoptados/', views.adoptados_list, name='adoptados_list'),
]
