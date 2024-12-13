from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario,Mensaje
from usuarios.froms import FormUsuario,FormMensaje
from django.contrib import messages
from dentista.models import Dentista
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from comentario.models import Comentario
from django.db import transaction
# Create your views here.
def inicio(request):

    comentarios = Comentario.objects.all()

    # todos los email
    correos_dentistas = Dentista.objects.values_list('correo_electronico',flat=True)
    bandera = False
    if request.user.is_authenticated: 
        if request.user.email in correos_dentistas :
            bandera = True

    return render(request,'index.html', {
        'titulo': 'Inicio',
        'comentarios': comentarios,
        "bandera": bandera
    })

def nosotros(request):

    dentistas =  Dentista.objects.all()[:4]
    

    return render(request, 'nosotros.html', {
        'titulo':'nosotros',
        'dentistas': dentistas
    })
def nosotros_id(request,id):

    dentistas =  Dentista.objects.all()

    return render(request, 'nosotros.html', {
        'titulo':'nosotros',
        'dentistas': dentistas
    })
@transaction.atomic
def cerrar_session(request):
    logout(request)
    return redirect('loginUsuario')


def contacto(request):

    if request.method == 'POST':
        formulario_data=FormMensaje(request.POST)

        if formulario_data.is_valid():
            formulario_data.save()  # Guardar los datos directamente en la base de datos
            return redirect("contacto")

    else:
        formulario_data = FormMensaje()

    return render(request, 'contacto.html' ,{
        'titulo':'contacto',
        'formulario': formulario_data
    })

def guardar_usuario(request):
    return HttpResponse('Usuario Guardado')
@transaction.atomic
def login_usuario(request):
    username = request.POST.get('username')
    print(username)
    if request.user.is_authenticated:
         return redirect('inicio')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password= password)

            if user is not None:

                login(request, user)

                return redirect('inicio')
            else:
                messages.warning(request, 'No te has identificado correctamente')

        return render(request,'loginUsuario.html')
@transaction.atomic
def crear_full_usuario(request):
    # Verificamos que el usuario no este autenticado
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            formulario = FormUsuario(request.POST)

            if formulario.is_valid():
                datos_form = formulario.cleaned_data
                username = datos_form.get('username')
                nombre = datos_form.get('nombre')
                correo = datos_form.get('correo')
                contraseña = datos_form.get('contraseña')
                telefono = datos_form.get('telefono')
                rol = datos_form.get('rol')

                # Verificar si el nombre de usuario ya existe
                if User.objects.filter(username=username).exists():
                    formulario.add_error('username', 'El nombre de usuario ya está registrado')
                    return render(request, 'crear_full_usuario.html', {
                        'form': formulario,
                        'titulo': 'Formulario de registro',
                        'success': False
                    })

                # Creamos en la tabla de la base de datos y los guardamos
                usuario = Usuario(
                    nombre=nombre,
                    correo=correo,
                    contraseña=contraseña,
                    telefono=telefono,
                    rol=rol
                )
                usuario.save()

                user = User.objects.create_user(
                    username=username,
                    email=correo,
                    password=contraseña,
                    first_name=nombre
                )
                user.save()

                # Reseteamos el Formulario :

                formulario  = FormUsuario()

                return render(request, 'index.html', {
                    'success': True,
                    'form': formulario, 
                    'titulo': 'Formulario de registro',
                    'paciente': True,
                    'comentarios': Comentario.objects.all()[:3]
                })

        else: 
            formulario = FormUsuario()

        return render(request, 'crear_full_usuario.html', {
            'form': formulario,
            'titulo': 'Formulario de registro',
            'success': False
        })


def selecForm(request):

    titulo = 'SelecForm'
    
    return render(request,'SelecForm.html',{
        'titulo' : titulo
    })

