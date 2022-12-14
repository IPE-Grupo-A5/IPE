from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login

def home(request):
    return render(request, 'main/home.html')

def servicos(request):
    return render(request, 'main/servicos.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = RegisterForm()

    return render(request, 'registration/cadastro.html', {"form": form})