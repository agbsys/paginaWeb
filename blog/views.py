from django.shortcuts import render
from blog.models import post, categoria
# Create your views here.

def blog(request):
    listaBlogs = post.objects.all()   
    return render(request, "blog.html",  {"listaBlogs":listaBlogs, "valor":1})
    
def filtracategoria(request, categoria_id):
    lcategoria = categoria.objects.get(id=categoria_id)
    print(lcategoria.nombre)
    listaBlogs = post.objects.filter(categorias=lcategoria)
    #listaBlogs = post.objects.all()   
    print(listaBlogs)
    return render(request, "categorias.html", {"categorias":lcategoria, "listaBlogs":listaBlogs})