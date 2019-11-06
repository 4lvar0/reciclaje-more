from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from .views import Home,Login,Registrar,Account,Account_premios,Account_noticias, Logout

urlpatterns = [
    path('', Home, name='home'),
    re_path(r'^Ingresar/',Login, name='login'),
    re_path(r'^Registrarse/', Registrar,name='registro'),
    re_path(r'^Perfil/$',login_required(Account),name='usuario'),
    re_path(r'^Premios/$',Account_premios,name='premios'),
    re_path(r'^Noticias/',Account_noticias,name='noticias'),
    path('Salir/',Logout, name="Salir")
]