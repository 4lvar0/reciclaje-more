from django.db import models
import datetime

# Create your models here.
class proveedorRecompensa(models.Model):
    id = models.IntegerField(primary_key = True,null = False)
    nombre = models.CharField(max_length=20)
    Logo = models.CharField(max_length=2083, blank=True)

class recompensa(models.Model):
    idproveedor = models.ForeignKey(proveedorRecompensa , on_delete = models.DO_NOTHING)
    idrecompensa = models.IntegerField(primary_key= True, null=False, default=0)
    descripcion = models.CharField(max_length=17)
    expiracion = models.DateField(null= True)
    activo = models.BooleanField(null= False, blank= False, default=False)

class noticias(models.Model):
    codigoNoticia = models.IntegerField(primary_key= True, blank = True, null = False )
    titulo = models.CharField(max_length = 40, null = False, default ='Missing')
    fecha = models.DateField(default=datetime.date.today)
    descripcion = models.CharField(max_length=70)
    Imagen = models.CharField(max_length=2083,blank=True)