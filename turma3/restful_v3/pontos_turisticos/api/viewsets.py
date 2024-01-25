from rest_framework import viewsets
from .serializers import PontoTuristicoSerializer
from pontos_turisticos.models import PontoTuristico

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer