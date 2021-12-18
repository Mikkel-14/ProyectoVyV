# Created by Mahatma at 18/12/2021
# language: es
Característica: Calculadora de costos de proyecto
  Como administrador del proyecto quiero obtener un cálculo automático del costo total del proyecto
  o grupos de tareas en base a los recursos y el tiempo, para poder verificar que el proyecto se
  encuentre dentro del presupuesto.

  Esquema del escenario: Costo de una tarea
    Dado que la tarea <tarea> requiere del recurso <recurso> con un costo por hora de <costo_hora> por <horas> horas
    Cuando se acceda al módulo de calculadora de costos
    Entonces se podrá visualizar un costo total de <resultado>
    Ejemplos:
      | tarea                         | costo_hora | recurso                     | horas | resultado |
      | Elicitación de requerimientos | 15.00      | Ingeniero de requerimientos | 24    | 360.00    |
      | Diseño de alto nivel          | 20.00      | Arquitecto de software      | 30    | 600.00    |

  Escenario: Costo del proyecto
    Dado que se tienen los costos calculados de cada tarea de un proyecto
    Cuando se acceda al módulo de información general del proyecto
    Entonces se podrá visualizar el costo total del proyecto como la suma de los costos de sus tareas