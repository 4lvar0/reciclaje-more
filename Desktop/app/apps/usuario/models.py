from .managers import CustomUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User, PermissionsMixin
from django.contrib.auth import authenticate
from django.conf import settings
import datetime

# Create your models here.
class Perfil(AbstractBaseUser,PermissionsMixin):
    nombre = models.CharField(max_length = 30, default=0)
    apellido = models.CharField(max_length = 30,default=0)
    correoElectronico = models.EmailField(unique =True)
    username = models.CharField(unique = True, max_length = 12)
    password = models.CharField(max_length = 10)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'password'
    EMAIL_FIELD = 'correoElectronico'
    objects = CustomUserManager()
    #Permisos
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    #metodos
    def authenticate(request,username=None,password=None):
        try:
            user= authenticate(username = username,password=password)
            if user is not None:
                return user
            else:
                return None
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

class proveedorRecompensa(models.Model):
    id = models.AutoField(primary_key = True,null = False)
    nombre = models.CharField(max_length=20)
    Logo = models.CharField(max_length=2083)
    def get_empresa(id):
        try:
            empresa = proveedorRecompensa.objects.get(id=id)
            return empresa
        except proveedorRecompensa.DoesNotExist:
            return None

class recompensa(models.Model):
    idproveedor = models.ForeignKey(proveedorRecompensa , on_delete = models.DO_NOTHING)
    idrecompensa = models.AutoField(primary_key= True)
    descripcion = models.CharField(max_length=30)
    expiracion = models.DateField(null= True)
    activo = models.BooleanField(null= False, blank= False, default=False)
    costo = models.IntegerField(null=False,default=0)

    def get_recompensas(id):
        try:
            empresa = proveedorRecompensa.get_empresa(id)
            recompensas = recompensa.objects.filter(idproveedor=id).filter(activo=True)
            return recompensas, empresa
        except recompensa.DoesNotExist:
            return None

class noticias(models.Model):
    codigoNoticia = models.AutoField(primary_key= True)
    titulo = models.CharField(max_length = 70, null = False, default ='Missing')
    fecha = models.DateField(default=datetime.date.today)
    descripcion = models.CharField(max_length=500)
    Imagen = models.CharField(max_length=2083)

    