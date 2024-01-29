from django import forms
from gestor_tarjetas.models import ConfiguracionTarjeta


class ConfiguracionTarjetaForm(forms.ModelForm):
    class Meta:
        model = ConfiguracionTarjeta
        fields = [
            'nombre',
            'fecha_cierre',
            'fecha_vencimiento'
        ]
        widgets = {
            'fecha_cierre' : forms.DateInput(attrs={'type':'date'}),
            'fecha_vencimiento' : forms.DateInput(attrs={'type':'date'}),
            
        }