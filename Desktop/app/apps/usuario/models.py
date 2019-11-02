from django.db import models

# Create your models here.
class Perfil(models.Model):
<<<<<<< HEAD
    id = models.AutoField( primary_key=True ,default=3)
    nombre = models.CharField(max_length = 30, default=0)
    apellido = models.CharField(max_length = 30,default=0)
    correoElectronico = models.EmailField(unique =True)
    username = models.CharField(unique = True, max_length = 12)
    password = models.CharField(max_length = 10)
    staff = models.BooleanField(null= False, blank= False, default=False)

class Estadistica(models.Model):
    idUsuario = models.ForeignKey(Perfil, null = True, blank = True ,on_delete =models.DO_NOTHING)
    puntaje = models.IntegerField()
    progreso = models.FloatField(default=0)
=======
    idPerfil = models.IntegerField(primary_key= True, null=False, default=0)
    nombre = models.CharField(max_length = 30,null=False, default="")
    apellido = models.CharField(max_length = 30,null=True)
    correoElectronico = models.EmailField(unique =True)
    username = models.CharField(unique = True, max_length = 12)
    password = models.CharField(max_length = 16)

class Material(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Reciclaje(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, default=0)
    tipoMaterial = models.ForeignKey(Material, null= False,on_delete=models.DO_NOTHING)
    cantidadReciclada = models.FloatField(null=False, blank=False, default=0)

class Estadistica(models.Model):
    idUsuario = models.ForeignKey(Perfil, null = True, blank = True ,on_delete =models.DO_NOTHING)
    puntaje = models.IntegerField(null=False,default=0)
    distanciaRecorrida= models.FloatField(default=0)
    objectoReciclado= models.ForeignKey(Reciclaje, on_delete=models.DO_NOTHING,null = True)

>>>>>>> b59e1fac2c6a2edc02ca4ee04333958e19c788f6
    