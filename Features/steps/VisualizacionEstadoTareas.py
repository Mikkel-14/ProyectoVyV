from diagrama_gantt.models import Proyecto, Tarea
from behave import *
from diagrama_gantt.views import acceso_tareas_guard
from django.http import HttpRequest
from django.shortcuts import redirect
use_step_matcher("re")


@step("que se ingresa a un proyecto sin tareas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Se crea un proyecto sin tareas
    context.proyecto = Proyecto(nombre_proyecto="Proyecto sin tareas")
    context.proyecto.save()
    assert not context.proyecto.tieneTareas()


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
    context.tarea = Tarea(nombre_tarea = nombre_tarea)


@step("la fecha de inicio de la tarea sea (?P<fecha_inicial>.+)")
def step_impl(context, fecha_inicial):
    """
    :type context: behave.runner.Context
    :type fecha_inicial: str
    """
    context.tarea.fecha_inicial = fecha_inicial


@step("la fecha límite de la tarea sea (?P<fecha_limite>.+)")
def step_impl(context, fecha_limite):
    """
    :type context: behave.runner.Context
    :type fecha_limite: str
    """
    context.tarea.fecha_limite = fecha_limite


@step("la fecha actual del sistema sea (?P<fecha_actual>.+)")
def step_impl(context, fecha_actual):
    """
    :type context: behave.runner.Context
    :type fecha_actual: str
    """
    context.fecha_actual = fecha_actual


@step("el responsable marcó la culminación de la tarea con (?P<esta_completado>.+)")
def step_impl(context, esta_completado):
    """
    :type context: behave.runner.Context
    :type esta_completado: str
    """
    context.tarea.esta_completado = esta_completado


@step(
    "se estableció que una tarea en progreso tiene el estado crítico si faltan 7 días o menos hasta su (?P<fecha_limite>.+)")
def step_impl(context, fecha_limite):
    """
    :type context: behave.runner.Context
    :type fecha_limite: str
    """
    raise NotImplementedError(
        u'STEP: Y se estableció que una tarea en progreso tiene el estado crítico si faltan 7 días o menos hasta su <fecha_limite>')


@step("la tarea tendrá el estado (?P<estado>.+)")
def step_impl(context, estado):
    """
    :type context: behave.runner.Context
    :type estado: str
    """
    raise NotImplementedError(u'STEP: Entonces la tarea tendrá el estado <estado>')


@step("se mostrará la tarea en el diagrama de Gannt con el color (?P<color_estado>.+)")
def step_impl(context, color_estado):
    """
    :type context: behave.runner.Context
    :type color_estado: str
    """
    raise NotImplementedError(u'STEP: Y se mostrará la tarea en el diagrama de Gannt con el color <color_estado>')