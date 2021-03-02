from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .forms import formularioContacto

# Create your views here.
def contacto(request):
    if request.method=="POST":
        miformulario = formularioContacto(request.POST)
        #miformulario.as_p()   ##Con parrafos
        #miformulario.as_ul()   ##Con forma de Lista
        #miformulario.as_table() #Con forma de Tabla 
        if miformulario.is_valid():
            ifform = miformulario.cleaned_data
            try:
                send_mail(ifform["nombre"] , ifform["mensaje"] ,ifform["email"],['agbsys@gmail.com'],fail_silently=False,)
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    else:
        miformulario = formularioContacto()
    return render(request, "contactos.html", {"form": miformulario})
    