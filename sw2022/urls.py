"""sw2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from actus import views as actus_views
from manage_user import views as manage_user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", actus_views.home_function, name="index"),
    path("", include('manage_user.urls')),
    path("404", manage_user_views.page_not_found_view, name="404"),
    path("500", manage_user_views.page_internal_error, name="500"),
    path("connaitre", actus_views.connaitre_function, name="connaitre"),
    path("suivre", actus_views.suivre_function, name="suivre"),
    path("contacte", manage_user_views.contact_function , name="contacte"),
    path("mentions_legales", actus_views.legals_mentions, name="mentions_legales"),
    path("join_newsletter", actus_views.join_newsletter, name="join_newsletter"),
    path("participer" , manage_user_views.connaitre_function, name="participer"),
    path("login", manage_user_views.connexion, name="login"),
    path("signup", manage_user_views.register, name="signup"),
    path("login_page",manage_user_views.signin_function,name="login_page"),
    path("logout", manage_user_views.logout_view, name="logout"),
    path("mon_compte", manage_user_views.my_account_function ,name="mon_compte"),
    path("modify_account", manage_user_views.modify_account_function ,name="modify_account"),
    path("formulaire", manage_user_views.formulaire_function, name="formulaire"),
    path("complete_signup",manage_user_views.complete_signup, name="complete_signup"),

]
