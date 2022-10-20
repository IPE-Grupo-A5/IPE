from django.shortcuts import render
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def home(request):
    return render(request,'clientes/home.html')
def servicos(request):
    messages.add_message(request, messages.ERROR, 'ocorreu um erro.')
    return render(request,'clientes/servicos.html')
