# registro_app/urls.py

from django.urls import path
from .views import registro

urlpatterns = [
    path('', registro, name='registro'),  # URL raíz de la aplicación de registro
]
