from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)

class Perfil(models.Model):
    idPerfil = models.ForeignKey(Usuario , null = True ,blank = True , on_delete = models.DO_NOTHING)
    correoElectronico = models.EmailField(unique =True)
    username = models.CharField(unique = True, max_length = 12)
    password = models.CharField(max_length = 10)

class Estadistica(models.Model):
    idUsuario = models.ForeignKey(Usuario, null = True, blank = True ,on_delete =models.DO_NOTHING)
    puntaje = models.IntegerField()
    progreso = models.FloatField(default=0)
    