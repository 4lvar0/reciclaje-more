from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import authenticate
from django.conf import settings

# Create your models here.
class Perfil(AbstractUser):
    id = models.AutoField( primary_key=True ,default=3)
    nombre = models.CharField(max_length = 30, default=0)
    apellido = models.CharField(max_length = 30,default=0)
    correoElectronico = models.EmailField(unique =True)
    username = models.CharField(unique = True, max_length = 12)
    password = models.CharField(max_length = 10)

    def authenticate(request,username=None,password=None):
        try:
            user= authenticate(username = username,password=password)
            if user is not None:
                return user
            else:
                return None
        except Perfil.DoesNotExist:
                return None

    def get_user( username=None ):
        try:
            return Perfil.objects.get(username = username)
        except Perfil.DoesNotExist:
            return None
            
    def get_email(correoElectronico=None):
        try:
            return Perfil.objects.get(correoElectronico=correoElectronico)
        except Perfil.DoesNotExist:
            return None

class Material(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Reciclaje(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, default=0)
    tipoMaterial = models.ForeignKey(Material, null= False,on_delete=models.DO_NOTHING)
    cantidadReciclada = models.FloatField(null=False, blank=False, default=0)

class Estadistica(models.Model):
    idUsuario = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, blank = True ,on_delete =models.DO_NOTHING)
    puntaje = models.IntegerField(null=False,default=0)
    distanciaRecorrida= models.FloatField(default=0)
    objectoReciclado= models.ForeignKey(Reciclaje, on_delete=models.DO_NOTHING,null = True)

    