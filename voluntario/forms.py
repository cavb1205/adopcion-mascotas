from django import forms
from voluntario.models import Casa_Temporal, Otras_actividades
from donacion.models import Tipo_Donacion
from evento.models import Tipo_Evento



class InscripcionVoluntarioForm(forms.Form):
    '''formulario para solicitudes de inscripcion de voluntarios'''

    rut = forms.CharField(label='Rut:', max_length=10)
    nombres = forms.CharField(label='Nombres:', max_length=100)
    apellidos = forms.CharField(label='Apellidos:', max_length=100)
    email = forms.EmailField(label='Email:')
    direccion = forms.CharField(label='Dirección de residencia:', max_length=255)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento:')
    telefono_fijo = forms.CharField(label='Telefono fijo', max_length=20)
    telefono_celular = forms.CharField(label='Telefono celular', max_length=20)
    ##obciones de voluntariado
    casa_temporal = forms.ModelMultipleChoiceField(queryset=Casa_Temporal.objects.all())
    donaciones = forms.ModelMultipleChoiceField(queryset=Tipo_Donacion.objects.all())
    eventos = forms.ModelMultipleChoiceField(queryset=Tipo_Evento.objects.all())
    otras_actividades = forms.ModelMultipleChoiceField(queryset=Otras_actividades.objects.all())
    experiencia = forms.CharField()
    extra = forms.CharField()
