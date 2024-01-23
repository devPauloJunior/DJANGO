from django.db import models

class Beneficiarios(models.Model):
    nome = models.CharField(max_length=120, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length=150)
    cep = models.CharField(max_length=10, blank=True, null=True)
    doador = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
