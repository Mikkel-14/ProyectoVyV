# Created by joset at 12/18/2021
#language: es
@CA4
Característica: [CA4] Visualización del estado de tareas
  Como administrador del proyecto deseo identificar las tareas que están atrasadas, pendientes,
  en progreso y finalizadas, para evitar que el proyecto se retrase.

  Escenario: No existen tareas
    Dado que se ingresa a un proyecto sin tareas
    Entonces el sistema redirigirá al usuario a la ventana de creación de nueva tarea

  Esquema del escenario: Existen tareas
    Dado que en el proyecto existe la tarea <nombre_tarea>
    Cuando la fecha de inicio de la tarea sea <fecha_inicial>
    Y la fecha límite de la tarea sea <fecha_limite>
    Y la fecha actual del sistema sea <fecha_actual>
    Y el responsable marcó la culminación de la tarea con <esta_completado>
    Y se estableció que una tarea en progreso tiene el estado crítico si faltan 7 días o menos hasta su <fecha_limite>
    Entonces la tarea tendrá el estado <estado>
    Y se mostrará la tarea en el diagrama de Gannt con el color <color_estado>

    Ejemplos:
      | nombre_tarea                  | estado      | color_estado | fecha_inicial | fecha_actual | fecha_limite | esta_completado |
      | Elicitación de requerimientos | pendiente   | #7f8fa6      | 10-02-2022    | 10-01-2022   | 10-03-2022   | False           |
      | Diseño de alto nivel          | completado  | #4cd137      | 23-11-2021    | 10-01-2022   | 12-12-2021   | True            |
      | Implementación del software   | en-progreso | #fbc531      | 06-12-2021    | 10-01-2022   | 31-01-2022   | False           |
      | Plan de proyecto              | crítico     | #e17055      | 06-12-2021    | 10-01-2022   | 12-01-2022   | False           |
      | Diseño del plan de pruebas    | atrasado    | #d63031      | 13-11-2021    | 10-01-2022   | 10-12-2021   | False           |