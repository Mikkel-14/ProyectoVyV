# Created by joset at 12/18/2021
#language: es
Característica: Visualización del estado de tareas
  Como administrador del proyecto deseo identificar las tareas que están atrasadas, pendientes,
  en progreso y finalizadas, para evitar que el proyecto se retrase.

  Escenario: No existen tareas
    Dado que no existen tareas
    Cuando se presente el diagrama de Gantt
    Entonces se mostrará el mensaje "No existen tareas para mostrar" al usuario
    Y se mostrará un botón para "Crear una nueva tarea"

  Escenario: Existen tareas
    Dado que existen las siguientes tareas
      | nombre_tarea                  | responsable | fecha_inicio | fecha_fin  |
      | Elicitacion de requerimientos | Santiago    | 18-12-2021   | 23-12-2021 |

    Cuando se presente el diagrama de Gantt
    Entonces cada tarea se