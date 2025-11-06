# app_orders/urls.py
from django.urls import path

app_name = 'app_orders'

from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('<int:pk>/', views.detalle_pedido, name='detalle_pedido'),
]