
from django.shortcuts import render, redirect
from django.contrib import messages
from firebase_admin import auth 

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            # Autenticación del usuario con Firebase
            user = auth.sign_in_with_email_and_password(email, password)

            # Si la autenticación es exitosa, redirigir a la página de inicio
            return redirect('home')  # Asegúrate de que 'home' esté definido en tus urls

        except Exception as e:
            messages.error(request, "Error al iniciar sesión: {}".format(e))

    return render(request, 'loginapp/login.html')

def home_view(request):
    return render(request, 'loginapp/home.html')

def index_view(request):  # Nueva vista para la página principal
    return render(request, 'loginapp/index.html') 

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir después de un registro exitoso
    else:
        form = RegistrationForm()
    return render(request, 'loginapp/register.html', {'form': form})
