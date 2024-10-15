# registro_app/views.py

from django.shortcuts import render, redirect
from .forms import RegistroForm
import firebase_admin
from firebase_admin import auth, firestore

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
                user = auth.create_user_with_email_and_password(correo, contrasena)
                
                # Guarda en Firestore
                db.collection('registros').add({
                    'nombre': nombre,
                    'correo': correo,
                })
                return redirect('registro') 
            except Exception as e:
                form.add_error(None, 'Error al registrar el usuario: {}'.format(e))
    else:
        form = RegistroForm()
    
    return render(request, 'registro/registro.html', {'form': form})
