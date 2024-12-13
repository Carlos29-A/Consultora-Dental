from django.forms import ModelForm
from comentario.models import Comentario
from django.utils.translation import gettext_lazy as _
from django import forms
class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ["contenido","calificacion","cita_id","dentista_id"]
        labels = {
            "contenido":_("Contenido"),
            "calificacion":_("Calificación"),
            "cita_id":_("Cita"),
            "dentista_id":_("Dentista")
        }
        widgets = {
            "contenido": forms.TextInput(attrs={"class": "form-control my-3"}),
            "calificacion": forms.NumberInput(attrs={"class": "form-control my-3"}),
            "cita_id": forms.Select(attrs={"class": "form-control my-3"}),
            "dentista_id":forms.Select(attrs={"class": "form-control my-3"})
        }