from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.lista_categorias, name='lista'),
    path('crear/', views.crear_categoria, name='crear'),
    path('<int:id>/editar/', views.editar_categoria, name='editar'),
    path('<int:id>/eliminar/', views.eliminar_categoria, name='eliminar'),
]