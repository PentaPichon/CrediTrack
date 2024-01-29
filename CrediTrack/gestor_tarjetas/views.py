from django.shortcuts import render, redirect, get_object_or_404
from .models import OperacionTarjeta, Calendario
from .forms import OperacionTarjetaForm
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
import calendar
from dateutil.relativedelta import relativedelta
import locale
from django.utils.timezone import make_aware
from datetime import datetime, timedelta
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required


def calcular_pagos_mensuales(usuario):
    locale.setlocale(locale.LC_ALL, 'es')
    fecha_actual = make_aware(datetime.now())
    un_año_despues = fecha_actual + timedelta(days=365)

    creditos = Calendario.objects.filter(
        operacion_id__usuario=usuario,
        fecha_vencimiento__gte=fecha_actual,
        fecha_vencimiento__lte=un_año_despues
    ).annotate(
        año=ExtractYear('fecha_vencimiento'),
        mes=ExtractMonth('fecha_vencimiento')
    ).values(
        'año','mes'
    ).annotate(
        total_credito=Sum('monto_cuota')
    ).order_by('año','mes')

    suscripciones = OperacionTarjeta.objects.filter(
        tipo_operacion='SUSCRIPCION',
        usuario=usuario,
        fecha_operacion__lt=un_año_despues
    )

    resumen = {(fecha_actual.year + m // 12, (fecha_actual.month + m - 1) % 12 + 1): 0 for m in range(0, 12)}

    for credito in creditos:
        resumen[(credito['año'], credito['mes'])] += credito['total_credito']

    for s in suscripciones:
        for m in range(0, 12):
            año, mes = fecha_actual.year + m // 12, (fecha_actual.month + m - 1) % 12 + 1
            resumen[(año, mes)] += s.monto

    resumen_lista = [(año, _(calendar.month_name[mes]), total) for (año, mes), total in resumen.items()]


    return resumen_lista
    

@login_required
def nueva_operacion(request):
    if request.method == 'POST':
        form = OperacionTarjetaForm(request.POST, usuario=request.user)
        if form.is_valid():
            operacion = form.save(commit=False)
            operacion.usuario =request.user
            operacion.save()

            if operacion.tipo_operacion == 'CUOTA':
                for n in range (operacion.cantidad_cuotas):
                    monto_cuota = operacion.monto / operacion.cantidad_cuotas
                    fecha_vencimiento = operacion.fecha_operacion + relativedelta(months=+n)
                    Calendario.objects.create(
                        operacion_id=operacion,
                        numero_cuota=n+1,
                        monto_cuota=monto_cuota,
                        fecha_vencimiento=fecha_vencimiento,
                        concepto=operacion.concepto
                    )

            return redirect ('lista_operaciones')
    
        
    else:
        form = OperacionTarjetaForm()

    return render(request, 'gestor_tarjetas/nueva_operacion.html', {'form': form})


#########   DE AQUI PARA ABAJO ESTA BIEN; NO MODIFICAR!  ######### 

@login_required
def lista_operaciones(request):
    operaciones_cuotas = OperacionTarjeta.objects.filter(tipo_operacion='CUOTA').filter(usuario=request.user)
    operaciones_suscripcion = OperacionTarjeta.objects.filter(tipo_operacion='SUSCRIPCION').filter(usuario=request.user)
   
    return render(request, 'gestor_tarjetas/lista_operaciones.html', {
        'operaciones_cuotas': operaciones_cuotas,
        'operaciones_suscripcion' : operaciones_suscripcion,
        
    })

@login_required
def resumen_view(request):
    resumen = calcular_pagos_mensuales(request.user)
    return render(request, 'gestor_tarjetas/resumen.html', {'resumen': resumen})


def editar_operacion(request, id):
    operacion = get_object_or_404(OperacionTarjeta, id=id)
    if request.method == 'POST':
        form = OperacionTarjetaForm(request.POST, instance=operacion)
        if form.is_valid():
            form.save()

            Calendario.objects.filter(operacion_id=operacion).delete()
            if operacion.tipo_operacion == 'CUOTA':
                for n in range(operacion.cantidad_cuotas):
                    monto_cuota = operacion.monto / operacion.cantidad_cuotas
                    fecha_vencimiento = operacion.fecha_operacion + relativedelta(months=+n)
                    Calendario.objects.create(
                        operacion_id=operacion,
                        numero_cuota=n+1,
                        monto_cuota=monto_cuota,
                        fecha_vencimiento=fecha_vencimiento,
                        concepto=operacion.concepto
                    )

            return redirect ('lista_operaciones')
    else:
        print("Fecha de operacion:", operacion.fecha_operacion)
        form = OperacionTarjetaForm(instance=operacion)

    return render(request, 'gestor_tarjetas/editar_operacion.html', {'form':form})

def eliminar_operacion(request, id):
    operacion = get_object_or_404(OperacionTarjeta, id=id)
    if request.method == 'POST':
        operacion.delete()
        return redirect('lista_operaciones')

def confirmar_eliminacion(request, id):
    operacion = get_object_or_404(OperacionTarjeta, id=id)
    return render (request, 'gestor_tarjetas/confirmar_eliminacion.html', {'operacion':operacion})



