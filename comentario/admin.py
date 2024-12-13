from django.contrib import admin
from .models import Comentario
# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Contenido", {"fields":["contenido"]}),
        ("Calificacion", {"fields":["calificacion"]}),
        ("Fecha_Creacion",{"fields":["fecha_creacion"]}),
        ("Paciente_id",{"fields":["paciente_id"]}),
        ("Cita_id",{"fields":["cita_id"]}),
        ("Dentista_id",{"fields":["dentista_id"]})
    ]

admin.site.register(Comentario,ComentarioAdmin)