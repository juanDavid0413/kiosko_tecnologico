from django.urls import path
from .views import (listar_clientes, editar_cliente, crear_cliente, eliminar_cliente, inicio,
                    listar_proveedores, editar_proveedor, crear_proveedor, eliminar_proveedor,
                    listar_productos, editar_producto, crear_producto, eliminar_producto
                    )

urlpatterns = [
    path('', inicio, name = 'inicio'),

    path('clientes/', listar_clientes , name='listar_clientes'),
    path('clientes/crear_cliente', crear_cliente, name='crear_cliente'),
    path('clientes/editar_cliente/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar_cliente/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),

    path('proveedores/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/crear/', crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),

    path('productos/', listar_productos, name='listar_productos' ),
    path('productos/crear', crear_producto, name='crear_producto'), 
    path('producto/editar/<int:pk>', editar_producto, name='editar_producto'), 
    path('producto/eliminar/<int:pk>', eliminar_producto, name='eliminar_producto')
    ]