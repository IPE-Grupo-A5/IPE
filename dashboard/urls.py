from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add-dashboard', views.add_dashboard, name='add_dashboard'),
    path('consumo-mensal', views.consumo_mensal, name='consumo_mensal')
]
