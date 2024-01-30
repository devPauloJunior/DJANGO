from rest_framework import viewsets
from .serializers import AtracaoTuristicaSerializer
from atracoes_turisticas.models import AtracaoTuristica

class AtracaoTuristicaViewSet(viewsets.ModelViewSet):
    queryset = AtracaoTuristica.objects.all()
    serializer_class = AtracaoTuristicaSerializer