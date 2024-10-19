# loginapp/views.py

from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User  # Importa el modelo User

class RegistrationForm(UserCreationForm):  # Hereda de UserCreationForm
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Cambia a la URL de tu vista principal
        else:
            messages.error(request, "Credenciales incorrectas.")
    
    return render(request, 'loginapp/login.html')

def home_view(request):
    return render(request, 'loginapp/home.html')

def index_view(request):
    return render(request, 'loginapp/index.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # Usa el formulario de creación de usuarios
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'loginapp/register.html', {'form': form})
