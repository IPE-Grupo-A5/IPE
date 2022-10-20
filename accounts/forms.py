from socket import fromshare
from django.forms import ModelForm
from django import forms
from .models import Dados


class UploadForm(ModelForm):
    concessionaria = forms.ChoiceField()
    subgrupo = forms.ChoiceField()
    energia_utilizada_p = forms.TextInput()
    energia_utilizada_fp = forms.TextInput()
    potencia_utilizada_p = forms.TextInput()
    potencia_contratada = forms.TextInput()

    class Meta:
        model = Dados
        fields = ['concessionaria', 'subgrupo', 'energia_utilizada_p',
                  'energia_utilizada_fp', 'potencia_utilizada_p', 'potencia_contratada']
