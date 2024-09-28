from django import forms
from .models import Cliente, Proveedor, Producto, DetalleVenta, Factura
from django.core.exceptions import ValidationError

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

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente']


class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad']

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')

        if producto and cantidad:  
            if cantidad > producto.stock:
                raise forms.ValidationError(f'La cantidad solicitada ({cantidad}) excede el stock disponible ({producto.stock}).')

        return cleaned_data
    
  
