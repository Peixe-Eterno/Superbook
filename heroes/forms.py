from django import forms
from .models import Hero


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['codinome', 'poder_principal', 'poderes_secundarios', 'jurisdicao', 'historia']

    def __init__(self):
        super(HeroForm, self).__init__()
        self.fields['codinome'].widget.attrs.update({'class': 'form-control'})
        self.fields['poder_principal'].widget.attrs.update({'class': 'form-control'})
        self.fields['poderes_secundarios'].widget.attrs.update({'class': 'form-control'})
        self.fields['jurisdicao'].widget.attrs.update({'class': 'form-control'})
        self.fields['historia'].widget.attrs.update({'class': 'form-control'})

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True, label="Seu nome")
    email = forms.EmailField(required=True, label="E-mail")
    mensagem = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self):
        super().__init__()
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['mensagem'].widget.attrs.update({'class': 'form-control'})
    