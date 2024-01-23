from django.db import models

class Doadores(models.Model):
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    tipo_sanguineo = models.CharField(max_length=3)
    doador = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
