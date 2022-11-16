from django.contrib import admin
from .models import Dado

# Register your models here.

class dadoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_tempo', 'potencia_contratada')

admin.site.register(Dado, dadoAdmin)