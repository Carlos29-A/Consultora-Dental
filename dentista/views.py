from django.shortcuts import render, redirect
from dentista.froms import FormDentista
from django.db import transaction
from dentista.models import Dentista
from django.http import HttpResponse
from django.contrib.auth.models import User
from comentario.models import Comentario
# Create your views here.
@transaction.atomic
def crear_full_dentista(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method =='POST':
            formularioDentista = FormDentista(request.POST)
        
            if formularioDentista.is_valid():

                data_form_dentista = formularioDentista.cleaned_data

                username = data_form_dentista.get('username')
                

                # Validar si el usuario existe :
                if User.objects.filter(username = username).exists():
                    formularioDentista.add_error('username' ,'El nombre de usuario ya esta registrado')
                    
                    return render(request,'crear_full_dentista.html',{
                        'titulo': 'Formulario Dentista',
                        'success': False,
                        'form': formularioDentista
                    })
                # Creamos y almacenamos en la base de datos
                dentista= Dentista(
                    nombre = data_form_dentista.get('nombre'),
                    especialidad = data_form_dentista.get('especialidad'),
                    telefono = data_form_dentista.get('telefono'),
                    correo_electronico = data_form_dentista.get('correo_electronico'),
                    contraseña = data_form_dentista.get("contraseña"),
                )          
                dentista.save()

                user = User.objects.create_user(
                    username=username,
                    email=data_form_dentista.get("correo_electronico"),
                    password=data_form_dentista.get("contraseña"),
                    first_name=data_form_dentista.get("nombre")
                )
                user.save()
                
                formularioDentista = FormDentista()

                return render(request,'index.html',{
                    'titulo': 'Formulario Dentista',
                    'success': True,
                    'form': formularioDentista,
                    'paciente': False,
                    'comentarios': Comentario.objects.all()[:3]
                })           
            
        else: 
            formularioDentista = FormDentista()
            
        return render(request,'crear_full_dentista.html',{
                    'form': formularioDentista,
                    'titulo': 'Formulario Dentista',
                    'success': False,
            })