# registro_app/views.py

from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages
from firebase_admin import auth, firestore
from django.conf import settings  # Importa settings para acceder a la configuración de Firebase

# Inicializa Firestore
db = firestore.client()

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            contrasena = form.cleaned_data['contrasena']

            # Registra al usuario en Firebase Authentication
            try:
                # Crear el usuario en Firebase
                user = auth.create_user(
                    email=correo,
                    password=contrasena,
                    display_name=nombre  # Puedes almacenar el nombre del usuario si deseas
                )

                # Guarda en Firestore
                db.collection('registros').add({
                    'nombre': nombre,
                    'correo': correo,
                })

                messages.success(request, 'Usuario registrado con éxito.')
                return redirect('login')  # Cambia esto a la vista de inicio de sesión o donde necesites

            except Exception as e:
                messages.error(request, f'Error al registrar el usuario: {str(e)}')
                form.add_error(None, 'Error al registrar el usuario. Intente nuevamente.')
    else:
        form = RegistroForm()
    
    return render(request, 'registro/registro.html', {'form': form})
