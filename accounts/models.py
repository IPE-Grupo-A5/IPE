from django.db import models
from django import forms


# Create your models here.

class Dado(models.Model):
    concessionaria = models.CharField(
        choices = (
            ("1", "Light"),
        )
        , max_length = 255
    )
    subgrupo = models.CharField(
        choices = (
            ("1", "A2"),
            ("2", "A4"),
            ("3", "A5"),
        )
        , max_length = 255
    )

    energia_utilizada_p = models.PositiveIntegerField()
    energia_utilizada_fp = models.PositiveIntegerField()
    potencia_utilizada_p = models.PositiveIntegerField()
    potencia_contratada = models.PositiveIntegerField()

class FormDado(forms.ModelForm):
    class Meta:
        model = Dado
        fields ='__all__'
        exclude = ()