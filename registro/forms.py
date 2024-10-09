# registro_app/forms.py

from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo')
