from django.shortcuts import render, redirect
from django.http import HttpResponse
from citas.froms import FormCitas,FormActualizarCita
from citas.models import Citas
from dentista.models import Dentista
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="loginUsuario")
def crear_full_citas(request):

    if request.method =='POST':

        formulario = FormCitas(request.POST)

        if formulario.is_valid():

            formulario_data = formulario.cleaned_data

            fecha = formulario_data.get('fecha_cita')
            hora = formulario_data.get('hora_cita')
            estado = formulario_data.get('estado')
            motivo = formulario_data.get('motivo')
            idDentista = formulario_data.get('Dentista')

            cita = Citas(
                fecha_cita =fecha,
                hora_cita =hora,
                estado = estado,
                motivo = motivo,
                id_usuario = request.user,
                id_dentista = idDentista
            )

            cita.save()

            return HttpResponse("Se creo la cita correctamente")
        else:
            return HttpResponse("Ocurrio un error")

    else:
        formulario = FormCitas()

    return render(request,'formularioCitas.html', {
        'formulario' : formulario
    })
@login_required(login_url="loginUsuario")
def listadoCitas(request):

    usuario = request.user

    correos_dentistas = Dentista.objects.values_list('correo_electronico',flat=True)
    bandera = False

    if usuario.email in correos_dentistas :
        bandera = True
        dentista=Dentista.objects.get(correo_electronico = usuario.email)
        citas = Citas.objects.filter(id_dentista_id = dentista.id)
    else :        
        citas = Citas.objects.filter(id_usuario_id = usuario.id)

    return render(request,'listadoCitas.html' ,{
        'citas': citas,
        'bandera': bandera
    })
@login_required(login_url="loginUsuario")
def actualizarCita(request,id):

    citaActualizada = Citas.objects.get(pk=id)

    if request.method=='POST':

        formulario = FormActualizarCita(request.POST)

        if formulario.is_valid():

            formulario_data = formulario.cleaned_data

            fecha = formulario_data.get('fecha_cita')
            hora = formulario_data.get('hora_cita')
            motivo = formulario_data.get('motivo')
        
            citaActualizada.fecha_cita = fecha
            citaActualizada.hora_cita = hora
            citaActualizada.motivo = motivo

            citaActualizada.save()

            return redirect ('listadoCitas')
    else:
        formulario = FormActualizarCita(initial={
            'fecha_cita': citaActualizada.fecha_cita,
            'hora_cita': citaActualizada.hora_cita,
            'motivo': citaActualizada.motivo,
        })

    return render(request,'actualizarCita.html',{
        'FormularioActualizado' : formulario
    })
@login_required(login_url="loginUsuario")
def actualizarEstado(request,id):
    citaActualizada = Citas.objects.get(pk=id)

    citaActualizada.estado = 'Cancelada'

    citaActualizada.save()

    return redirect('listadoCitas')
@login_required(login_url="loginUsuario")
def eliminarCita(request,id):
    citaEliminada = Citas.objects.get(pk=id)

    citaEliminada.delete()

    citas = Citas.objects.all()

    return redirect('listadoCitas')

