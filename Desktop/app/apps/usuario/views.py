from django.shortcuts import render, redirect
from apps.menu.views import Home, Ingresar, Registrar
from .models import Perfil
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.
<<<<<<< HEAD
=======
def Ingresar(request):
    return render(request,'usuario/ingreso/login.html')

def Registrar(request):
    return render(request, 'usuario/ingreso/registro.html')

>>>>>>> b59e1fac2c6a2edc02ca4ee04333958e19c788f6
def Login(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return render(request,Home)
    else:
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
                usuario = Perfil.objects.all()
                if usuario.get(username =request.POST['username']):
                    messages.error(request, 'El nombre de usuario no esta disponible', extra_tags='username')
                elif usuario.get(correoElectronico =request.POST['email']):
                    messages.error(request, 'El email ya se encuentra registrado', extra_tags='email')
                return redirect(Registrar)
            except Perfil.DoesNotExist:
                usuario = Perfil.objects.create(
                                                    nombre =request.POST['name'],
                                                    apellido=request.POST['lastName'],
                                                    correoElectronico=request.POST['email'],
                                                    username =request.POST['username'],
                                                    password =request.POST['password'],
                                                    staff = False
                                                    )
                return render(request,Home)
    else:
        return redirect(Registrar)

        




