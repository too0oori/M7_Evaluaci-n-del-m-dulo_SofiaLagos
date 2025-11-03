from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista_productos(request):
    return render(request, 'lista_productos.html')

def crear_producto(request):
    return render(request, 'crear_producto.html')

def editar_producto(request):
    return render(request, 'editar_producto.html')

def eliminar_producto(request):
    return render(request, 'eliminar_producto.html')

def detalle_producto(request):
    return render(request, 'detalle_producto.html')