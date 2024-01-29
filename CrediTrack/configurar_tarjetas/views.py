from django.shortcuts import render, redirect, get_object_or_404
from gestor_tarjetas.models import ConfiguracionTarjeta
from django.contrib.auth.decorators import login_required
from .forms import ConfiguracionTarjetaForm


@login_required
def listar_tarjetas(request):
    tarjetas = ConfiguracionTarjeta.objects.filter(usuario=request.user)
    return render(request, 'configurar_tarjetas/listar_tarjetas.html', {'tarjetas': tarjetas})


@login_required
def agregar_tarjeta(request):
    if request.method == 'POST':
        form = ConfiguracionTarjetaForm(request.POST)
        if form.is_valid():
            tarjeta = form.save(commit=False)
            tarjeta.usuario = request.user
            tarjeta.save()
            return redirect('listar_tarjetas')
    else:
        form = ConfiguracionTarjetaForm()
    return render(request, 'configurar_tarjetas/agregar_tarjeta.html', {'form': form})


@login_required
def editar_tarjeta(request, id):
    tarjeta = get_object_or_404(ConfiguracionTarjeta, id=id, usuario=request.user)
    if request.method == 'POST':
        form = ConfiguracionTarjetaForm(request.POST, instance=tarjeta)
        if form.is_valid():
            form.save()
            return redirect('listar_tarjetas')
    else:
        form = ConfiguracionTarjetaForm(instance=tarjeta)
    return render(request, 'configurar_tarjetas/editar_tarjeta.html', {'form': form})

@login_required
def eliminar_tarjeta(request, id):
    operacion = get_object_or_404(ConfiguracionTarjeta, id=id)
    if request.method == 'POST':
        operacion.delete()
        return redirect('listar_tarjetas')
    
def confirmar_eliminacion_tarjeta(request, id):
    tarjeta = get_object_or_404(ConfiguracionTarjeta, id=id)
    return render (request, 'configurar_tarjetas/confirmar_eliminacion_tarjeta.html', {'tarjeta':tarjeta})