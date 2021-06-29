from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from .models import Savoir

# Create your views here.

def home_function(request):
    """Render the Savoir page"""
    actus_list = Savoir.objects.all().order_by('-date')
    list_dispo = []
    list_pas_dispo = []
    print(actus_list)
    for actu_no in actus_list:
        if actu_no.disponible == True:
            list_dispo.append(actu_no)
            # dict_actus["dispo"] = actu_no
        else:
            list_pas_dispo.append(actu_no)
            # dict_actus["pas_dispo"] = actu_no
    context = {"actus_dispo" : list_dispo,"actus_pas_dispo" : list_pas_dispo} 
    return render(request,"index.html",context)

def connaitre_function(request):
    """Render the Connaitre page"""
    return render(request,"connaitre.html")

def suivre_function(request):
    """Render the Suivre page"""
    return render(request,"suivre.html")

def contact_function(request):
    """Render the Contact page"""
    return render(request,"contact.html")
