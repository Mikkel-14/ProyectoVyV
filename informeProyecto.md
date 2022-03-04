# Informe del proyecto


Las actividades de verificación y validación del software empezaron desde la concepción del proyecto de software. Mediante la [planificación del proyecto](https://github.com/Mikkel-14/ProyectoVyV/blob/main/planificacion.md), se establecieron objetivos que debe cumplir el producto, por lo tanto, que pueden derivar en métricas para determinar el grado de conformidad del cliente y **validar** cuán apto es el producto para su uso. Adicionalmente, se establecieron las herramientas de apoyo para **verificar** que el producto se haga correctamente. 

A lo largo del ciclo de vida de desarrollo se adoptó un desarrollo dirigido por comportamiento, el cual nos proporcionó algunas prácticas y herramientas de apoyo a las actividades de verificación y validación, como las siguientes: 

### Etapa de requerimientos

- Mediante la herramienta de las [historias de usuario](https://trello.com/b/lkaRzC0F), se logra establecer la comunicación con el cliente para comprender su necesidad y conversar cómo el sistema podría satisfacer este problema. Dado que esta herramienta comunica el valor de las funcionalidades del sistema por medio del leguaje natural, el cliente puede **validar** si el sistema es apto para el uso que él necesite mediante la conversación con el desarrollador y el tester.
- Al finalizar cada sesión de recopilación de requerimientos, se realizó una revisión informal de pares usando una lista de atributos de calidad de requisitos para **verificar** que este artefacto no introduzca defectos relacionados con la ambigüedad, correctitud, realizabilidad, consistencia, comprensibilidad, gramaticalidad o legibilidad. De esta manera, evitamos que estos defectos se introduzcan en artefactos de las etapas del ciclo de vida posteriores.
- Al dotar a cada historia de usuario un identificador de historia, buscamos **verificar** que este requisito se encuentre realizado en un caso de prueba e implementado en el código. En otras palabras, **verificamos** que el requisito se pueda trazar a todo el resto de artefactos del proyecto.
- Usando la herramienta Trello, mantenemos a todas las historias del proyecto en un mismo lugar y como un documento vivo. Dado que nos encontramos en un desarrollo ágil, los posibles cambios que vayan surgiendo a través del tiempo para una historia quedan documentados a través de comentarios. De esta manera, el cliente puede **validar** la implementación de la historia en el producto y proponer nuevas ideas.
- Cuando escribimos los criterios de aceptación para cada historia, se utilizó la herramienta Gherkins para automatizar la prueba mediante el uso de lenguaje natural. Con esta herramienta, el desarrollador puede **validar** que el producto se comporta como espera el cliente. A todo esto, pensar en escenarios de pruebas nos permite **verificar** de forma temprana si los requerimientos son realizables y claros no solo para el cliente sino para el equipo de desarrollo.

Hasta esta etapa del desarrollo, hemos utilizado una herramienta para dar seguimiento a las historias. Sin embargo, desde la creación de criterios de aceptación mediante escenarios, y los artefactos descritos en las etapas posteriores, se utiliza la herramienta GitHub como repositorio central para el control de versiones de los artefactos. Con esta herramienta, buscamos **asegurar** la gestión de cambios sobre los artefactos. Adicionalmente, gracias a la integración disponible entre GitHub y Trello, se puede **verificar** la trazabilidad de porciones de código con la funcionalidad especificada en la historia de usuario adjuntando el identificador del commit.

### Etapa de diseño

- Para el diseño de pruebas, se utiliza la librería behave, que nos permite enlazar los escenarios de prueba en lenguaje natural (criterios de aceptación) con los detalles de implementación de las pruebas. Es decir, esta herramienta nos permite **verificar** la trazabilidad de las pruebas con los criterios de aceptación.
- Al desarrollar las pruebas en un lenguaje de programación, buscamos **validar** el comportamiento del sistema, probando que las firmas de los métodos de una clase proporcionen la funcionalidad esperada.
- Gracias a que las pruebas se realizan a un alto nivel de abstracción, estas mismas guían el diseño de las entidades del sistema y su funcionalidad. Al definir las firmas de los métodos desde las pruebas, estamos **verificando** que cada método cumpla con el principio de responsabilidad única, propiciada por una revisión informal del diseño.
- Mediante el complemento PlantUML se diseñaron las diferentes clases que conformarían el sistema y las relaciones entre estas. Esto permitió **verificar** la trazabilidad de las pruebas diseñadas hacia artefactos vivos.

### Etapa de implementación

- La selección del entorno de desarrollo integrado PyCharm nos proporciona un estándar de programación para Python (PEP). De esta manera, se puede **verificar** que el código sea legible y consistente con el resto de desarrolladores.
- Durante cada etapa de desarrollo, se obtuvo retroalimentación del cliente mediante revisiones informales, de modo que podamos **validar** la conformidad del cliente con el mínimo producto viable, y de ser el caso hacer cambios.
- Se adoptó la práctica de programación por pares usando las herramientas Code With Me y Google Meet. Esto nos permitió **verificar** que el código esté implementado de acuerdo al diseño y que tenga la menor cantidad de defectos posible.