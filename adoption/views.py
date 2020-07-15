from django.shortcuts import render, redirect
from django.urls import reverse

from perfil.models import Perfil
from django.contrib.auth.models import User

from .models import Pet, Solicitud_Adopcion

from .forms import AdopcionForm


def adoption_list(request):
    '''list pets actives for adoption'''

    #pets_adoption = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    pets_adoption = Pet.objects.filter(estado_adopcion = 1)
    context = {
        'pets_adoption':pets_adoption
    }
    return render(request, 'adoption/adoption_list.html', context)



def adoption_detail(request, id):
    '''detail pet in adoption'''

    pet = Pet.objects.get(id=id)
    context = {
        'pet':pet
    }
    return render(request, 'adoption/adoption_detail.html', context)




def solicitud_adopcion(request, pet_id):
    '''solucitud de adopcion del peludo'''
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        print('ingresa a method = post')
        form = AdopcionForm(request.POST)
        if form.is_valid():
            print('form is valid')
            rut = form.cleaned_data['rut']
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            telefono_fijo = form.cleaned_data['telefono_fijo']
            telefono_celular = form.cleaned_data['telefono_celular']

            
            
            if not Perfil.objects.filter(rut=rut).exists():
                print('perfil no existe.... se crea uno nuevo')
                user = User.objects.create(username=email, password='password1234567890',email=email, first_name=nombres,last_name=apellidos)
                user.save()
                perfil = Perfil.objects.get(user=user)
                perfil.rut = rut 
                perfil.direccion = direccion
                perfil.fecha_nacimiento = fecha_nacimiento
                perfil.telefono_fijo = telefono_fijo
                perfil.telefono_movil = telefono_celular
                perfil.save()
                print('se crea el perfil con exito')
                solicitud = Solicitud_Adopcion.objects.create(pet=pet, perfil=perfil)
                solicitud.save()
                print('se crea la solicitud en la bd')
            else:
                print(f'el perfil de ya existe..')
                perfil = Perfil.objects.get(rut=rut)
                solicitud = Solicitud_Adopcion.objects.create(pet=pet, perfil=perfil)
                solicitud.save()
                print('solicitud creada')

                

            print(f'el peludo se llama {pet.nombre}')
            return redirect('adoption:gracias')


    else:
        form = AdopcionForm()

    return render(request, 'adoption/adopcion_form.html', {'form':form, 'pet':pet})




def gracias(request):
    pass
    return render(request,'adoption/adopcion_gracias.html')



def apadrinar(request,pet_id):
    '''apadrinar un peludo'''

    pet = Pet.objects.get(id=pet_id)
    plans = {
        'bronce':{
            'valor':20000,
            'beneficio':'Cubre un mes de comida para un perro',
            'tiempo':'mensual'
        },
        'silver':{
            'valor':40000,
            'beneficio':'Cubre un mes de comida e insumos veterinarios',
            'tiempo':'mensual'
        },
        'gold':{
            'valor':60000,
            'beneficio':'Cubre la alimentación, atención e insumos veterinarios',
            'tiempo':'mensual'
        },
        'platinum':{
            'valor':80000,
            'beneficio':'Cubre el gasto total en salud, refugio y alimentación de un perro',
            'tiempo':'mensual'
        }
    }        
            
    context = {
        'pet':pet,
        'plans':plans
    }
    return render(request,'adoption/apadrinar_detail.html',context)