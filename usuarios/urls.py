from django.contrib import admin
from django.urls import path
from  . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path('nosotros/<int:id>',views.nosotros_id, name='nosotros'),
    path('contacto/',views.contacto, name='contacto'),
    path('guardar-usuario/', views.guardar_usuario, name='guardar-usuario'),
    path('crear_full_usuario/',views.crear_full_usuario, name='crear_full_usuario'),
    path('login-usuario/',views.login_usuario, name='loginUsuario'),
    path('cerrar-session/',views.cerrar_session, name='cerrarSesion'),
    path('selectForm/',views.selecForm, name='selectForm')
]
