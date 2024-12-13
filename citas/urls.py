from django.contrib import admin
from django.urls import path
from  . import views
urlpatterns = [
    path('registrar-cita/',views.crear_full_citas, name='registroCitas'),
    path('listado-cita/',views.listadoCitas, name='listadoCitas'),
    path('listado-cita/<int:id>',views.actualizarEstado, name='ActualizarEstado'),
    path('actualizar-cita/<int:id>',views.actualizarCita, name='actualizarCita'),
    path('Eliminar-cita/<int:id>',views.eliminarCita, name='eliminarCita'),
]