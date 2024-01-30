from django.db import models

class AtracaoTuristica(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to='atracoes_turisticas', null=True, blank=True)
    valuation = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    cad_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



