from django.shortcuts import render, redirect
from proyectos.models import Proyecto, ProyectoUsuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='login')
def acceso_proyectos_guard(request):
    usuario = request.user
    if ProyectoUsuario.tiene_proyectos(usuario=usuario):
        return index(request)
    if request.user.has_perm('proyectos.add_proyecto'):
        return redirect('crearProyecto')
    return HttpResponse(status=204)


def crear_proyecto(request):
    pass


@login_required(login_url='login')
def index(request):
    usuario = request.user
    listaProyectos = ProyectoUsuario.obtener_proyectos(usuario=usuario)
    data = {
        'proyectos': listaProyectos,
    }
    return render(request, 'ver_proyectos.html', data)
