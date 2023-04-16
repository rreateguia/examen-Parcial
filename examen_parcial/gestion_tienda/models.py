from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class datosUsuario(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Nombre = models.CharField(default='NOMBRE',max_length=30)
    Apellido =models.CharField(default='APELLIDO',max_length=30)
    Email = models.EmailField()
    Username = models.CharField(default='USERNAME',max_length=30)
    Contrasena = models.CharField(default='PASSWORD',max_length=30)
    RolUsuario = models.CharField(default='ROL',max_length=512)
    NoCelular = models.CharField(default='999999999',max_length=11)
    FechaIngreso = models.DateField(default=date.today)

class Producto(models.Model):
    NombreProducto=models.CharField(default='NOMBREPRODUCTO',max_length=30)
    Codigo=models.CharField(default='CODIGO',max_length=30)
    PrecioCompra=models.FloatField(default=0.00)
    PrecioVenta=models.FloatField(default=0.00)
    Usuario=models.ForeignKey(User,on_delete=models.CASCADE)

class tareasInformacion(models.Model):
    usuarioRelacionado=models.ForeignKey(User,on_delete=models.CASCADE)
    descripcionTarea=models.CharField(default='',max_length=512)
    fechaInicio=models.DateField(default=date.today)
    fechaFin=models.DateField(default=date.today)
    estadoTarea=models.CharField(default='PROCESO',max_length=30)