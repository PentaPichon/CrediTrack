from django import forms
from .models import OperacionTarjeta

class OperacionTarjetaForm(forms.ModelForm):
    class Meta:
        model = OperacionTarjeta
        fields = ['fecha_operacion', 'concepto', 'monto', 'tipo_operacion', 'cantidad_cuotas']
