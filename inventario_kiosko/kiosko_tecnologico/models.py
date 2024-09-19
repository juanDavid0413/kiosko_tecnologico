from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return str(self.nombre)    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
    
class DetalleProducto(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    especificaciones = models.TextField()
    fecha_vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"
    
class Venta(models.Model):
    fecha_venta = models.DateTimeField(auto_now_add=True,)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f'Venta de {self.cantidad} {self.producto} a {self.cliente}'
