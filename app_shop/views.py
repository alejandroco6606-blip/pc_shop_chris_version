from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca, Proveedor, Categoria
from .forms import ProductoForm, MarcaForm, ProveedorForm, CategoriaForm

# Vista (Read) y (Create) combinadas
def lista_productos(request):
    
    # Lógica de CREAR (si se envía el formulario)
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos') # Redirige a la misma página
    else:
        # Si es GET, crea un formulario vacío
        form = ProductoForm()

    # Lógica de LEER (se ejecuta siempre)
    productos = Producto.objects.all()
    
    # Prepara el "contexto" para la plantilla
    context = {
        'productos': productos,
        'form': form  # Pasa el formulario (vacío o con errores)
    }
    return render(request, 'productos/lista_productos.html', context)

# --- VISTA DE CREAR (Se mantiene por estructura) ---
# Esta vista ahora puede ser un simple render
# o redirigir a la principal si prefieres.
# La dejaremos funcional por si quieres acceder a /crear/ directamente.
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    # Apunta al HTML de creación
    return render(request, 'productos/crear_producto.html', {'form': form})

# --- ESTAS VISTAS NO CAMBIAN ---

# Editar producto (Update)
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

# Eliminar producto (Delete)
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'marcas/lista_marcas.html', {'marcas': marcas})

# 2. CREAR Marca (Create)
def crear_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_marcas')
    else:
        form = MarcaForm()
    return render(request, 'marcas/crear_marca.html', {'form': form})

# 3. EDITAR Marca (Update)
def editar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('lista_marcas')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'marcas/editar_marca.html', {'form': form})

# 4. ELIMINAR Marca (Delete)
def eliminar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('lista_marcas')
    return render(request, 'marcas/eliminar_marca.html', {'marca': marca})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/crear_proveedor.html', {'form': form})

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/editar_proveedor.html', {'form': form})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'proveedores/eliminar_proveedor.html', {'proveedor': proveedor})

# --- VISTAS PARA CATEGORÍA ---

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/crear_categoria.html', {'form': form})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/editar_categoria.html', {'form': form})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'categorias/eliminar_categoria.html', {'categoria': categoria})