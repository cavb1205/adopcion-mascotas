from django.db import models

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
    esterilizado = models.BooleanField(default=0)

    

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


class Pet(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la Mascota')
    edad = models.IntegerField(help_text='Meses')
    historia = models.TextField()
    imagen_destacada = models.ImageField(upload_to='images/adoption/')
    imagen1 = models.ImageField(upload_to='images/adoption/',blank=True,null=True)
    imagen2 = models.ImageField(upload_to='images/adoption/',blank=True,null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    tipo_pet = models.ForeignKey(Tipo_Pet, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    esterilizado = models.ForeignKey(Esterilizado, on_delete=models.CASCADE)
    tamano = models.ForeignKey(Tamano, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    estado_adopcion = models.ForeignKey(Estado_Adopcion, on_delete=models.CASCADE)
    #usuario = models.ForeignKey(User,null=True,blank=True)
    usuario = usuarios[0]

    def __str__(self):
        return self.nombre