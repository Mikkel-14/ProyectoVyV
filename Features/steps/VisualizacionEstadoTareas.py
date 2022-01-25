from diagrama_gantt.models import Proyecto, Tarea, Estado
from behave import *
from diagrama_gantt.views import acceso_tareas_guard
from django.http import HttpRequest
from django.shortcuts import redirect
from datetime import datetime
use_step_matcher("re")


@step("que se ingresa a un proyecto sin tareas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Se crea un proyecto sin tareas
    context.proyecto = Proyecto(nombre_proyecto="Proyecto sin tareas")
    context.proyecto.save()
    assert not context.proyecto.tiene_tareas()


@step("el sistema redirigirá al usuario a la ventana de creación de nueva tarea")
def step_impl(context):
    expected = redirect('crearTarea').url
    actual = acceso_tareas_guard(HttpRequest(), context.proyecto.id).url
    assert expected == actual


@step("que en el proyecto existe la tarea (?P<nombre_tarea>.+)")
def step_impl(context, nombre_tarea):
    """
    :type context: behave.runner.Context
    :type nombre_tarea: str
    """
    proyecto = Proyecto(nombre_proyecto="ProyectoA")
    proyecto.save()
    context.tarea = Tarea(proyecto=proyecto, nombre_tarea=nombre_tarea)


@step("la fecha de inicio de la tarea sea (?P<fecha_inicial>.+)")
def step_impl(context, fecha_inicial):
    """
    :type context: behave.runner.Context
    :type fecha_inicial: str
    """
    context.tarea.fecha_inicial = datetime.strptime(fecha_inicial, '%d-%m-%Y').date()


@step("la fecha límite de la tarea sea (?P<fecha_limite>.+)")
def step_impl(context, fecha_limite):
    """
    :type context: behave.runner.Context
    :type fecha_limite: str
    """
    context.tarea.fecha_limite = datetime.strptime(fecha_limite, '%d-%m-%Y').date()


@step("la fecha actual del sistema sea (?P<fecha_actual>.+)")
def step_impl(context, fecha_actual):
    """
    :type context: behave.runner.Context
    :type fecha_actual: str
    """
    context.fecha_actual = datetime.strptime(fecha_actual, '%d-%m-%Y').date()


@step("el responsable marcó la culminación de la tarea con (?P<esta_completado>.+)")
def step_impl(context, esta_completado):
    """
    :type context: behave.runner.Context
    :type esta_completado: str
    """
    context.tarea.esta_completado = esta_completado == 'True'
    context.tarea.save()


@step(
    "se estableció que una tarea en progreso tiene el estado crítico si faltan 7 días o menos hasta su ("
    "?P<fecha_limite>.+)")
def step_impl(context, fecha_limite):
    """
    :type context: behave.runner.Context
    :type fecha_limite: str
    """
    context.tipo_tarea = context.tarea.es_critica(fecha_actual=context.fecha_actual)


@step("la tarea tendrá el estado (?P<estado>.+)")
def step_impl(context, estado):
    """
    :type context: behave.runner.Context
    :type estado: str
    """
    assert context.tarea.obtener_estado(context.fecha_actual) == estado


@step("se mostrará la tarea en el diagrama de Gannt con el color (?P<color_estado>.+)")
def step_impl(context, color_estado):
    """
    :type context: behave.runner.Context
    :type color_estado: str
    """
    estado1 = Estado(nombre_estado='pendiente', color_estado='#7f8fa6')
    estado1.save()
    estado2 = Estado(nombre_estado='completado', color_estado='#4cd137')
    estado2.save()
    estado3 = Estado(nombre_estado='en-progreso', color_estado='#fbc531')
    estado3.save()
    estado4 = Estado(nombre_estado='crítico', color_estado='#e17055')
    estado4.save()
    estado5 = Estado(nombre_estado='atrasado', color_estado='#d63031')
    estado5.save()
    assert context.tarea.obtener_color(context.fecha_actual) == color_estado
