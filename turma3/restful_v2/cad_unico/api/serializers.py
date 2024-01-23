from rest_framework import serializers
from cad_unico.models import Beneficiarios

class BeneficiariosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Beneficiarios
        fields = '__all__'