from rest_framework import serializers
from banco_de_sangue.models import Doadores

class DoadoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doadores
        fields = ['nome', 'sobrenome', 'tipo_sanguineo', 'doador']