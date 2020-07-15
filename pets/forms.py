from django.forms import ModelForm
from perfil.models import Contacto, Maltrato


class ContactoForm(ModelForm):
    '''furmulario de contacto'''
    class Meta:
        model = Contacto
        fields = '__all__'


class MaltratoForm(ModelForm):
    '''furmulario de maltrato'''
    class Meta:
        model = Maltrato
        fields = '__all__'