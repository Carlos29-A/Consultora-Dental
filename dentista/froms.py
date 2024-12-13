from django import forms
from django.core import validators

class FormDentista(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingrese su username", 
                "class": "form-control mt-3 mb-3"
            }
        ),
        help_text="Máximo 50 caracteres.",
        validators=[
            validators.RegexValidator('^[A-Za-zñÑ0-9._ ]*$', 'El nombre está mal', 'nombre_invalido')
        ],
        required=True
    )
    nombre = forms.CharField(
        label="Nombre",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingrese su nombre", 
                "class": "form-control mt-3 mb-3"
            }
        ),
        help_text="Máximo 50 caracteres.",
        validators=[
            validators.RegexValidator('^[A-Za-zñáéíóúÁÉÍÓÚñÑ ]*$', 'El nombre está mal', 'nombre_invalido')
        ],
        required=True
    )
    especialidad = forms.CharField(
        label="Especialidad",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Tu especialidad", 
                "class": "form-control mt-3 mb-3"
            }
        ),
        help_text="Máximo 50 caracteres.",
        required=True
    )
    telefono = forms.RegexField(
        label="Teléfono",
        regex=r'^(\+51)?(9\d{8}|0\d{1,2}\d{6,7}|\d{7})$',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ejemplo: +123456789", 
                "class": "form-control mt-3 mb-3"
            }
        ),
        help_text="Ingrese un número válido de Perú (móvil o fijo).",
        error_messages={"invalid": "Ingrese un número de teléfono válido."},
        required=True
    )
    correo_electronico = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "ejemplo@dominio.com", 
                "class": "form-control mt-3 mb-3"
            }
        ),
        help_text="Ingrese un correo electrónico válido.",
        required=True
    )
    contraseña = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Ingrese su contraseña", 
                "class": "form-control mt-3 mb-3"
            }
        ),
        help_text="Debe tener al menos 8 caracteres.",
        required=True
    )