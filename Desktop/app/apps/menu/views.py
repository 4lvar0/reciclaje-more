from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import recompensa, proveedorRecompensa , noticias
from django.contrib.auth import login 
# Create your views here.
def Home(request):
    proveedor = proveedorRecompensa.objects.all()
    recompensas = recompensa.objects.all()
    noticiosas = noticias.objects.all()
    return render(request,'menu/Home.html',{'noticia':noticiosas,'Empresa':proveedor,'recompensa':recompensas})

def Ingresar(request):
    return render(request, 'usuario/Ingreso/login.html')

def Registrar(request):
    return render(request, 'usuario/Ingreso/registro.html')


