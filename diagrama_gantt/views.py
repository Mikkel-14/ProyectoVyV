from datetime import timedelta, datetime
from django.shortcuts import render, redirect
from diagrama_gantt.models import Proyecto, Tarea
from django.db.models import Min, Max
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='login')
def acceso_tareas_guard(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    if proyecto.tiene_tareas():
        return index(request, id_proyecto)
    if request.user.has_perm('diagrama_gantt.add_tarea'):
        return redirect('crearTarea', id_proyecto)
    return HttpResponse(status=204)


@login_required(login_url='login')
def index(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    tareas = Tarea.objects.filter(proyecto=id_proyecto)

    # El proyecto puede tener una fecha inicial y una de fin o ser calculadas???
    menor_fecha = Tarea.objects.all().aggregate(Min('fecha_inicial'))['fecha_inicial__min']
    mayor_fecha = Tarea.objects.all().aggregate(Max('fecha_limite'))['fecha_limite__max']

    diferencia_dias = mayor_fecha - menor_fecha

    # La menor fecha es la base
    lista_fechas = [menor_fecha + timedelta(days=x) for x in range(diferencia_dias.days + 1)]

    def obtener_colspan_meses(lista_fechas):  
        index = 0
        contador = 0
        meses_colspan = []
        while index < len(lista_fechas):
            if lista_fechas[index].day == 1:
                meses_colspan.append({"fecha": lista_fechas[index-1], "colspan": contador})
                contador = 1
            else:
                contador += 1
            index += 1
        meses_colspan.append({"fecha":lista_fechas[-1], "colspan": contador})
        return meses_colspan   

    meses_info = obtener_colspan_meses(lista_fechas)

    # Total semanas
    semanas = diferencia_dias.days / 7

    lunes_anterior = menor_fecha - timedelta(days=menor_fecha.weekday())
    domingo_siguiente = mayor_fecha + timedelta(days=6 - mayor_fecha.weekday())

    diferencia = domingo_siguiente - lunes_anterior
    semanas = (diferencia.days / 7) - 2

    datos_tareas = [
        {'tarea': tarea,
         'duracion': (tarea.fecha_limite - tarea.fecha_inicial).days + 1,
         'dia_offset': (tarea.fecha_inicial - menor_fecha).days,
         'post_offset': (mayor_fecha - tarea.fecha_limite).days,
         'color_estado': "background-color:" + tarea.obtener_color(),
         'estado': tarea.obtener_estado()}
        for tarea in tareas
    ]

    data = {
        'proyecto': proyecto,
        'tareas': datos_tareas,
        'menor_fecha': menor_fecha,
        'mayor_fecha': mayor_fecha,
        'lista_fechas': lista_fechas,
        'colspan_semana_inicio': 7 - menor_fecha.weekday(),
        'colspan_semana_final': mayor_fecha.weekday() + 1,
        'meses_info': meses_info,
        'semanas_intermedias': range(2, int(semanas) + 3),
        'hoy': datetime.now().date()
    }

    def es_hoy(fecha):
        return fecha == datetime.now().date()

    return render(request, 'diagrama_gantt.html', data)
