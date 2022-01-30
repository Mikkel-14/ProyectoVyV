from django.shortcuts import render
from django.http import HttpResponse
from diagrama_gantt.models import Proyecto
from datetime import datetime, timedelta
from .forms import IngresoTarea

# Create your views here.
def crear_tarea(request, id_proyecto):
    if request.method == 'GET':
        proyecto = Proyecto.objects.get(id=id_proyecto)
        fecha_hoy = datetime.now().date()
        form = IngresoTarea()
    data = {
        'form': form,
        'proyecto': proyecto,
        'fecha_hoy': fecha_hoy,
        'fecha_siguiente': fecha_hoy + timedelta(days=1)    # TODO JavaScript
    }
    return render(request, 'crear_tarea.html', data)

def ver_tarea(request, id_proyecto, id_tarea):
    return HttpResponse(f"Ver tarea {id_tarea}")