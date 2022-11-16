from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add-dashboard', views.add_dashboard, name='add_dashboard'),
    path('update-dashboard/<str:pk>/', views.update_dashboard, name='update_dashboard'),
    path('delete-dashboard/<str:pk>/', views.delete_dashboard, name='delete_dashboard'),
    path('consumo-mensal', views.consumo_mensal, name='consumo_mensal')
]
