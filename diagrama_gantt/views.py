from django.shortcuts import render
from diagrama_gantt.models import Proyecto, Tarea, Estado


# Create your views here.
def index(request):
    #TODO Definir a que proyecto se hace referencia
    proyectoID = 1

    proyecto = Proyecto.objects.get(id=proyectoID)
    tareas = Tarea.objects.filter(proyecto=proyectoID)
    #'tareas': tareas
    return render(request, 'diagrama_gantt.html',{'proyecto': proyecto, 'tareas': tareas})
