from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html", {"valor":request.path})

def tienda(request):
    return render(request, "tienda.html",  {"valor":request.path})

def contacto(request):
    return render(request, "contactos.html",{"valor":request.path})
