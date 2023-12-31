from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
#creatiionform
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Usuario
from .forms import InquilinoForm


#Administrador e Index
def index(request):
     title='Index'
    # return HttpResponse("Hello, world. You're at the polls index.")
     return render (request,"sistemabio/index.html",{
          'mytitle':title
     })
     
def signup(request):
        if request.method == 'GET':
            print('enviando formulario')
            title='Registrar'
            return render(request, "sistemabio/signup.html",{
                'mytitle':title,
                'form':UserCreationForm
            } ) 
        else:
             if request.POST["password1"] == request.POST["password2"]:
                  #register user
                  try:
                    user = User.objects.create_user(username=request.POST["username"],
                                                   password=request.POST["password1"])
                    user.save()
                    login(request, user)
                    return redirect('/sistemabio/principal/')
                   # return HttpResponse('User creado satisfactoriamente')        
                  except IntegrityError:
                       return render(request, "sistemabio/signup.html",{
                            'error': 'El user ya existe',
                            'form':UserCreationForm
                        } ) 
             return render(request, "sistemabio/signup.html",{
                            'error': 'Passwords no coinciden',
                            'form':UserCreationForm
                        } )   
 

   #return render(request, "sistemabio/signin.html",
def signin(request):
         if request.method == "GET":
            title='Iniciar sesion'
            return render(request, "sistemabio/signin.html",{
                'mytitle':title,
                'form':AuthenticationForm
            } )        
         else:
              user = authenticate( request, username=request.POST['username'], password=request.POST['password'])
              if user is None:
                return render(request, 'sistemabio/signin.html',{
                    'error': "usuario o password es incorrecto.",
                    'form': AuthenticationForm
                    })

              login(request, user)
              return redirect('/sistemabio/principal/')
            
   #return render(request, "sistemabio/signin.html",
@login_required
def principal(request):
     title='Principal Administrador'
     return render (request,"sistemabio/principal.html",{
          'mytitle':title
     })
@login_required
def signout(request):
     logout(request)
     return redirect('/sistemabio/signin/')
def about(request):
     title='About'
     return render (request,"sistemabio/about.html",{
          'mytitle':title
     })

#Inquilinos
def inquilinosinicial(request):
     title='Inquilinos Inicial'
     return render (request,"sistemabio/inquilinos/inquilinos_inicial_copy.html",{
          'mytitle':title
     })
def inquilinos(request):
     inquilinos = Usuario.objects.all()
     title='Inquilinos'
     return render (request,"sistemabio/inquilinos/all-inquilinos.html",{
          'mytitle':title,
          'inquilinos':inquilinos
     })

def new_inquilino(request):
     if request.method == "GET":
        return render(request, 'sistemabio/inquilinos/new-inquilino.html', {"form":  InquilinoForm})
     else:
        # print(request.POST)
        # return render(request, 'sistemabio/inquilinos/new-inquilino.html', {"form":  InquilinoForm})
        try:
            form = InquilinoForm(request.POST)
            new_inquilino = form.save(commit=False)
            new_inquilino.save()
            return redirect('/sistemabio/inquilinos/')
        except ValueError:
            return render(request, 'sistemabio/inquilinos/new-inquilino.html', {"form":  InquilinoForm, "error": "Error creando el inquilino."})
def search_inquilino(request):
     busqueda = request.POST.get("buscar")
     print('nusqueda es ',busqueda)
     nombre = request.POST.get("nombre")
     print('nombre es ',nombre)
     piso = request.POST.get("piso")
     print('npiso es ',piso)
     departamento = request.POST.get("departamento")
     print('ndepartamento es ',departamento)
     inquilinos = Usuario.objects.all()
     if busqueda:
        inquilinos = Usuario.objects.filter(
            Q(piso__icontains = busqueda) | 
            Q(nombre__icontains = busqueda) |
            Q(curp__icontains = busqueda) |
            Q(departamento__icontains = busqueda)
        ).distinct()  
     if nombre:
        inquilinos = Usuario.objects.filter(
            Q(nombre__icontains = nombre) 
        ).distinct()  
        print('nombre des ',nombre)
     if piso:
        inquilinos = Usuario.objects.filter(
            Q(piso__icontains = piso) 
        ).distinct() 
        print('npiso des ',piso) 
     if departamento:
        inquilinos = Usuario.objects.filter(
            Q(departamento__icontains = departamento)
        ).distinct() 
        print('ndepartamento des ',departamento)
        print('inquilino es ',inquilinos)
    # inquilino = get_object_or_404(Usuario,pk=inquilino_para)
    #  inquilinos = Usuario.objects.filter(nombre='jessica sanchez pruebaF5')
     title='search'
     return render (request,"sistemabio/inquilinos/s-inquilinos.html",{
          'mytitle':title,
          'inquilinos':inquilinos
     })
#     
def detail_inquilino(request, usuario_id):
    inquilino = get_object_or_404(Usuario,pk=usuario_id)
    print('usuario id ', usuario_id)
    title='detail'
    return render(request,"sistemabio/inquilinos/detail-inquilino.html",{
        'mytitle':title,
        'inquilino':inquilino
    })

def delete_inquilino(request, inquilino_id):
    inquilino = Usuario.objects.get( id_usuario=inquilino_id)
    if request.method == 'POST':
        inquilino.delete()
        return redirect('/sistemabio/inquilinos/')

