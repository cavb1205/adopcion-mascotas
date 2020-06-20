from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Pet,Sexo,Ubicacion,Estado_Adopcion,Tamano,Esterilizado,Color,Raza,Tipo_Pet)
class PetAdmin(admin.ModelAdmin):
    pass