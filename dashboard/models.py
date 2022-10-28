from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    LIGHT = "LIGHT"
    A2 = "A2"
    A4 = "A4"
    A5 = "A5"

    CONCESSIONARIA_CHOICES = [
        (LIGHT, "Light"),
    ]

    SUBGRUPO_CHOICES = [
        (A2, "A2"),
        (A4, "A4"),
        (A5, "A5"),
    ]

    concessionaria = models.CharField(
        max_length=5,
        choices=CONCESSIONARIA_CHOICES
    )

    subgrupo = models.CharField(
        max_length=2,
        choices=SUBGRUPO_CHOICES
    )

    energia_utilizada_p = models.PositiveIntegerField()
    energia_utilizada_fp = models.PositiveIntegerField()
    potencia_utilizada_p = models.PositiveIntegerField()
    potencia_contratada = models.PositiveIntegerField()
