from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from usuarios.models import Mensaje
from django.utils.translation import gettext_lazy as _

class FormUsuario(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingrese su username", 
                "class": "form-control mt-3 mb-3"
                }),
        help_text="Máximo 50 caracteres.",
        validators=[
            validators.RegexValidator('^[A-Za-zñÑ0-9._ ]*$', 'El nombre esta mal', 'nombre_invalido')
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
                }),
        help_text="Máximo 50 caracteres.",
        validators=[
            validators.RegexValidator('^[A-Za-zñáéíóúÁÉÍÓÚñÑ ]*$', 'El nombre esta mal', 'nombre_invalido')
        ],
        required=True
    )
    correo = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "ejemplo@dominio.com", 
                "class": "form-control mt-3 mb-3"
                }),
        help_text="Ingrese un correo electrónico válido.",
        required=True
    )
    contraseña = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Ingrese su contraseña", 
                "class": "form-control mt-3 mb-3"
                }),
        help_text="Debe tener al menos 8 caracteres.",
        required=True
    )
    telefono = forms.RegexField(
        label="Teléfono",
        regex=r'^(\+51)?(9\d{8}|0\d{1,2}\d{6,7}|\d{7})$',
        widget=forms.TextInput(
            attrs={
            "placeholder": "Ejemplo: +123456789", 
            "class": "form-control mt-3 mb-3"
            }),
        help_text="Ingrese un número válido de Perú (móvil o fijo).",
        error_messages={"invalid": "Ingrese un número de teléfono válido."},
        validators=[
            validators.RegexValidator('^[0-9]*$','Numero incorrecto')
        ],
        required=True
    )
    rol = forms.ChoiceField(
        label="Rol",
        choices=[
            ("admin", "Administrador"), 
            ("user", "Paciente")],
        widget=forms.Select(
            attrs={"class": "form-control mt-3 mb-3"}),
        help_text="Seleccione el rol del usuario.",
        required=True
    )

class FormMensaje(ModelForm):
    class Meta:
        model = Mensaje
        fields = ["nombre","correo_electronico","asunto","mensaje"]
        labels ={
            "nombre":_("Nombre"),
            "correo_electronico":_("Correo Electrónico"),
            "asunto":_("Asunto"),
            "mensaje":_("Mensaje"),
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control my-3"}),
            "correo_electronico": forms.EmailInput(attrs={"class": "form-control my-3"}),
            "asunto": forms.TextInput(attrs={"class": "form-control my-3"}),
            "mensaje": forms.Textarea(attrs={"class": "form-control my-3", "rows": 4}),
        }
