from django.contrib import admin
from apps.menu.models import noticias, proveedorRecompensa, recompensa

# Register your models here.
admin.site.register(noticias)
admin.site.register(proveedorRecompensa)
admin.site.register(recompensa)