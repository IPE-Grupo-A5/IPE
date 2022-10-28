from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('servicos', views.servicos, name='servicos'),
    path('cadastro', views.sign_up, name='cadastro'),
]
