from django.db import models
from stdimage import StdImageField

class Produto(models.Model):
    nome_produto = models.CharField(max_length=120)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem_produto = StdImageField(upload_to='produtos', variations={'thumb': (124, 124)}, delete_orphans=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome_produto
