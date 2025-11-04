from django.urls import path
from . import views


app_name = 'etiquetas'

urlpatterns = [
    path('', views.lista_etiquetas, name='lista'),
    path('crear/', views.crear_etiqueta, name='crear'),
    path('<int:id>/editar/', views.editar_etiqueta, name='editar'),
    path('<int:id>/eliminar/', views.eliminar_etiqueta, name='eliminar'),
]