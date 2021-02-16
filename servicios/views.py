from django.shortcuts import render
from servicios.models import servicio

# Create your views here.

def servicios(request):
    listaServicios = servicio.objects.all()   
    return render(request, "servicios.html",  {"listaServicios":listaServicios, "valor":1})