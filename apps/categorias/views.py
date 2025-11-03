from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def lista_categorias(request):
    return render(request, 'lista_categorias.html')

def crear_categoria(request):
    return render(request, 'crear_categoria.html')

def editar_categoria(request):
    return render(request, 'editar_categoria.html')

def eliminar_categoria(request):
    return render(request, 'eliminar_categoria.html')