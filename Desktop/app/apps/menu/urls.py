from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import Home, Login

urlpatterns = [
    path('', Home,name='home'),
    path('Login/',Login,name='login')
]