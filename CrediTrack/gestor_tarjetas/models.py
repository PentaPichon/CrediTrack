from django.db import models
from django.conf import settings



class ConfiguracionTarjeta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tarjetas_credito', null=False)
    nombre = models.CharField(max_length=100, null=False)
    fecha_cierre = models.DateField()
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre
    

class OperacionTarjeta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='operaciones',null=False )
    tarjeta_credito = models.ForeignKey(ConfiguracionTarjeta, on_delete=models.CASCADE, related_name='operaciones',null=False)
    TIPOS_OPERACION = (
        ('CUOTA', 'Compra en Cuotas'),
        ('SUSCRIPCION', 'Suscripcion Mensual')
    )
    CANTIDAD_CUOTAS = (
        (1, '1'),
        (3, '3'),
        (6, '6'),
        (9, '9'),
        (12, '12'),
    )
    fecha_operacion = models.DateField()
    concepto = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_operacion = models.CharField(max_length=12, choices=TIPOS_OPERACION)
    cantidad_cuotas = models.PositiveIntegerField(default=1, choices=CANTIDAD_CUOTAS) #Solo para compras en cuotas

    def __str__(self):
        return f"{self.concepto} - {self.fecha_operacion}"
    

class Calendario(models.Model):
    operacion_id = models.ForeignKey(OperacionTarjeta, on_delete=models.CASCADE)
    numero_cuota = models.PositiveIntegerField()
    monto_cuota = models.DecimalField(max_digits=10, decimal_places =2)
    fecha_vencimiento = models.DateField()
    fecha_cierre_en_operacion = models.DateField(null=False)
    concepto = models.CharField(max_length=200)

    def __str__(self):
        return f"Cuota {self.numero_cuota} de {self.operacion_id}"


