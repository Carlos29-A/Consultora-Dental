from django import forms
from django.core import validators
from usuarios.models import Usuario
from django.contrib.auth.models import User
from dentista.models import Dentista

class FormCitas(forms.Form):

    fecha_cita= forms.DateField(
        label='Fecha',
        widget=forms.TextInput(
            attrs={
                "placeholder":"MM/DD/YYYY",
                "class": "form-control mt-3 mb-3",
                "type":"date"
            }),
        help_text="Ingrese la fecha en este formato Mes/Dia",
        required=True
    )
    hora_cita = forms.TimeField(
        label='Hora',
        widget=forms.TextInput(
            attrs={
                "placeholder":"HH:MM",
                "class": "form-control mt-3 mb-3",
                "type": "time"
            }
        ),
        help_text="Ingrese la Hora en este formato HH:MM (24 horas)",
        required=True
    )

    estado = forms.ChoiceField(
        label="Estado",
        choices=[
            ('Pendiente', 'Pendiente'),
            ('Confirmada', 'Confirmada'),
            ('Cancelada', 'Cancelada')],
        widget=forms.Select(
            attrs={
                "class": "form-control mt-3 mb-3"}),
        help_text="Seleccione el estado",
        required=True
    )

    motivo = forms.CharField(
        label='Motivo',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Ingresa el Motivo",
                "class": "form-control mt-3 mb-3"
            }
        ),
        help_text="Ingrese el motivo ejemplo: Dolor de Muela",
        required=True
    )
    Dentista = forms.ModelChoiceField(
        label='Dentista',
        queryset=  Dentista.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder":"Ingresa el Motivo",
                "class": "form-control mt-3 mb-3"
            }
        ),
        help_text="Ingrese el motivo ejemplo: Dolor de Muela",
        required=True
    )

class FormActualizarCita(forms.Form):
    fecha_cita = forms.DateField(
        label='Fecha',
        widget=forms.TextInput(
            attrs={
                "placeholder": "MM/DD/YYYY",
                "class": "form-control mt-3 mb-3",
                "type": "date"
            }),
        help_text="Ingrese la fecha en este formato Mes/Día",
        required=True
    )
    hora_cita = forms.TimeField(
        label='Hora',
        widget=forms.TextInput(
            attrs={
                "placeholder": "HH:MM",
                "class": "form-control mt-3 mb-3",
                "type": "time"
            }
        ),
        help_text="Ingrese la Hora en este formato HH:MM (24 horas)",
        required=True
    )
    motivo = forms.CharField(
        label='Motivo',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingresa el Motivo",
                "class": "form-control mt-3 mb-3"
            }
        ),
        help_text="Ingrese el motivo ejemplo: Dolor de Muela",
        required=True
    )