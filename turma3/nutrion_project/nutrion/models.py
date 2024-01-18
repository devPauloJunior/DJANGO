from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    nome = models.CharField(max_length=100)
    carboidratos = models.FloatField()
    proteinas = models.FloatField()
    gorduras = models.FloatField()
    calorias = models.IntegerField()

    def __str__(self):
        return self.nome

class Consumed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comida_consumida = models.ForeignKey(Food, on_delete=models.CASCADE)

