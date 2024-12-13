from django.contrib import admin
from .models import Citas

class CitasAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):

        if not change:  
            obj.id_usuario = request.user

        super().save_model(request, obj, form, change)

admin.site.register(Citas, CitasAdmin)
