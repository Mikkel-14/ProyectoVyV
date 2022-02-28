# Created by joset at 12/18/2021
# language: es
@CA2
Característica: [CA2] Separación de ambientes de proyecto
  Como administrador de proyectos deseo poder separar la información de cada proyecto en espacios de
  trabajo aislados, para poder gestionar las tareas de múltiples proyectos sin confundirme.

  Escenario: No existen proyectos
    Dado que no existe ningún proyecto del administrador en el módulo de proyectos
    Entonces el sistema redirigirá al administrador a la ventana de creación de nuevo proyecto

  Escenario: Existe uno o más proyectos
    Dado que el administrador tiene proyectos registrados
    Entonces se mostrará una lista de los proyectos existentes que le pertenecen al administrador
    