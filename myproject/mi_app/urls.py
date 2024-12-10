from django.urls import path
from .views import agregar_cliente

urlpatterns = [
    path('cliente/', agregar_cliente, name='agregar_cliente'),
]
