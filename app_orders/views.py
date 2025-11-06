# app_orders/views.py
from django.shortcuts import render

def lista_pedidos(request):
    pedidos = []  # reemplaza por consulta real al modelo Pedido
    return render(request, 'app_orders/lista_pedidos.html', {'pedidos': pedidos})

def detalle_pedido(request, pk):
    pedido = None  # reemplaza por get_object_or_404(Pedido, pk=pk)
    return render(request, 'app_orders/detalle_pedido.html', {'pedido': pedido})