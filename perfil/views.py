from django.shortcuts import render

from .models import *

# Create your views here.

def detalle_perfil(request, id):
    '''muestra el perfil completo del usuario'''
    perfil = Perfil.objects.get(id=id)
   
    return render(request,'perfil/perfil_detail.html',{'perfil':perfil})