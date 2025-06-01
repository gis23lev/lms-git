# usuarios/forms.py
from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')



# REGISTRO ESTUDIANTE

class RegistroEstudianteForm(forms.Form):
    username = forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    ci = forms.CharField(max_length=20)
    telefono = forms.CharField(max_length=20, required=False)
    carrera = forms.CharField(max_length=100, required=False)


# REGISTRO DOCENTE

class RegistroDocenteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    ci = forms.CharField(max_length=20)
    telefono = forms.CharField(max_length=20, required=False)
    profesion = forms.CharField(max_length=100, required=False)


class DocenteLoginForm(forms.Form):
    nombre = forms.CharField(label="Nombre")
    ci = forms.CharField(label="CI", widget=forms.PasswordInput)