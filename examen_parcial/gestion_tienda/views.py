from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import datosUsuario,tareasInformacion
from datetime import date
import datetime
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')   
        usuarioInfo = authenticate(request,username=nombreUsuario,password=contraUsuario)
        if usuarioInfo is not None:
            login(request,usuarioInfo)
            if usuarioInfo.datosusuario.RolUsuario=='ADMINISTRADOR':
                return HttpResponseRedirect(reverse('gestion_tienda:gestionUsuarios'))
            else:
                return HttpResponseRedirect(reverse('gestion_tienda:verUsuario',kwargs={'ind':usuarioInfo.id}))
        else:
            return HttpResponseRedirect(reverse('gestion_tienda:index'))
    return render(request,'ingresoUsuario.html')
@login_required(login_url='http://127.0.0.1:8000')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('gestion_tienda:index'))

@login_required(login_url='http://127.0.0.1:8000')
def gestionUsuarios(request):
    if request.user.datosusuario.RolUsuario=='ADMINISTRADOR':
        if request.method=='POST':
            usernameUsuario=request.POST.get('usernameUsuario')
            nombreUsuario=request.POST.get('nombreUsuario')
            apellidoUsuario=request.POST.get('apellidoUsuario')
            emailUsuario=request.POST.get('emailUsuario')
            contraUsuario=request.POST.get('contraUsuario')
            rolUsuario=request.POST.get('rolUsuario')
            celularUsuario=request.POST.get('celularUsuario')
            usuarioNuevo=User.objects.create(
                username=usernameUsuario,
                email=emailUsuario
            )
            usuarioNuevo.set_password(contraUsuario)
            usuarioNuevo.first_name=nombreUsuario
            usuarioNuevo.last_name=apellidoUsuario
            usuarioNuevo.is_staff=True
            usuarioNuevo.save()
            datosUsuario.objects.create(
                user=usuarioNuevo,
                Nombre=nombreUsuario,
                Apellido=apellidoUsuario,
                Email=emailUsuario,
                Username=usernameUsuario,
                Contrasena=contraUsuario,
                RolUsuario=rolUsuario,
                NoCelular=celularUsuario
            )
            return HttpResponseRedirect(reverse('gestion_tienda:gestionUsuarios'))
        return render(request,'gestionUsuarios.html',{
        'usuariosTotales':User.objects.all().order_by('id')           
        })
    else:
        return HttpResponseRedirect(reverse('gestion_tienda:verUsuario',kwargs={'ind':request.user.id}))
def eliminarUsuario(request,ind):
    usuarioEliminar = User.objects.get(id=ind)
    datosUsuario.objects.get(user=usuarioEliminar).delete()
    usuarioEliminar.delete()
    return HttpResponseRedirect(reverse('gestion_tienda:gestionUsuario'))
def verUsuario(request, ind):
    usuarioInfo=User.objects.get(id=ind)
    tareasUsuario=tareasInformacion.objects.filter(usuarioRelacionado=usuarioInfo).order_by('id')
    return render(request,'informacionUsuario.html',{
        'usuarioInfo' : usuarioInfo,
        'tareasUsuario': tareasUsuario,
    })
def nuevaTarea(request,ind):
    if request.method=='POST':
        usuarioRelacionado=User.objects.get(id=ind)
        fechaInicio=request.POST.get('fechaInicio')
        fechaFin=request.POST.get('fechaFin')
        descripcionTarea=request.POST.get('descripcionTarea')
        fechaSeparada= fechaInicio.split('-')
        ini_dia=int(fechaSeparada[2])
        ini_mes=int(fechaSeparada[1])
        ini_ano=int(fechaSeparada[0])
        fechaSeparada= fechaFin.split('-')
        fin_dia=int(fechaSeparada[2])
        fin_mes=int(fechaSeparada[1])
        fin_ano=int(fechaSeparada[0])
        fechaInicioRegistro=datetime.datetime(ini_ano,ini_mes,ini_dia)
        fechaFinRegistro=datetime.datetime(fin_ano,fin_mes,fin_dia)
        tareasInformacion.objects.create(
            fechaInicio=fechaInicioRegistro,fechaFin=fechaFinRegistro,usuarioRelacionado=usuarioRelacionado,descripcionTarea=descripcionTarea
        )
        return HttpResponseRedirect(reverse('gestion_tienda:verUsuario',kwargs={'ind':ind}))