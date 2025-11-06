from django.db import models

# --- MODELOS INDEPENDIENTES ---
class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True) # Opcional
    email = models.EmailField(blank=True)                  # Opcional
    def __str__(self): return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True) # Opcional
    def __str__(self): return self.nombre

# --- MODELO PRINCIPAL ---
class Producto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    # Nueva relación: Un producto tiene UNA categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='productos', null=True, blank=True)
    # Usamos ON_DELETE=SET_NULL para que si borras una categoría, los productos no se borren, solo queden "sin categoría".

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self): return self.nombre

