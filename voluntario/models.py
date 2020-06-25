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



class Actividades_Voluntario(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
    casa_temporal = models.ManyToManyField(Casa_Temporal,blank=True)
    donaciones = models.ManyToManyField(Tipo_Donacion,blank=True)
    eventos = models.ManyToManyField(Tipo_Evento, blank=True)
    rescates = models.BooleanField(verbose_name='Rescates', default=False)
    vehiculo = models.BooleanField(verbose_name='Vehículo', default=False)
    capacitacion = models.BooleanField(verbose_name='Capacitaciones, Charlas', default=False)
    representacion_medios = models.BooleanField(verbose_name='Representación Medios', default=False)
    cuidados_veterinarios = models.BooleanField(verbose_name='Cuidados Veterinarios', default=False)
    legal = models.BooleanField(verbose_name='Legal(escritos, trámites, denuncias)', default=False)
    experiencia = models.TextField(verbose_name='Experiencia',blank=True)
    extra = models.CharField(max_length=255, blank=True)
   
    def __str__(self):
        return self.perfil.user.username