from django.db import models
import datetime

# Create your models here.
class proveedorRecompensa(models.Model):
    id = models.AutoField(primary_key = True,null = False)
    nombre = models.CharField(max_length=20)
<<<<<<< HEAD
    Logo = models.CharField(max_length=2083)
=======
    Logo = models.CharField(max_length=2083, blank=True)
>>>>>>> b59e1fac2c6a2edc02ca4ee04333958e19c788f6

class recompensa(models.Model):
    idproveedor = models.ForeignKey(proveedorRecompensa , on_delete = models.DO_NOTHING)
    idrecompensa = models.IntegerField(primary_key= True, null=False, default=0)
    descripcion = models.CharField(max_length=30)
    expiracion = models.DateField(null= True)
    activo = models.BooleanField(null= False, blank= False, default=False)

class noticias(models.Model):
    codigoNoticia = models.AutoField(primary_key= True)
    titulo = models.CharField(max_length = 70, null = False, default ='Missing')
    fecha = models.DateField(default=datetime.date.today)
<<<<<<< HEAD
    descripcion = models.CharField(max_length=500)
    Imagen = models.CharField(max_length=2083)
=======
    descripcion = models.CharField(max_length=70)
    Imagen = models.CharField(max_length=2083,blank=True)
>>>>>>> b59e1fac2c6a2edc02ca4ee04333958e19c788f6
