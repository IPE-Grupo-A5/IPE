from django import forms
from .models import Dado

class FormDado(forms.ModelForm):
    # concessionaria = forms.TextInput()
    # subgrupo = forms.TextInput()
    # energia_utilizada_p = forms.TextInput()
    # energia_utilizada_fp = forms.TextInput()
    # potencia_utilizada_p = forms.TextInput()
    # potencia_contratada = forms.TextInput()

    class Meta:
        model = Dado
        fields = ['concessionaria', 'subgrupo', 'energia_utilizada_p',
                  'energia_utilizada_fp', 'potencia_utilizada_p', 'potencia_contratada']