from django.db import models

# Create your models here.
class proveedorRecompensa(models.Model):
    id = models.IntegerField(primary_key = True,null = False)
    activo = models.BooleanField(null= False, blank= False)
    nombre = models.CharField(max_length=20)
    Logo = models.ImageField(default='default.png')

class recompensa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=17)
    expiracion = models.DateField()

class noticias(models.Model):
    codigoNoticia = models.IntegerField(primary_key= True, blank = True, null = False )
    descripcion = models.CharField(max_length=30)
    Imagen = models.ImageField(default='default.png')