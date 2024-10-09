# registro_app/views.py

from django.shortcuts import render, redirect
from .forms import RegistroForm
import firebase_admin
from firebase_admin import firestore

# Inicializa Firestore
db = firestore.client()

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']

            # Guarda en Firebase
            db.collection('registros').add({
                'nombre': nombre,
                'correo': correo,
            })

            return redirect('registro')  # Redirige a la misma página
    else:
        form = RegistroForm()
    
    return render(request, 'registro/registro.html', {'form': form})
