from django.db import models

class Plans(models.Model):
    titulo = models.CharField(max_length=120)
    description = models.CharField('Descrição', max_length=300)
    type_plan = models.CharField('Tipo de Plano', max_length=50)
    road_map = models.CharField('Roteiro', max_length=300)
    duration = models.IntegerField('Duração', default=0)
    value = models.FloatField('Preço', default=0.0)

    def __str__(self):
        return f'{self.titulo}'
