from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Savoir(models.Model):
    """Savoir class"""

    title = models.CharField(max_length=150)
    date = models.CharField(max_length=50)
    link_yt = models.CharField(max_length=200,blank=True)
    link_pdf = models.CharField(max_length=100,blank=True)
    ouvert_par_defaut = models.CharField(max_length=10, default="",blank=True)
    disponible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering = ['created_at']
         
    def __str__(self):
        return self.title

class Actusuivre(models.Model):
    """Actusuivre class"""

    title = models.CharField(max_length=150)
    link = models.CharField(max_length=200,blank=True)
    date = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering = ['created_at']
         
    def __str__(self):
        return self.title

class Agendasuivre(models.Model):
    """Actusuivre class"""

    title = models.CharField(max_length=150)
    lieu = models.CharField(max_length=100,blank=True)
    ville = models.CharField(max_length=50,blank=True)
    date = models.CharField(max_length=50,blank=True)
    heure = models.CharField(max_length=50,blank=True)
    message = models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
         ordering = ['created_at']
         
    def __str__(self):
        return self.title

class Newsletter_model(models.Model):
    """List of the User who receive the Newsletter"""
    email = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    subscribed = models.BooleanField(default=True)

    class Meta:
         ordering = ['date']
         
    def __str__(self):
        return self.email

