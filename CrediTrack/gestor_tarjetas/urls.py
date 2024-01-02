from django.urls import path
from . import views

urlpatterns = [
    path('operaciones/', views.lista_operaciones, name='lista_operaciones'),
    path('operacion/nueva/', views.nueva_operacion, name='nueva_operacion'),
]
