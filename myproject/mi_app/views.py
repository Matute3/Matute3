from django.shortcuts import render, redirect
from .models import Cliente, Producto, Pedido
from .forms import ClienteForm, ProductoForm, PedidoForm


# Vista para agregar clientes
def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_cliente')
    else:
        form = ClienteForm()
    return render(request, 'mi_app/agregar_cliente.html', {'form': form})


# Vista para agregar productos
def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')
    else:
        form = ProductoForm()
    return render(request, 'mi_app/agregar_producto.html', {'form': form})
