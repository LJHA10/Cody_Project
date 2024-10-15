# loginapp/urls.py
from django.urls import path
from .views import login_view
from . import views

urlpatterns = [
    path('login/', login_view, name='login'),# Ruta para el login
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
]
