from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,'menu/Home.html')

def Login(request):
    return HttpResponse(request,'Hola')