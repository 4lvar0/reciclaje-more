from django.shortcuts import render, redirect
from .forms import CustomCreationForm
from .models import Perfil , proveedorRecompensa, recompensa, noticias
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.
def Home(request):
    proveedor = proveedorRecompensa.objects.all()
    for a in proveedor:
        recompensas = recompensa.objects.prefetch_related('idproveedor').filter(activo=True)
    premios = zip(proveedor,recompensas)
    noticia = noticias.objects.all()[:2]
    context ={'premios':premios,'noticia':noticia}
    return render(request,'usuario/menu/Home.html',context)

def Recuperar_contraseña(request):
    return render(request, 'usuario/Ingreso/Recuperar_contraseña.html')

def Account(request):
    return render(request, 'usuario/Perfil/Perfil.html')

def Account_premios(request):
    proveedor = proveedorRecompensa.objects.all()
    for a in proveedor:
        recompensas = recompensa.objects.prefetch_related('idproveedor').filter(activo=True)
    premios = zip(proveedor,recompensas)
    context = {'premios':premios}
    return render(request, 'usuario/Perfil/Premios.html',context)

def Account_noticias(request):
    noticia = noticias.objects.all()
    context ={'noticia':noticia}
    return render(request, 'usuario/Perfil/Noticias.html',context)

def Login(request):
    if request.method == 'POST':
        user = Perfil.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect(Home)
        else:
            messages.error(request, 'El nombre de usuario y/o contraseña son invalidos', extra_tags='username')
            return render(request, 'usuario/Ingreso/Login.html')
    else:
        return render(request, 'usuario/Ingreso/Login.html')

def Logout(request):
    logout(request)
    return redirect(Home)

def Registrar(request):
    if request.method == 'POST':
        try:
            username=request.POST['username']
            email =request.POST['correoElectronico']
            if Perfil.objects.filter(username=username,correoElectronico=email):
                messages.error(request,'Email o usuario no disponible')
            form = CustomCreationForm()
            return render(request, 'usuario/Ingreso/Registro.html' ,{'form':form} )
        except Perfil.DoesNotExist:
            user = Perfil.objects.create_user(nombre=request.POST['nombre'],
                                              apellido=request.POST['apellido'],
                                              email=request.POST['correoElectronico'],
                                              username=request.POST['username'],
                                              password=request.POST['password']
                                              )
            login(request,user)
            return redirect(Home)
    else:
        form = CustomCreationForm()
        return render(request, 'usuario/Ingreso/Registro.html' ,{'form':form} )
    

        




