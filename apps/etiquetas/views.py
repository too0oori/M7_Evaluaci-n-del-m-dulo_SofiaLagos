from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista_etiquetas(request):
    return render(request, 'lista_etiquetas.html')

def crear_etiqueta(request):
    return render(request, 'crear_etiqueta.html')

def editar_etiqueta(request):
    return render(request, 'editar_etiqueta.html')

def eliminar_etiqueta(request):
    return render(request, 'eliminar_etiqueta.html')
