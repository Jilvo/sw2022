from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Savoir(models.Model):
    """Savoir class"""

    title = models.CharField(max_length=150)
    date = models.CharField(max_length=50)
    link_yt = models.CharField(max_length=200)
    link_pdf = models.CharField(max_length=100)
    ouvert_par_defaut = models.CharField(max_length=10, default="",blank=True)
    disponible = models.BooleanField()

    def __str__(self):
        return self.title