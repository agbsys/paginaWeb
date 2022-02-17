from django.shortcuts import render

# Create your views here.

from .carro import Carro
from tienda.models import Productos
from django.shortcuts import redirect

def agregarProducto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect("tienda")

def eliminarProducto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.eliminarProducto(producto)
    return redirect("tienda")

def restarProducto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar_producto(producto)
    return redirect("tienda")

def limpiarCarro(request, productoId):
    carro = Carro(request)
    producto = Productos.objects.get(id=productoId)
    carro.limparCarro()
    return redirect("tienda")
    