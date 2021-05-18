from django.shortcuts import render

# Create your views here.

from .carro import Carro
from tienda.models import Productos
from django.shortcuts import redirect

def agregarProducto(request, productoId):
    carro = Carro(request)
    producto = Productos.objects.get(id=productoId)
    carro.agregar(producto)
    return redirect("tienda")

def eliminarProducto(request, productoId):
    carro = Carro(request)
    producto = Productos.objects.get(id=productoId)
    carro.eliminarProducto(producto)
    return redirect("tienda")

def restarProducto(request, productoId):
    carro = Carro(request)
    producto = Productos.objects.get(id=productoId)
    carro.restar_producto(producto)
    return redirect("tienda")

def limpiarCarro(request, productoId):
    carro = Carro(request)
    producto = Productos.objects.get(id=productoId)
    carro.limparCarro()
    return redirect("tienda")
    