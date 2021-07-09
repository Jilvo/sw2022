from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib import messages

from .models import Actusuivre, Savoir, Agendasuivre, Newsletter_model

# Create your views here.


def home_function(request):
    """Render the Savoir page"""
    actus_list = Savoir.objects.all().order_by("-created_at")
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
    context = {"actus_dispo": list_dispo, "actus_pas_dispo": list_pas_dispo}
    return render(request, "index.html", context)


def connaitre_function(request):
    """Render the Connaitre page"""
    return render(request, "connaitre.html")


def suivre_function(request):
    """Render the Suivre page"""
    actu_suivre = Actusuivre.objects.all().order_by("-created_at")
    agenda_suivre = Agendasuivre.objects.all().order_by("-created_at")
    context = {"actu_suivre": actu_suivre, "agenda_suivre": agenda_suivre}
    print(context)
    return render(request, "suivre.html", context)


def legals_mentions(request):
    """Render the Mentions Legales page"""
    return render(request, "legals_mentions.html")


def join_newsletter(request):
    query = request.GET.get("email")
    print(query)
    
    new_reader = Newsletter_model.objects.create(email=query)
    # new_reader.save()
    print(new_reader)
    messages.success(request, "Vous êtes bien inscrit à notre lettre d'information")
    return render(request, "suivre.html")
    # return HttpResponseRedirect(request.path_info)
    # return HttpResponse("Merci de vous être inscrit à la newsletter")
