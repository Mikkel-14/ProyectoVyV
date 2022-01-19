# Created by Mahatma at 18/12/2021
# language: es
@CA3
Característica: [CA3] Compartición de completitud de tareas
  Como colaborador de un proyecto tengo que actualizar la completitud de mis tareas
  para que el sistema pueda marcar las tareas críticas

  Esquema del escenario: Existen nuevas tareas asignadas
    Dado que se me asignaron una o más tareas de un proyecto
    Cuando acceda a una tarea y marque su estado de completitud como <esta_completado>
    Entonces se actualizará el estado de completitud de la tarea en la base de datos a <esta_completado>

    Ejemplos:
      | esta_completado |
      | true            |
      | false           |