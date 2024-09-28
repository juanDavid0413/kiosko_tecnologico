from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Proveedor, Producto, Factura, DetalleVenta
from .forms import ClienteForm, ProveedorForm, ProductoForm, DetalleVentaForm, FacturaForm
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def listar_ventas(request):
    ventas = Factura.objects.all()
    return render(request, 'listar_ventas.html', {'ventas': ventas})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = form.save()
            return redirect('agregar_detalle_venta', factura_id=factura.id)
    else:
        form = FacturaForm()
    return render(request, 'crear_factura.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form})

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form})   

def editar_producto(request, pk):
    productos = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=productos)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=productos)
    return render(request, 'editar_producto.html', {'form': form})    

def editar_venta(request, pk):
    ventas = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=ventas)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = FacturaForm(instance=ventas)
    return render(request, 'editar_venta.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listar_proveedores')
    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedor})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

def eliminar_venta(request, pk):
    ventas = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        ventas.delete()
        return redirect('listar_ventas')
    return render(request, 'eliminar_venta.html', {'ventas':ventas} )

def agregar_detalle_venta(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.factura = factura
            producto = detalle.producto
            if producto.stock >= detalle.cantidad:
                producto.stock -= detalle.cantidad
                producto.save()  
                detalle.save()  
                factura.total = factura.calcular_total()  
                factura.save()  
                return redirect('agregar_detalle_venta', factura_id=factura.id)
            else:
                return render(request, 'agregar_detalle_venta.html', {
                    'form': form,
                    'factura': factura,
                    'productos': Producto.objects.all(),
                })
    else:
        form = DetalleVentaForm()
    
    productos = Producto.objects.all()
    return render(request, 'agregar_detalle_venta.html', {
        'form': form,
        'factura': factura,
        'productos': productos,
    })
