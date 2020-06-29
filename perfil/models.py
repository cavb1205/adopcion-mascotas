from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver



class Tipo_Perfil(models.Model):
    '''tipo de perfil, si el suaurio es voluntario, socio, etc'''
    nombre_tipo_perfil = models.CharField(max_length=255)
    descripcion_tipo_perfil = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre_tipo_perfil


class Perfil(models.Model):
    '''perfil user model'''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=10,null=True)
    avatar = models.ImageField(upload_to='images/perfil/', blank=True)
    fecha_nacimiento = models.DateField(auto_now=False, blank=True,null=True)
    direccion = models.CharField(max_length=255, blank=True)
    telefono_fijo = models.CharField(max_length=20, blank=True)
    telefono_movil = models.CharField(max_length=20, blank=True)
    tipo_perfil = models.ForeignKey(Tipo_Perfil, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.user.username


    @receiver(post_save, sender=User)
    def crear_perfil(sender,instance,created,**kwargs):
        if created:
            perfil = Perfil.objects.create(user=instance)
            perfil.save()
        else:
            return 'Usuario ya fue creado'
        print('fin a la funcion crear perfil')






class Contacto(models.Model):
    '''formulario de contacto'''

    nombres = models.CharField(max_length=255)
    email = models.EmailField()
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    fecha_contacto = models.DateField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.asunto