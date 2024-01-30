from rest_framework import serializers
from atracoes_turisticas.models import AtracaoTuristica

class AtracaoTuristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtracaoTuristica
        fields = '__all__'