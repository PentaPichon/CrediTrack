from django import forms
from .models import OperacionTarjeta, ConfiguracionTarjeta

class OperacionTarjetaForm(forms.ModelForm):
    class Meta:
        model = OperacionTarjeta
        fields = [
            'tarjeta_credito',
            'fecha_operacion', 
            'concepto', 
            'monto', 
            'tipo_operacion', 
            'cantidad_cuotas']
        widgets = {
            'fecha_operacion' : forms.DateInput(format='%Y-%m-%d',attrs={'type':'date'}),
            
        }

    def __init__ (self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super(OperacionTarjetaForm, self).__init__(*args, **kwargs)
        if usuario:
            self.fields['tarjeta_credito'].queryset=ConfiguracionTarjeta.objects.filter(usuario=usuario)
            self.fields['tarjeta_credito'].label_from_instance = lambda obj: f"{obj.nombre}"

