from diagrama_gantt.models import Proyecto, Tarea
from behave import *

use_step_matcher("re")

proyecto = None
tareasProyecto = None


@step("que se ingresa a un proyecto dado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # El proyecto "Proyecto 2" con id = 2 no tiene tareas
    proyecto = Proyecto.objects.get(id=2)


@step("no existen tareas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    tareasProyecto = Tarea.objects.filter(proyecto_id = proyecto.id).count()


@step("el sistema redirigirá al usuario a la ventana de creación de nueva tarea")
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Entonces el sistema redirigirá al usuario a la ventana de creación de nueva tarea')