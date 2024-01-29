from django.urls import path
from . import views  

urlpatterns = [
    path('tarjetas/', views.listar_tarjetas, name='listar_tarjetas'),
    path('tarjetas/agregar/', views.agregar_tarjeta, name='agregar_tarjeta'),
    path('tarjetas/editar/<int:id>/', views.editar_tarjeta, name='editar_tarjeta'),
    path('tarjetas/confirmacion/<int:id>/', views.confirmar_eliminacion_tarjeta , name='confirmar_eliminacion_tarjeta'),
    path('tarjetas/eliminar/<int:id>', views.eliminar_tarjeta, name='eliminar_tarjeta'),
]


