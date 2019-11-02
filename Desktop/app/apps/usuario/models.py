from django.db import models

# Create your models here.
class Perfil(models.Model):
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
    