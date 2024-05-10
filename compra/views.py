from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from compra.models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm


def home(request):
    return render(request, 'compra/index.html')


#READ
# vista para el listado productos:
@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'compra/listado-productos.html', {'productos':productos})


# vista para el listado proveedores:
@login_required
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'compra/listado-proveedores.html', {'proveedores': proveedores})
    

#eliminar 
@login_required
@permission_required('compra.delete_producto', raise_exception=True)
def eliminar_producto(request, id):
     producto = get_object_or_404(Producto, id=id)
     if request.method == "POST":
          producto.delete()
          return redirect(reverse('listado-productos'))
     

@login_required
@permission_required('compra.delete_proveedor')
def eliminar_proveedor(request, id):
     proveedor = get_object_or_404(Producto, id = id)
     if request.method == "POST":
          proveedor.delete()
          return redirect(reverse('listado-proveedores'))
     


@login_required
@permission_required('producto.add_producto', raise_exception=True)
def agregar_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save(commit=True)
            return redirect('listado-productos')
    else:
        producto_form = ProductoForm()
    return render(request, 'compra/form-productos.html', {'producto_form': producto_form})



@login_required
@permission_required('proveedor.add_proveedor', raise_exception=True)
def agregar_proveedor(request):
    if request.method == "POST":
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save(commit=True)
            return redirect('listado-proveedores')
    else:
        proveedor_form = ProveedorForm()
    return render(request, 'compra/form-proveedores.html', {'proveedor_form':proveedor_form})
    