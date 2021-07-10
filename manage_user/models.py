from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=10,null=True)
    profession = models.CharField(max_length=100, blank=True)
    adresse = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=5)
    commune = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    telephone = models.CharField(max_length=10, blank=True)
    elu = models.BooleanField(default=False)
    fonction_elu = models.CharField(max_length=100, blank=True)
    total_don = models.IntegerField(null=True, default=0)
    soutien = models.BooleanField(default=False)
    campagne = models.BooleanField(default=False)
    parrainage = models.BooleanField(default=False)
