from django import forms
from django.contrib.auth.models import User

from perfil.models import Perfil



class AdopcionForm(forms.Form):
    '''formulario para postular la adopcion de un peludo'''
    
    rut = forms.CharField(label='Rut:', max_length=10)
    nombres = forms.CharField(label='Nombres:', max_length=100)
    apellidos = forms.CharField(label='Apellidos:', max_length=100)
    email = forms.EmailField(label='Email:')
    direccion = forms.CharField(label='Dirección de residencia:', max_length=255)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento:')
    telefono_fijo = forms.CharField(label='Telefono fijo', max_length=20)
    telefono_celular = forms.CharField(label='Telefono celular', max_length=20)
    

