from django.urls import path
from .views import (listar_clientes, editar_cliente, crear_cliente, eliminar_cliente, inicio)

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('clientes/', listar_clientes , name='listar_clientes'),
    path('clientes/crear_cliente', crear_cliente, name='crear_cliente'),
    path('clientes/editar_cliente/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar_cliente/<int:pk>/', eliminar_cliente, name='eliminar_cliente')
    ]