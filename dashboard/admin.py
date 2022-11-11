from django.contrib import admin
from .models import Dado

# Register your models here.

class dadoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dado, dadoAdmin)