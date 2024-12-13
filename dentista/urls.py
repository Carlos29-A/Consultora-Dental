from django.contrib import admin
from django.urls import path
from  . import views
urlpatterns = [
    path('crear_full_dentista/',views.crear_full_dentista, name='crear_full_dentista')
]
