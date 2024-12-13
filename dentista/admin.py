from django.contrib import admin
from .models import Dentista
# Register your models here.

class DentistaAdmin(admin.ModelAdmin):
    list_display = ("nombre","especialidad","correo_electronico")

admin.site.register(Dentista, DentistaAdmin)