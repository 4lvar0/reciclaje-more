from django.shortcuts import render
from django.http import HttpResponse
from .models import proveedorRecompensa, noticias

# Create your views here.
def Home(request):
    proveedor = proveedorRecompensa.objects.all()
    noticia = noticias.objects.all()
    return render(request,'menu/Home.html',{'proveedorRecompensas':proveedor},{'noticias':noticia})


