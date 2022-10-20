from django.db import models

# Create your models here.

class Dados(models.Model):
    concessionaria = models.PositiveSmallIntegerField(
        choices = (
            ("1", "Light"),
        )
    )

    subgrupo = models.PositiveSmallIntegerField(
        choices = (
            ("1", "A2"),
            ("2", "A4"),
            ("3", "A5"),
        )
    )

    energia_utilizada_p = models.PositiveIntegerField()
    energia_utilizada_fp = models.PositiveIntegerField()
    potencia_utilizada_p = models.PositiveIntegerField()
    potencia_contratada = models.PositiveIntegerField()