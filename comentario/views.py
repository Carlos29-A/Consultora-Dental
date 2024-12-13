from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from comentario.froms import ComentarioForm
from comentario.models import Comentario
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from citas.models import Citas
from dentista.models import Dentista
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="loginUsuario")
def comentario(request):

    if request.method == 'POST':
        # Verificar si se envió un dentista desde el formulario de selección
        dentista_id = request.POST.get('dentista_id')
        if dentista_id:
            try:
                dentista = Dentista.objects.get(id=dentista_id)
                citas = Citas.objects.filter(id_dentista=dentista, id_usuario=request.user)
                return render(request, 'comentario.html', {
                    'dentista': dentista,
                    'citas': citas
                })
            except Dentista.DoesNotExist:
                return render(request, 'seleccionar_dentista.html', {
                    'dentistas': Dentista.objects.all(),
                    'error': 'El dentista seleccionado no existe.'
                })

        # Manejar el formulario de comentarios
        cita_id = request.POST.get('cita_id')
        if cita_id:
            try:
                cita = Citas.objects.get(id=cita_id, id_usuario=request.user)
                dentista = cita.id_dentista
                contenido = request.POST.get('contenido')
                calificacion = request.POST.get('calificacion')

                if contenido and calificacion:
                    Comentario.objects.create(
                        contenido=contenido,
                        calificacion=calificacion,
                        paciente_id=request.user,
                        cita_id=cita,
                        dentista_id=dentista
                    )
                    return redirect('comentario')  # Redirigir después del éxito
                
            except Citas.DoesNotExist:
                return render(request, 'comentario.html', {
                    'error': 'La cita seleccionada no es válida.',
                    'citas': [],
                    'dentista': None
                })

    # Mostrar la lista de dentistas si no se envió un formulario válido
    return render(request, 'seleccionar_dentista.html', {
        'dentistas': Dentista.objects.all()
    })

def listadoComentarios(request):
    # Mostrar todos los comentarios
    bandera=False
    if request.user.is_authenticated:
        usuario = request.user
        correos_dentistas = Dentista.objects.values_list('correo_electronico',flat=True)
        # Mostrar comentarios especificos
        bandera=True
        if usuario.email in correos_dentistas :
            dentista = Dentista.objects.get(correo_electronico = usuario.email)
            comentarios = Comentario.objects.filter(dentista_id=dentista)     
            return render(request,'listadoComentarios.html',{
            'comentarios': comentarios,
            'bandera':bandera,
            'paciente': False
            })
        else :
            comentarios = Comentario.objects.filter(paciente_id=request.user)      
            return render(request,'listadoComentarios.html',{
            'comentarios': comentarios,
            'bandera':bandera,
            'paciente': True
            })
   
    else:
        comentarios = Comentario.objects.all()
        return render(request,'listadoComentarios.html',{
            'comentarios': comentarios,
            'bandera':bandera
        })