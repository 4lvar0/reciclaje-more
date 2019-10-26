from django.shortcuts import render
from django.http import HttpResponse
from apps.menu.models import recompensa, proveedorRecompensa , noticias

# Create your views here.
def Home(request):
    proveedor = proveedorRecompensa.objects.all()[:2]
    noticia = noticias.objects.all()
    return render(request,'menu/Home.html',{'proveedorRecompensas':proveedor},{'noticias':noticia})


