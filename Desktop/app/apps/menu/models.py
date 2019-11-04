from django.db import models
import datetime

# Create your models here.
class proveedorRecompensa(models.Model):
    id = models.AutoField(primary_key = True,null = False)
    nombre = models.CharField(max_length=20)
    Logo = models.CharField(max_length=2083)

class recompensa(models.Model):
    idproveedor = models.ForeignKey(proveedorRecompensa , on_delete = models.DO_NOTHING)
    idrecompensa = models.AutoField(primary_key= True)
    descripcion = models.CharField(max_length=30)
    expiracion = models.DateField(null= True)
    activo = models.BooleanField(null= False, blank= False, default=False)

    def get_recompensa(id):
        try:
            recompensa = recompensa.objects.filter(idproveedor=id,activo=True)
            return recompensa
        except recompensa.DoesNotExist:
            return None

class noticias(models.Model):
    codigoNoticia = models.AutoField(primary_key= True)
    titulo = models.CharField(max_length = 70, null = False, default ='Missing')
    fecha = models.DateField(default=datetime.date.today)
    descripcion = models.CharField(max_length=500)
    Imagen = models.CharField(max_length=2083)
