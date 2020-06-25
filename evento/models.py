from django.db import models

# Create your models here.
class Tipo_Evento(models.Model):
    '''tipo evento: rifas, peticiones comercios etc'''
    nombre_tipo_evento = models.CharField(max_length=255)


    def __str__(self):
        return self.nombre_tipo_evento