from django.shortcuts import render
from .models import Productos, categoriaProd

# Create your views here.
def tienda(request):    
    listaProductos = Productos.objects.all()   
    return render(request, "tienda.html",  {"listaProductos":listaProductos, "valor":1})