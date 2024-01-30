from django.db import models

class Filme(models.Model):
    GENERO_CHOICES = (
        ('AC', 'Ação'),
        ('AV', 'Aventura'),
        ('RO', 'Romance'),
        ('TE', 'Terror'),
        ('DR', 'Drama'),
        ('SU', 'Suspense'),
        ('FC', 'Ficção Cientifica'),
        ('CO', 'Comedia'),
        ('DO', 'Documentario'),
        ('AN', 'Animação'),
        ('NS', 'Não Selecionado'),
    )
    
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=60)
    sinopse = models.TextField()
    ano_lancamento = models.DateField()
    duracao = models.IntegerField(default=0)
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES, default='NS' )
    data_cad = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='capas', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
