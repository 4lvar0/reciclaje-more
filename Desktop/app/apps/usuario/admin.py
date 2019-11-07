from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Perfil,Estadistica,Reciclaje,Material, noticias, proveedorRecompensa, recompensa

# Register your models here.

admin.site.register(Perfil)
admin.site.register(Estadistica)
admin.site.register(Reciclaje)
admin.site.register(Material)
admin.site.register(noticias)
admin.site.register(proveedorRecompensa)
admin.site.register(recompensa)