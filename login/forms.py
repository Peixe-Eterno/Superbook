from django import forms
from .models import Conta

class CriarConta(forms.Form):
    
    class Meta:
        model = Conta
        fields = ('email', 'senha')
        