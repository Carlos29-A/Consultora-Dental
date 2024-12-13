from django.urls import path
from comentario import views

urlpatterns = [
    path ("comentarios/", views.comentario, name ='comentario'),
    path ("listado-comentarios/", views.listadoComentarios, name ='listadoComentarios')
]