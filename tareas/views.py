from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def crearTarea(request):
    return HttpResponse("Crea tareas")