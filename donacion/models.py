from django.db import models

# Create your models here.
class Tipo_Donacion(models.Model):
    '''tipo donacion, comida, dinero,etc'''
    nombre_tipo_donacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_tipo_donacion