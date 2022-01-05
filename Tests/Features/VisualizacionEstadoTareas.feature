# Created by joset at 12/18/2021
#language: es
Característica: [CA4] Visualización del estado de tareas
  Como administrador del proyecto deseo identificar las tareas que están atrasadas, pendientes,
  en progreso y finalizadas, para evitar que el proyecto se retrase.

  Escenario: No existen tareas
    Dado que no existen tareas
    Cuando se presente el diagrama de Gantt
    Entonces se mostrará el mensaje "No existen tareas para mostrar" al usuario
    Y se mostrará un botón para "Crear una nueva tarea"

  Esquema del escenario: Existen tareas
    Dado que existe la tarea <nombre_tarea> tiene un estado <estado>
    Cuando se presente el diagrama de Gantt
    Entonces la tarea se coloreará de <color_estado>
    Y la tarea tendrá una etiqueta con el mensaje <mensaje_estado>

    Ejemplos:
      | nombre_tarea                  | estado      | color_estado | mensaje_estado |
      | Elicitación de requerimientos | Pendiente   | celeste      | Pendiente      |
      | Diseño de alto nivel          | Completado  | verde        | Completado     |
      | Implementación del software   | En progreso | amarillo     | En progreso    |
      | Diseño del plan de pruebas    | Atrasado    | naranja      | Atrasado       |