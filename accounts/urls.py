from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index-login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-dados-dashboard/', views.add_dados_dashboard,
         name='add_dados_dashboard'),
]
