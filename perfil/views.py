from django.shortcuts import render

from voluntario.models import Actividades_Voluntario

from .models import *

# Create your views here.

def detalle_perfil(request, id):
    '''muestra el perfil completo del usuario'''
    perfil = Perfil.objects.get(id=id)
    actividades = Actividades_Voluntario.objects.get(perfil=perfil)
    casa_temporal_list = actividades.casa_temporal.all()
    donaciones_list = actividades.donaciones.all()
    eventos_list = actividades.eventos.all()
   
    context = {
        'perfil':perfil,
        'actividades':actividades,
        'casa_temporal_list':casa_temporal_list,
        'donaciones_list': donaciones_list,
        'eventos_list': eventos_list,


    } 
    return render(request,'perfil/perfil_detail.html',context)