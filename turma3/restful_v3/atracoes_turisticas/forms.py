from django import forms
from .models import AtracaoTuristica

class AtracaoTuristicaForm(forms.ModelForm):
    class Meta:
        model = AtracaoTuristica
        fields = '__all__'