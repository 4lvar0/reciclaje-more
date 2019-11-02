from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from .models import recompensa, proveedorRecompensa , noticias
from django.contrib.auth import login 
# Create your views here.
def Home(request):
    proveedor = proveedorRecompensa.objects.all()
    recompensas = recompensa.objects.all()
    noticiosas = noticias.objects.all()
    return render(request,'menu/Home.html',{'noticia':noticiosas})

def Ingresar(request):
    return render(request, 'usuario/login.html')

def Registrar(request):
    return render(request, 'usuario/registro.html')
=======
from .models import proveedorRecompensa, noticias

# Create your views here.
def Home(request):
    proveedor = proveedorRecompensa.objects.all()
    noticia = noticias.objects.all()
    return render(request,'menu/Home.html',{'proveedorRecompensas':proveedor},{'noticias':noticia})
>>>>>>> b59e1fac2c6a2edc02ca4ee04333958e19c788f6


