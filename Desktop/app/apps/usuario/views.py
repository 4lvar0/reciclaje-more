from django.shortcuts import render, redirect
from apps.menu.views import Home
from apps.usuario.models import Perfil

# Create your views here.
def Ingresar(request):
    return render(request,'usuario/ingreso/login.html')

def Registrar(request):
    return render(request, 'usuario/ingreso/registro.html')

def Login(request):
    usuario = Perfil.objects.get(username =request.POST['username'])
    if usuario.password == request.POST['password']:
        request.session['idPerfil'] == m.idPerfil
        return render(request,Home)
    else:
        return render(request,Login)




