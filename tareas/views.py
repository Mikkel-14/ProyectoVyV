from django.shortcuts import render, redirect
from diagrama_gantt.models import Tarea
from proyectos.models import Proyecto
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import IngresoTarea
from django.forms.models import model_to_dict
from datetime import datetime, timedelta


def tarea_contenida_en_proyecto_guard(id_proyecto, tarea):
    return id_proyecto == tarea.proyecto_id


@login_required(login_url='login')
def crear_tarea(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    # Si el usuario no tiene permisos para crear tareas se redirige
    if not request.user.has_perm('diagrama_gantt.add_tarea'):
        return redirect('gantt', id_proyecto)
    if request.method == 'POST':
        formulario = IngresoTarea(request.POST)
        if formulario.is_valid():
            nombre_tarea = formulario.cleaned_data['nombre_tarea']
            descripcion = formulario.cleaned_data['descripcion']
            fecha_inicial = formulario.cleaned_data['fecha_inicial']
            fecha_limite = formulario.cleaned_data['fecha_limite']
            # Creamos la tarea en la BD
            nueva_tarea = Tarea(
                nombre_tarea=nombre_tarea,
                descripcion=descripcion,
                fecha_inicial=fecha_inicial,
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
            'proyecto': proyecto,
            'editable': False,
            'hoy': 'min:{}'.format(datetime.today().date().strftime('%Y-%m-%d')),
            'manana': 'min:{}'.format((datetime.today() + timedelta(days=1)).date().strftime('%Y-%m-%d')),
        }
        return render(request, 'crear_tarea.html', data)


@login_required(login_url='login')
def ver_tarea(request, id_proyecto, id_tarea):

    # TODO: Guarda para que no acceda a un proyecto que no le corresponda

    proyecto = Proyecto.objects.get(id=id_proyecto)
    # Si el usuario no tiene permisos para crear tareas se redirige
    if not request.user.has_perm('diagrama_gantt.view_tarea'):
        return redirect('gantt', id_proyecto)
    tarea = Tarea.objects.get(id=id_tarea)
    if tarea_contenida_en_proyecto_guard(id_proyecto, tarea):
        data = {
            'tarea': tarea,
            'proyecto': proyecto,
        }
        return render(request, 'ver_tarea.html', data)
    else:
        raise Http404(f"Tarea no encontrada en el proyecto {proyecto.nombre_proyecto}")


@login_required(login_url='login')
def editar_tarea(request, id_proyecto, id_tarea):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    tarea = Tarea.objects.get(id=id_tarea)
    # Si el usuario no tiene permisos para crear tareas se redirige
    if not request.user.has_perm('diagrama_gantt.change_tarea'):
        return redirect('gantt', id_proyecto)
    
    if request.method == 'POST':
        formulario = IngresoTarea(request.POST)
        if formulario.is_valid():
            nombre_tarea = formulario.cleaned_data['nombre_tarea']
            descripcion = formulario.cleaned_data['descripcion']
            fecha_inicial = formulario.cleaned_data['fecha_inicial']
            fecha_limite = formulario.cleaned_data['fecha_limite']
            # Creamos la tarea en la BD
            tarea.nombre_tarea = nombre_tarea
            tarea.descripcion = descripcion
            tarea.fecha_inicial = fecha_inicial
            tarea.fecha_limite = fecha_limite
            tarea.save()
            return redirect('gantt', proyecto.id)
    else:
        if tarea_contenida_en_proyecto_guard(id_proyecto, tarea):
            valores_iniciales = model_to_dict(tarea)
            valores_iniciales['fecha_inicial'] = str(valores_iniciales['fecha_inicial'])
            valores_iniciales['fecha_limite'] = str(valores_iniciales['fecha_limite'])
            formulario = IngresoTarea(initial=valores_iniciales)
            data = {
                'form': formulario,
                'proyecto': proyecto,
                'tarea': tarea,
                'editable': True,
            }
            return render(request, 'crear_tarea.html', data)
        else:
            raise Http404(f"Tarea no encontrada en el proyecto {proyecto.nombre_proyecto}")


@login_required(login_url='login')
def eliminar_tarea(request, id_proyecto, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)
    # Si el usuario no tiene permisos para crear tareas se redirige
    if request.user.has_perm('diagrama_gantt.delete_tarea') and tarea_contenida_en_proyecto_guard(id_proyecto, tarea):
        tarea.delete()
    return redirect('gantt', id_proyecto)
    
        
    