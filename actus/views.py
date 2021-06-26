from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
# Create your views here.

def home_function(request):
    """Render the Savoir page"""
    return render(request,"index.html")

def connaitre_function(request):
    """Render the Connaitre page"""
    return render(request,"connaitre.html")
