from django.shortcuts import render

# Create your views here.
def home(request):
    '''home page voluntario info'''

    return render(request,'voluntarios/voluntario_home.html')