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
    def id(self):
        return self.pk

    def authenticate(request,username=None,password=None):
        try:
            user= authenticate(username = username,password=password)
            if user is not None:
                return user
            else:
                return None
        except Perfil.DoesNotExist:
                return None

class Friend(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owner", null=True,on_delete=models.CASCADE)

    def search_friend(self,username):
        user = self.objects.select_related('users').get(username=username)
        return user

    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)

class Estadistica(models.Model):
    idUsuario = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, blank = True ,on_delete =models.DO_NOTHING)
    puntaje = models.IntegerField(null=False,default=0)
    def get_cantidad(id):
        cantidad = Reciclaje.objects.select_related('idUsuario').get(idUsuario=id)
        return cantidad

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True,max_length=100)

class Reciclaje(models.Model):
    id = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    tipoMaterial = models.ForeignKey(Material, null= False,on_delete=models.DO_NOTHING)
    cantidadReciclada = models.FloatField(null=False, blank=False, default=0)

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

class recompensaFavoritos(models.Model):
    idUsuario = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    idRecompensa = models.ManyToManyField(recompensa)
    def add_favorito(self, current_user, recompensa):
        favorito, created = self.objects.get_or_create(
            current_user = current_user
        )
        favorito.idRecompensa.add(recompensa)


class noticias(models.Model):
    codigoNoticia = models.AutoField(primary_key= True)
    titulo = models.CharField(max_length = 70, null = False, default ='Missing')
    fecha = models.DateField(default=datetime.date.today)
    descripcion = models.CharField(max_length=500)
    Imagen = models.CharField(max_length=2083)

    