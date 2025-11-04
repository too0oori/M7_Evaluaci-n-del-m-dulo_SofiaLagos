from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Página de inicio
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    
    # Aplicaciones
    path('productos/', include('apps.productos.urls')),
    path('categorias/', include('apps.categorias.urls')),
    path('etiquetas/', include('apps.etiquetas.urls')),
]