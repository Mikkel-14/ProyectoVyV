from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def crear_tarea(request, id_proyecto):
    return HttpResponse("Crea tareas")

def ver_tarea(request, id_proyecto, id_tarea):
    return HttpResponse(f"Ver tarea {id_tarea}")