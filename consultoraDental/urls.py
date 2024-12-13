from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('',include('citas.urls')),
    path('',include('dentista.urls')),
    path('',include('comentario.urls'))
]
