from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('operaciones/', views.lista_operaciones, name='lista_operaciones'),
    path('operacion/nueva/', views.nueva_operacion, name='nueva_operacion'),
    path('operacion/editar/<int:id>', views.editar_operacion, name='editar_operacion'),
    path('operacion/confirmacion/<int:id>', views.confirmar_eliminacion, name='confirmar_eliminacion'),
    path('operacion/eliminar/<int:id>', views.eliminar_operacion, name='eliminar_operacion'),
    path('resumen/', views.resumen_view, name='resumen'),
]
