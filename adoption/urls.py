from django.urls import path

from . import views

app_name = 'adoption'
urlpatterns = [
    path('', views.adoption_list, name='adopcion_list'),
    path('<int:id>/', views.adoption_detail, name = 'adopcion_detail'),
    path('solicitud/<int:pet_id>/', views.solicitud_adopcion, name = 'solicitud_adopcion'),
    path('gracias-por-adoptar/', views.gracias, name='gracias'),
    path('apadrinar/<int:pet_id>/', views.apadrinar, name='apadrinar'),
]
