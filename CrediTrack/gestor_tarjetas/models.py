from django.db import models


class OperacionTarjeta(models.Model):
    TIPOS_OPERACION = (
        ('CUOTA', 'Compra en Cuotas'),
        ('SUSCRIPCION', 'Suscripcion Mensual')
    )

    fecha_operacion = models.DateField()
    concepto = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_operacion = models.CharField(max_length=12, choices=TIPOS_OPERACION)
    cantidad_cuotas = models.IntegerField(null=True, blank=True) #Solo para compras en cuotas

    def __str__(self):
        return f"{self.concepto} - {self.fecha_operacion}"
    

class ConfiguracionTarjeta(models.Model):
    fecha_cierre = models.DateField()
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Cierre: {self.fecha_cierre}, venciemiento: {self.fecha_vencimiento}"
    