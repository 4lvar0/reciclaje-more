from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Perfil, noticias, proveedorRecompensa, recompensa

# Register your models here.

admin.site.register(Perfil)
admin.site.register(noticias)
admin.site.register(proveedorRecompensa)
admin.site.register(recompensa)