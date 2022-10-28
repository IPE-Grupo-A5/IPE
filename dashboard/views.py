from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from dashboard.forms import FormDado

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