from django.db import models

from django.contrib.auth.models import User
from perfil.models import Perfil



usuarios = ['camilo','kevin','paola','german']


class Tipo_Pet(models.Model):
    '''type pet if: cat or dog'''

    tipo_pet = models.CharField(max_length=200) 

    def __str__(self):
        return self.tipo_pet


class Sexo(models.Model):
    """pet sex"""
    sexo = models.CharField(max_length=100)

    def __str__(self):
        return self.sexo
    

class Raza(models.Model):
    '''pet raza'''
    raza = models.CharField(max_length=100)
    
    def __str__(self):
        return self.raza

class Color(models.Model):
    '''pet color'''
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Esterilizado(models.Model):
    '''pet esterilization 1=si 0=no'''
    esterilizado = models.CharField(max_length=2)

    def __str__(self):
        return self.esterilizado

class Tamano(models.Model):
    '''pet size'''

    tamano = models.CharField(max_length=50)

    def __str__(self):
        return self.tamano


class Estado_Adopcion(models.Model):
    '''pet status ej: Adopted, in adoption'''

    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado

class Ubicacion(models.Model):
    '''pet ubication'''

    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.ubicacion

class Vacuna(models.Model):
    '''vacuna pet'''
    vacuna = models.CharField(max_length=50)
    

    def __str__(self):
        return self.vacuna

class Desparasitado(models.Model):
    
    desparasitado = models.CharField(max_length=50)
    

    def __str__(self):
        return self.desparasitado


class Salud(models.Model):

    estado_salud = models.CharField(max_length=100)
    

    def __str__(self):
        return self.estado_salud

class Cuidados(models.Model):

    nombre_cuidado = models.CharField(max_length=255)
    descripcion_cuidado = models.TextField()

    def __str__(self):
        return self.nombre_cuidado

class Pet(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la Mascota')
    edad = models.IntegerField(help_text='Meses')
    historia = models.TextField()
    imagen_destacada = models.ImageField(upload_to='images/adoption/')
    imagen1 = models.ImageField(upload_to='images/adoption/',blank=True,null=True)
    imagen2 = models.ImageField(upload_to='images/adoption/',blank=True,null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    tipo_pet = models.ForeignKey(Tipo_Pet, on_delete=models.CASCADE)
    tamano = models.ForeignKey(Tamano, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    esterilizado = models.ForeignKey(Esterilizado, on_delete=models.CASCADE)
    vacunado = models.ForeignKey(Vacuna, on_delete=models.CASCADE, null=True)
    desparasitado = models.ForeignKey(Desparasitado, on_delete=models.CASCADE, null=True)
    chip = models.CharField(max_length=10, null=True,blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    estado_adopcion = models.ForeignKey(Estado_Adopcion, on_delete=models.CASCADE, null=True)
    estado_salud = models.ForeignKey(Salud, on_delete=models.Model, null=True)
    cuidados_especiales = models.ForeignKey(Cuidados, on_delete=models.Model, null=True)
    #usuario = models.ForeignKey(User,null=True,blank=True)
    usuario = usuarios[0]

    def __str__(self):
        return self.nombre




class Solicitud_Adopcion(models.Model):
    '''solicitudes de adopcion enviadas por el formulario'''

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado_solicitud = models.BooleanField(blank=True, default=False)
    comentarios_solicitud = models.TextField(blank=True)

    def __str__(self):
        return self.fecha_solicitud