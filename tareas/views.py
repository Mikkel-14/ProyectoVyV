from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from diagrama_gantt.models import Tarea
from proyectos.models import Proyecto
from django.contrib.auth.decorators import login_required
from .forms import IngresoTarea


# Create your views here.
@login_required(login_url='login')
def crear_tarea(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    # Si el usuario no tiene permisos para crear tareas se redirige
    if not request.user.has_perm('diagrama_gantt.add_tarea'):
        return redirect('gantt', proyecto.id)
    if request.method == 'POST':
        formulario = IngresoTarea(request.POST)
        if formulario.is_valid():
            nombre_tarea = formulario.cleaned_data['nombre_tarea']
            descripcion = formulario.cleaned_data['descripcion']
            fecha_inicio = formulario.cleaned_data['fecha_inicio']
            fecha_limite = formulario.cleaned_data['fecha_limite']
            # Creamos la tarea en la BD
            nueva_tarea = Tarea(
                nombre_tarea=nombre_tarea,
                descripcion=descripcion,
                fecha_inicial=fecha_inicio,
                fecha_limite=fecha_limite,
                proyecto=proyecto,
                esta_completado=False
            )
            nueva_tarea.save()
            return redirect('gantt', proyecto.id)
    else:
        form = IngresoTarea()
        data = {
            'form': form,
            'proyecto': proyecto
        }
        return render(request, 'crear_tarea.html', data)


@login_required(login_url='login')
def ver_tarea(request, id_proyecto, id_tarea):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    tarea = Tarea.objects.get(id=id_tarea)
    if id_proyecto == tarea.proyecto_id:
        data = {
            'tarea': tarea,
            'proyecto': proyecto
        }
        return render(request, 'ver_tarea.html', data)
    else:
        raise Http404(f"Tarea no encontrada en el proyecto {proyecto.nombre_proyecto}")
