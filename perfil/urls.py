from django.urls import path
from .views import perfil

urlpatterns = [
    path('', perfil, name='perfil'),  # URL raíz de la aplicación de registro
]
