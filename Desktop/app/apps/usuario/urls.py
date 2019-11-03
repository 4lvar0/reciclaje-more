from django.contrib import admin
from django.urls import path, include
from .views import Login, Register , Logout
from apps.menu.views import Registrar

urlpatterns = [
    path('autenticar/', Login, name="login"),
    path('Registrarse/', Registrar,name='registro'),
    path('Registrarse/Registrar/', Register,name='register'),
    path('Salir/',Logout, name="Salir")
]