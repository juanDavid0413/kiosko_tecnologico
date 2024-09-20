from django import forms
from .models import Cliente, Proveedor, Producto, DetalleProducto, Venta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'direccion', 'email']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono'] 

class ProductoForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'proveedor']

class DetalleProductoForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['producto', 'especificaciones', 'fecha_vencimiento']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'cantidad', 'total']
