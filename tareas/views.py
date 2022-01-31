from django.shortcuts import render, redirect
from django.http import HttpResponse
from diagrama_gantt.models import Proyecto, Tarea
from datetime import datetime, timedelta
from .forms import IngresoTarea

# Create your views here.
def crear_tarea(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
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

def ver_tarea(request, id_proyecto, id_tarea):
    return HttpResponse(f"Ver tarea {id_tarea}")