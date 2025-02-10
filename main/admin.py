from django.contrib import admin
from .models import Universo, SpiderMan, Enemigo, Batalla, Comentario

# Registrar los modelos en el panel de administración
admin.site.register(Universo)
admin.site.register(SpiderMan)
admin.site.register(Enemigo)
admin.site.register(Batalla)
admin.site.register(Comentario)