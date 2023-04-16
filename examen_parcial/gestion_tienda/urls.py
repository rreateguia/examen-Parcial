from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'gestion_tienda'
urlpatterns = [
    path('',views.index,name='index'),
    path('gestionUsuarios',views.gestionUsuarios,name='gestionUsuarios'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('eliminarUsuario/<str:ind>',views.eliminarUsuario,name='eliminarUsuario'),
    path('eliminarProducto/<str:ind>',views.eliminarProducto,name='eliminarProducto'),
    path('verUsuario/<str:ind>',views.verUsuario,name='verUsuario'),
    path('nuevoProducto/<str:ind>',views.nuevoProducto,name='nuevoProducto')
]