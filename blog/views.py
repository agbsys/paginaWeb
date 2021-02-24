from django.shortcuts import render
from blog.models import post, categoria
# Create your views here.

def blog(request):
    listaBlogs = post.objects.all()   
    return render(request, "blog.html",  {"listaBlogs":listaBlogs, "valor":1})
    
def categoria(request, categoria_id):
    lcategorias = categoria.objects.get(id=categoria_id)
    listaBlogs = post.objects.filter(categorias=lcategorias)   
    return render(request, "categorias.html", {"categorias":lcategorias, "listaBlogs":listaBlogs})