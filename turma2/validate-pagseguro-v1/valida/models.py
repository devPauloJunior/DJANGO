from django.db import models

class Teste(models.Model):
    title = models.CharField(max_length=120) 

    def __str__(self):
        return f'{self.title}'    

class Valida(models.Model):
    name = models.CharField(max_length=120)
    area_code = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=120)
    cpf = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=120)
    number = models.IntegerField(null=True, blank=True)
    complement = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    postal_code = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.cpf}'
    