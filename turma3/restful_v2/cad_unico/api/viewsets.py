from rest_framework import viewsets
from .serializers import BeneficiariosSerializer
from cad_unico.models import Beneficiarios

class BeneficiariosViewSet(viewsets.ModelViewSet):
    queryset = Beneficiarios.objects.all()
    serializer_class = BeneficiariosSerializer