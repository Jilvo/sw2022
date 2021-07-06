from django.contrib import admin
from .models import Savoir, Agendasuivre, Actusuivre, Newsletter_model

# Register your models here.

admin.site.register(Savoir)
admin.site.register(Agendasuivre)
admin.site.register(Actusuivre)
admin.site.register(Newsletter_model)
