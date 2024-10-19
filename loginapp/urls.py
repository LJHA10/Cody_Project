# loginapp/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view
from . import views

urlpatterns = [
    path('login/', login_view, name='login'),# Ruta para el login
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
