from django.urls import path
from .views import home, listar_productos, listar_proveedores, agregar_proveedor, agregar_producto


#app_name = 'compra'

urlpatterns = [
    path('home/', home, name = 'home'),
    path('listado-productos/', listar_productos, name = 'listado-productos'),
    path('listado-proveedores/', listar_proveedores, name = 'listado-proveedores'), 
    path('alta-proveedor/', agregar_proveedor, name = 'alta-proveedor'),
    path('agregar-producto/', agregar_producto, name = 'agregar-producto'),
]