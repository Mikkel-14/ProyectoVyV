# Created by joset at 12/18/2021
# language: es
Característica: Separación de ambientes de proyecto
  Como director de proyectos deseo poder separar la información de cada proyecto en espacios de
  trabajo aislados, para poder gestionar las tareas de múltiples proyectos sin confundirme.

  Escenario: No existen proyectos
    Dado que no existe ningún proyecto
    Cuando el director acceda al módulo de proyectos
    Entonces se mostrará el mensaje "No existen proyectos"
    Y se mostrará un botón con el mensaje "Crear nuevo proyecto"

  Escenario: Existe uno o más proyectos
    Dado que hay proyectos existentes
    Cuando el director acceda al módulo de proyectos
    Entonces se mostrará una lista de los proyectos existentes
    Y se podrá hacer clic en cada proyecto para acceder a su información