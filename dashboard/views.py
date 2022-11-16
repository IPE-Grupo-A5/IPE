from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
import datetime

from dashboard.forms import FormDado

from .models import Dado

# Create your views here.


@login_required(login_url="/home")
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required(login_url="/home")
def add_dashboard(request):
    if request.method == "POST":
        form = FormDado(request.POST)
        if form.is_valid():
            dado = form.save(commit=False)
            dado.usuario = request.user
            dado.save()
            return redirect("/add-dashboard")
    else:
        form = FormDado()

    return render(request, 'dashboard/add_dashboard.html', {"form": form})


@login_required(login_url="/home")
def consumo_mensal(request):
    labels = []
    data = []

    queryset = Dado.objects.filter(usuario = request.user)
    for dado in queryset:
        print(dado.usuario)
        labels.append(str(dado.data_tempo))
        data.append(dado.potencia_contratada)

    zipped_list = sorted(list(zip(labels, data)), key=lambda x: datetime.datetime.strptime(x[0], '%Y-%m-%d'))

    labels = list(list(zip(*zipped_list))[0])
    data = list(list(zip(*zipped_list))[1])

    for i in range(len(labels)):
        labels[i] = labels[i][8:10] + "/" + labels[i][5:7] + "/" + labels[i][0:4]

    return render(request, 'dashboard/consumo_mensal.html', {'labels': labels, 'data': data})
