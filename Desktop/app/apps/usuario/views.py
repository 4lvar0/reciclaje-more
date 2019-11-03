from django.shortcuts import render, redirect
from apps.menu.views import Home, Ingresar, Registrar
from .models import Perfil
from django.db.models import Q
from django.core.cache import cache
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.
def Login(request):
    try:
        user = Perfil.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect(Home)
        else:
            messages.error(request, 'El nombre de usuario y/o contraseña son invalidos', extra_tags='username')
            return redirect(Ingresar)
    except Perfil.DoesNotExist:
            messages.error(request, 'El nombre de usuario y/o contraseña son invalidos', extra_tags='username')
            return redirect(Ingresar)


def Logout(request):
    logout(request)
    return redirect(Home)

def Register(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect(Home)
        else:
            try:
                if Perfil.get_user(username=request.POST['username']) is not None:
                    messages.error(request, 'El nombre de usuario no esta disponible', extra_tags='username')
                    return redirect(Registrar)
                elif Perfil.get_email(correoElectronico = request.POST['email']) is not None:
                    messages.error(request, 'El email ya se encuentra registrado', extra_tags='email')
                    return redirect(Registrar)
                else:
                    usuario = Perfil.objects.create_user(
                                 nombre =request.POST['name'],
                                 apellido=request.POST['lastName'],
                                 correoElectronico=request.POST['email'],
                                 username =request.POST['username']
                                 )
                    usuario.set_password(request.POST['password'])
                    usuario.is_staff=False
                    usuario.save()
                return redirect(Home)
            except Perfil.DoesNotExist:
                usuario = Perfil.objects.create_user(
                                 nombre =request.POST['name'],
                                 apellido=request.POST['lastName'],
                                 correoElectronico=request.POST['email'],
                                 username =request.POST['username']
                                 )
                usuario.set_password(request.POST['password'])
                usuario.is_staff=False
                usuario.save()
                return redirect(Home)
    else:
        return redirect(Registrar)
    

        




