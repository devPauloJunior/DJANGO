from django.contrib import admin
from .models import Produto

class ProdutoList(admin.ModelAdmin):
    list_display = ('nome_produto', 'preco', 'imagem_produto', 'descricao')

admin.site.register(Produto, ProdutoList)