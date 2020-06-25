from django.urls import path

from . import views

app_name = 'perfil'
urlpatterns = [
    path('<int:id>/', views.detalle_perfil, name='detail'),
]
