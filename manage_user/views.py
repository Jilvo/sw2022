from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import check_password
from .forms import ConnexionForm, RegistrationForm
# Create your views here.

def contact_function(request):
    """Render the Contact page"""
    return render(request,"contact.html")

def connaitre_function(request):
    return render(request,"participer.html")

def contactView(request):
    
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'jmillot41@hotmail.fr', [from_email,'jmillot41@hotmail.fr'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

# Create your views here.
def signin_function(request):
    """display the login page"""
    return render(request, "login.html")


def signup_function(request):
    """display the signup page"""
    return render(request, "signup.html")


def register(request):
    """function for create a account """
    if request.method == "GET":
        return render(request, "signup.html")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            try:
                user = form.save(commit=False)
                user.set_password(request.POST["password"])
                user.save()
                login(request, user)  # nous connectons l'utilisateur
            except Exception as e:
                form = RegistrationForm()
            return render(request, "login.html")
        else:
            return render(request, "login.html")


def connexion(request):
    """function who called when a user try to be connected"""
    # if request.method == "GET":
    #     return render(request, "index.html")
    if request.user.is_authenticated:
        return render(request, "index.html")
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        print(password)

        user = authenticate(
            username=username, password=password
        )
        print(user)
        if user is not None:  # Si l'objet renvoyé n'est pas None
            login(request, user)  # nous connectons l'utilisateur
            return redirect("index")
        else:  # sinon une erreur sera affichée
            return redirect("login")
    else:
        context = {"ConnexionForm": ConnexionForm()}
        return render(request, "login.html", context)


def logout_view(request):
    """function who call when a user logout from the website"""
    if request.method == "POST":
        logout(request)
        return render(request, "index.html")