from django.shortcuts import render

from voluntario.models import Actividades_Voluntario

# Create your views here.
def home(request):
    '''home page voluntario info'''

    return render(request,'voluntarios/voluntario_home.html')


#def actividades_voluntariado_detalle(request, perfil_id):
 #   '''get detail voluntaring for user'''

#    actividades = Actividades_Voluntario.objects.get(perfil=perfil_id)
    
 #   return render(request, '')