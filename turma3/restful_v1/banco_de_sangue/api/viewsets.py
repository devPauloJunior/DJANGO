from rest_framework import viewsets
from banco_de_sangue.models import Doadores
from .serializers import DoadoresSerializer

class DoadoresViewSet(viewsets.ModelViewSet):
    queryset = Doadores.objects.all()
    serializer_class = DoadoresSerializer