from django.shortcuts import render, redirect
from proyectos.models import Proyecto, ProyectoUsuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ProyectoVerificacion.views import acceso_proyecto_guard
from .forms import IngresoProyecto
from django.contrib.auth.models import User


@login_required(login_url='login')
def acceso_proyectos_guard(request):
    usuario = request.user
    if ProyectoUsuario.tiene_proyectos(usuario=usuario):
        return index(request)
    if request.user.has_perm('proyectos.add_proyecto'):
        return redirect('crearProyecto')
    return HttpResponse(status=204)


@login_required(login_url='login')
def crear_proyecto(request):
    # Si el usuario no tiene permisos para eliminar dicho proyecto
    if not request.user.has_perm('proyectos.add_proyecto'):
        return redirect('verProyectos')
    if request.POST:
        formulario = IngresoProyecto(request.POST)
        if formulario.is_valid():
            nombre_proyecto = formulario.cleaned_data['nombre_proyecto']
            colaboradores_proyecto = formulario.cleaned_data['colaboradores_proyecto']
            # Se crea el proyecto
            proyecto = ProyectoUsuario.crear_proyecto(nombre_proyecto=nombre_proyecto, usuario=request.user)
            # Se agregan los colaboradores
            usuarios = list(map(lambda id: User.objects.get(id=int(id)), colaboradores_proyecto))
            for usuario in usuarios:
                proyecto.agregar_colaborador(usuario)
            return redirect('verProyectos')
    else:
        formulario = IngresoProyecto()
        return render(request,'crear_proyecto.html',{'form': formulario})


@login_required(login_url='login')
def index(request):
    usuario = request.user
    listaProyectos = ProyectoUsuario.obtener_proyectos(usuario=usuario)
    colaboradores = list(map(lambda proy: ProyectoUsuario.numero_colaboradores(proy.id) ,listaProyectos))
    datosProyectos = [(proy, num_colab) for proy, num_colab in zip(listaProyectos, colaboradores)]
    data = {
        'proyectos': listaProyectos,
        'datosProyectos': datosProyectos,
    }
    return render(request, 'ver_proyectos.html', data)


@login_required(login_url='login')
def eliminar_proyecto(request, id_proyecto):
    # Si el usuario no tiene permisos para eliminar dicho proyecto
    if request.user.has_perm('proyectos.delete_proyecto') and acceso_proyecto_guard(request, id_proyecto):
        proyecto = Proyecto.objects.get(id=id_proyecto)
        proyecto.delete()
    return redirect('verProyectos')

