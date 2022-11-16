from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from dashboard.forms import FormDado

from .models import Dado

# Create your views here.


@login_required(login_url="/home")
def dashboard(request):
    data_list = Dado.objects.filter(usuario=request.user)
    paginator = Paginator(data_list,10)
    page = request.GET.get('p')
    data = paginator.get_page(page)
    return render(request, 'dashboard/dashboard.html',{"dados":data})


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
def update_dashboard(request,pk):
    data = Dado.objects.get(id=pk)
    form = FormDado(instance=data)
    if request.method == "POST":
        form = FormDado(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("/dashboard")
    
    return render(request, 'dashboard/update_dashboard.html', {"form": form})



@login_required(login_url="/home")
def delete_dashboard(request,pk):
    data = Dado.objects.get(id=pk)
    if request.method=="POST":
        data.delete()
        return redirect("/dashboard")
    return render(request, 'dashboard/delete_dashboard.html', {"item": data})


@login_required(login_url="/home")
def consumo_mensal(request):
    labels = []
    data = []

    queryset = Dado.objects.order_by('potencia_contratada')
    for dado in queryset:
        labels.append(dado.energia_utilizada_fp)
        data.append(dado.potencia_contratada)
    return render(request, 'dashboard/consumo_mensal.html', {'labels': labels, 'data': data})
