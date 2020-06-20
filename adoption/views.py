from django.shortcuts import render
from .models import Pet


def adoption_list(request):
    '''list pets actives for adoption'''

    #pets_adoption = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    pets_adoption = Pet.objects.filter(estado_adopcion = 1)
    context = {
        'pets_adoption':pets_adoption
    }
    return render(request, 'adoption/adoption_list.html', context)

