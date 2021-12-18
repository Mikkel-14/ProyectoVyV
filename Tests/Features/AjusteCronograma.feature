# Created by Mahatma at 18/12/2021
# language: es
Característica: Ajuste automático de cronograma
  Como administrador del proyecto deseo poder ajustar las fechas de las tareas
  de forma automática sin alterar el orden de flujo del trabajo, para poder ajustar
  el proyecto a cambios inesperados.

  Escenario: Se cambia la fecha de entrega del proyecto
    Dado que se cambia la fecha de entrega del proyecto
    Cuando se actualice la fecha de entrega desde el panel de información del proyecto
    Entonces las fechas de las tareas del proyecto se ajustarán para la nueva fecha
    Y se mostrará el mensaje "El cronograma del proyecto se ha actualizado correctamente"

  Escenario: Se ha actualizado la fecha de entrega del proyecto
    Dado que se ha actualizado la fecha de entrega del proyecto
    Cuando se presente el diagrama de Gantt
    Entonces se visualizará el ajuste de fechas para cada tarea