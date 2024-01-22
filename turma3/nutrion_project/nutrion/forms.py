from django import forms
from .models import Food

class FoodModelForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['nome', 'carboidratos', 'proteinas', 'gorduras', 'calorias']