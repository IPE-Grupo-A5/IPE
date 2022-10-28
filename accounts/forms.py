from django.forms import ModelForm
from .models import Dado

class FormDado(ModelForm):
    class Meta:
        model = Dado
        fields ='__all__'
        exclude = ()