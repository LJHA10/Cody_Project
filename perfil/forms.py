from django import forms


class PerfilForm(forms.Form):
    
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    correo = forms.EmailField(label='Correo')
    contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    
