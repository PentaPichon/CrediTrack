from django.shortcuts import render, redirect
from .models import OperacionTarjeta
from .forms import OperacionTarjetaForm
from django.http import HttpResponse
import datetime
from collections import defaultdict
from decimal import Decimal

def lista_operaciones(request):
    operaciones = OperacionTarjeta.objects.all()
    pagos_mensuales = calcular_pagos_mensuales()
    return render(request, 'gestor_tarjetas/lista_operaciones.html', {
        'operaciones': operaciones,
        'pagos_mensuales': pagos_mensuales
    })


def nueva_operacion(request):
    if request.method == 'POST':
        form = OperacionTarjetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('lista_operaciones')
        
    else:
        form = OperacionTarjetaForm()

    return render(request, 'gestor_tarjetas/nueva_operacion.html', {'form': form})


def home(request):
    return HttpResponse("Bienvenido a CrediTrack")


def calcular_pagos_mensuales():
    operaciones = OperacionTarjeta.objects.all()
    pagos_por_mes = defaultdict(float)  # Inicializa con float

    for operacion in operaciones:
        mes_año = operacion.fecha_operacion.strftime("%Y-%m")  # Formato año-mes
        pagos_por_mes[mes_año] += float(operacion.monto)  # Convierte el monto a float y lo suma

    return pagos_por_mes




def vista_proyeccion(request):
    pagos_mensuales = calcular_pagos_mensuales()
    return render(request, 'gestor_tarjetas/lista_operaciones.html', {'pagos_mensuales': pagos_mensuales })