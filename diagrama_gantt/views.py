import datetime
from datetime import timedelta

from django.shortcuts import render
from diagrama_gantt.models import Proyecto, Tarea, Estado
from django.db.models import Min, Max


# Create your views here.
def index(request):
    #TODO Definir a que proyecto se hace referencia
    proyectoID = 1

    proyecto = Proyecto.objects.get(id=proyectoID)
    tareas = Tarea.objects.filter(proyecto=proyectoID)

    # El proyecto puede tener una fecha inicial y una de fin o ser calculadas???
    menor_fecha = Tarea.objects.all().aggregate(Min('fecha_inicial'))['fecha_inicial__min']
    mayor_fecha = Tarea.objects.all().aggregate(Max('fecha_limite'))['fecha_limite__max']

    diferencia_dias = mayor_fecha - menor_fecha

    # La menor fecha es la base
    lista_fechas = [menor_fecha + timedelta(days=x) for x in range(diferencia_dias.days + 1)]

    # Total semanas
    semanas = diferencia_dias.days /7

    lunes_anterior = menor_fecha - timedelta(days=menor_fecha.weekday())
    domingo_siguiente = mayor_fecha + timedelta(days= 6 - mayor_fecha.weekday())

    diferencia = domingo_siguiente - lunes_anterior
    semanas = (diferencia.days / 7) - 2

    datos_tareas = [
        {'tarea': tarea,
         'duracion': (tarea.fecha_limite - tarea.fecha_inicial).days + 1,
         'dia_offset': (tarea.fecha_inicial - menor_fecha).days,
         'post_offset': (mayor_fecha - tarea.fecha_limite).days}
        for tarea in tareas
    ]

    data = {
        'proyecto': proyecto,
        'tareas': datos_tareas,
        'menor_fecha': menor_fecha,
        'mayor_fecha': mayor_fecha,
        'lista_fechas': lista_fechas,
        'colspan_inicio': 7 - menor_fecha.weekday(),
        'colspan_final': mayor_fecha.weekday() + 1,
        'semanas_intermedias': range(2,int(semanas)+3)
    }

    return render(request, 'diagrama_gantt.html', data)

