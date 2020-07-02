from django.db import models

from perfil.models import Perfil
from adoption.models import Tipo_Pet
from donacion.models import Tipo_Donacion
from evento.models import Tipo_Evento

# Create your models here.

class Casa_Temporal(Tipo_Pet):
    '''tipo mascota que puede acoger'''
    class Meta:
        proxy = True

class Otras_actividades(models.Model):
    '''otras actividades que se pueda colavorar'''

    nombre_actividad = models.CharField(max_length=255)
    descripcion_actividad = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_actividad


class Actividades_Voluntario(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
    casa_temporal = models.ManyToManyField(Casa_Temporal,blank=True)
    donaciones = models.ManyToManyField(Tipo_Donacion,blank=True)
    eventos = models.ManyToManyField(Tipo_Evento, blank=True)
    otras_actividades = models.ManyToManyField(Otras_actividades, blank=True)
    experiencia = models.TextField(verbose_name='Experiencia',blank=True)
    extra = models.TextField(verbose_name='Sugerencia',blank=True)
   
    def __str__(self):
        return self.perfil.user.username




class Solicitud_Voluntario(models.Model):
    '''solicitudes para ser voluntario'''

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    actividades = models.ForeignKey(Actividades_Voluntario, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add=True)

    