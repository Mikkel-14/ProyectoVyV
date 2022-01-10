# Created by Mahatma at 18/12/2021
# language: es
Característica: [CA1] Asignación de tareas
  Como administrador del proyecto deseo identificar el número de actividades
  asignadas a cada empleado para evitar la sobrecarga de trabajo.

  Escenario: Existen tareas asignadas
    Dado que existen tareas asignadas a los miembros del equipo
    Cuando se acceda al módulo de asignación de tareas
    Entonces se mostrará una lista de los miembros del equipo
    Y el número de tareas asignadas a cada uno
    Y el tiempo total en horas de las tareas asignadas

  Escenario: No existen tareas asignadas
    Dado que no existen tareas asignadas a los miembro del equipo
    Cuando se accede al módulo de asignación de tareas
    Entonces se mostrará el mensaje "No hay tareas asignadas a los miembros del equipo"
    Y se mostrará un botón con el mensaje "Asignar tareas"
