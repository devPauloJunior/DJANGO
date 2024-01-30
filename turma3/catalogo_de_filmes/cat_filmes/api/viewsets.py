from rest_framework import viewsets
from .serializers import FilmeSerializer
from cat_filmes.models import Filme

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer