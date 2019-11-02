from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import logout_then_login
from .views import Home , Ingresar, Registrar

urlpatterns = [
    path('', Home,name='home'),
    path('Ingresar/', Ingresar,name='Login'),
    path('Registrar/', Registrar,name='Registrarse'),

]