from django.shortcuts import render, redirect

from perfil.models import Perfil
from django.contrib.auth.models import User

from .forms import InscripcionVoluntarioForm

from voluntario.models import Actividades_Voluntario, Solicitud_Voluntario

# Create your views here.
def home(request):
    '''home page voluntario info'''

    return render(request,'voluntarios/voluntario_home.html')



def solicitud_voluntariado(request):
    '''tramitar la solicitud de voluntariado'''

    if request.method == 'POST':

        form = InscripcionVoluntarioForm(request.POST)
        print('se crea el form de post')
        if form.is_valid():
            print('formulario es valido')
            rut = form.cleaned_data['rut']
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            telefono_fijo = form.cleaned_data['telefono_fijo']
            telefono_celular = form.cleaned_data['telefono_celular']
            casa_temporal = form.cleaned_data['casa_temporal']
            donaciones = form.cleaned_data['donaciones']
            eventos = form.cleaned_data['eventos']
            otras_actividades = form.cleaned_data['otras_actividades']
            experiencia = form.cleaned_data['experiencia']
            extra = form.cleaned_data['extra']

            if not Perfil.objects.filter(rut=rut): #no existe perfil
                user = User.objects.create(username=email,first_name=nombres, last_name=apellidos, email=email)
                user.save()
                print('usuario creado')
                perfil = Perfil.objects.get(user=user)
                perfil.rut = rut
                perfil.direccion = direccion
                perfil.fecha_nacimiento = fecha_nacimiento
                perfil.telefono_fijo = telefono_fijo
                perfil.telefono_movil = telefono_celular
                perfil.save()
                print('guardamos el perfil con los nuevos datos')
                #asigno las actividades al perfil
                actividades = Actividades_Voluntario.objects.create(perfil=perfil,experiencia=experiencia, extra=extra)
                actividades.save()
                print('actividades creadas OK')
                
                for item in casa_temporal:
                    actividades.casa_temporal.add(item)
                
                for item in donaciones:
                    actividades.donaciones.add(item)

                for item in eventos:
                    actividades.eventos.add(item)

                for item in otras_actividades:
                    actividades.otras_actividades.add(item)
                
                actividades.save()
                
                #creamos la soplicitud_voluntariado
                solicitud = Solicitud_Voluntario.objects.create(perfil=perfil, actividades=actividades)
                return redirect('/gracias/')

            else:
                print('perfil ya existe') #perfil existe
                perfil = Perfil.objects.get(rut=rut)
                actividades = Actividades_Voluntario.objects.create(perfil=perfil,experiencia=experiencia, extra=extra)
                print('actividades creadas OK')
                for item in casa_temporal:
                    actividades.casa_temporal.add(item)
                
                for item in donaciones:
                    actividades.donaciones.add(item)

                for item in eventos:
                    actividades.eventos.add(item)

                for item in otras_actividades:
                    actividades.otras_actividades.add(item)
                
                actividades.save()
                print('items actividades agregados')
                #creamos la soplicitud_voluntariado
                solicitud = Solicitud_Voluntario.objects.create(perfil=perfil, actividades=actividades)
                print('solicitud creada con exito')

                return redirect('/gracias/')

    else:

        form = InscripcionVoluntarioForm()

    return render(request,'voluntarios/voluntario_form.html',{'form':form})
