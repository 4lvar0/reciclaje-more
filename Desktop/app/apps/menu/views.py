from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import recompensa, proveedorRecompensa , noticias
from django.contrib.auth import login 
# Create your views here.
def Home(request):
    proveedor = proveedorRecompensa.objects.all()
    recompensas = recompensa.objects.filter(activo=True)
    noticia = noticias.objects.all()
    context ={'empresa':proveedor,'recompensa':recompensas,'noticia':noticia}
    return render(request,'menu/Home.html',context)

def Ingresar(request):
    return render(request, 'usuario/Ingreso/login.html')

def Registrar(request):
    return render(request, 'usuario/Ingreso/registro.html')

def Perfil(request):
    return render(request, 'usuario/Perfil/perfil.html')

