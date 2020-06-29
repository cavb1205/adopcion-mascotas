from django.shortcuts import render, redirect
from perfil.models import Contacto
from .forms import *



def home(request):
    '''home page'''
    return render(request,'home.html')



def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            print('ingresa a for is valid')
            nombres = form.cleaned_data['nombres']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            registro = Contacto.objects.create(nombres= nombres, email=email, asunto=asunto,mensaje=mensaje)
            registro.save()
            return redirect('/gracias/')
    else:
        form = ContactoForm()
    return render(request,'contacto.html',{'form':form})
        

def gracias(request):
    '''gracias general'''
    return render(request,'gracias.html')