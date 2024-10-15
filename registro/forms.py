# registro_app/forms.py

from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput()) 