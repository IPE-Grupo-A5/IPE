from django import forms
from .models import Dado
from datetime import date

class FormDado(forms.ModelForm):
    concessionaria = forms.TextInput()
    subgrupo = forms.TextInput()
    energia_utilizada_p = forms.TextInput()
    energia_utilizada_fp = forms.TextInput()
    potencia_utilizada_p = forms.TextInput()
    potencia_contratada = forms.TextInput()

    this_year = date.today().year
    year_range = [x for x in range(this_year - 5, this_year + 1)]
    data_tempo = forms.DateField(
        widget=forms.SelectDateWidget(years=year_range),
    )

    class Meta:
        model = Dado
        fields = ['concessionaria', 'subgrupo', 'energia_utilizada_p',
                  'energia_utilizada_fp', 'potencia_utilizada_p', 'potencia_contratada', 'data_tempo']