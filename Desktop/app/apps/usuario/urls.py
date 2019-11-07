from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from .views import Home,Login,Registrar,Account,Account_amigos,Account_premios,Account_noticias,Account_settings, Logout

urlpatterns = [
    path('', Home, name='home'),
    re_path(r'^Ingresar/',Login, name='login'),
    path('Registrarse/', Registrar,name='registro'),
    re_path(r'^Perfil/$',login_required(Account),name='usuario'),
    re_path(r'^Amigos/$',login_required(Account_amigos),name='amigos'),
    re_path(r'^Premios/$',Account_premios,name='premios'),
    re_path(r'^Noticias/',Account_noticias,name='noticias'),
    re_path(r'^Ajustes/',Account_settings,name='configuracion'),
    path('Salir/',Logout, name="Salir")
]