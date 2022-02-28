from django.shortcuts import render, redirect
from proyectos.models import Proyecto, ProyectoUsuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
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


def index(request):
    pass