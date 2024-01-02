from django.contrib import admin

from .models import OperacionTarjeta, ConfiguracionTarjeta

admin.site.register(OperacionTarjeta)
admin.site.register(ConfiguracionTarjeta)
