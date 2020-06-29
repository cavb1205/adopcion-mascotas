from django.forms import ModelForm
from perfil.models import Contacto


class ContactoForm(ModelForm):
    '''furmulario de contacto'''
    class Meta:
        model = Contacto
        fields = '__all__'