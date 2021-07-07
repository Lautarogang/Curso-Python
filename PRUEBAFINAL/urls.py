from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib import admin

app_name="Final"
urlpatterns = [
    path('',views.listar_productos,name="index" ),
    path('agregar',views.agregar_producto,name="nProducto" ),
    path('Acerca De',views.AcercaDe,name="AcercaDe"),
    path('modificar-producto/<id>/',views.modificar_producto,name="modificarP"),
    path('eliminar-producto/<id>/',views.eliminar_producto,name="eliminarP"),
    path('ver-producto/<id>/',views.verP,name="verP"),
    path('registro/',views.registro,name="registro"),
    path('busqueda/',views.busqueda,name="busquedaR"),
    path('carro',views.carro,name="Carro"),
]
