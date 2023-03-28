from django import forms
from .models import capacidad

class capacidadForm(forms.ModelForm):
    class Meta:
        model = capacidad
        fields = '__all__'
