# Planificación del proyecto


## 1. Objetivos

---

En base al [desafio del negocio planteado](https://xbsoftware.com/case-studies-webdev/project-management-web-app/),
se identificaron los siguientes objetivos que persigue el proyecto:

- Visualizar el progreso de un proyecto y sus actividades
- Organizar las tareas de acuerdo a las restricciones de tiempo del proyecto
- Reducir la sobrecarga de trabajo en un proyecto mediante la asignación de tareas
- Comunicar el progreso a todos los involucrados en el proyecto.
<br/><br/>

## 2. Alcance del proyecto

---

El alcance inicial del proyecto se encuentra definido bajo los requerimientos que se pueden encontrar en
[un tablero en Trello](https://trello.com/b/lkaRzC0F), donde se incluye la siguiente información para cada requisito:

- Código, título y descripción de la historia de usuario
- Priorización obtenida por el cliente
- Estimación realizada con planning poker
- Criterios de aceptación (vinculados a este repositorio)
- Acciones relacionadas realizadas en el repositorio

Los requerimientos se encuentran sujetos a modificiaciones de su implementacón particular.
<br/><br/>

## 3. Planificación del proceso

---

Tomando en cuenta que se conocen los requisitos pero no en detalle y pueden haber cambios por parte del cliente, se considera un dominio de problema complejo, por lo cual se adoptará un proceso de desarrollo ágil (scrum).
<br/><br/>

### 3.1 Personalización del proceso de desarrollo

El proyecto se realizará en 3 sprints de 3 semanas, considerando un sprint inicial (sprint 0) para la comunicación del proyecto y las herramientas. El número de historias por sprint dependerá de estimación y la priorización de las mismas.

Se utilizarán las actividades generales definidas por scrum.

> **Herramientas escogidas**
> - Trello para la gestión, y seguimiento de las historias de usuario
> - PyCharm como entorno de desarrollo del proyecto, con los siguientes plugins y librerías:
>   - PlantUML para los diseños de diagramas
>   - Cucumber para BDD
>   - Behave para la integración de escenarios a pruebas en código
>   - Django y Bootstrap para el desarrollo del backend y el frontend, respectivamente
>   - Code with me como herramienta de colaboración en tiempo real
> - GitHub como repositorio centralizado del código y el plan del proyecto
> - Git como herramienta para el control de versiones
> - Google meet para las reuniones del equipo
<br/>

## 4. Entregables

---

Por cada sprint, se entregarán los siguientes productos del trabajo:

- Registro de conversación de las **historias del sprint** con el product owner / cliente
- Modelado de entidades para las **historias del sprint** (UML)
- Pruebas desarrolladas para los criterios de aceptación de las **historias del sprint**
- Reporte de pruebas ejecutadas para el sprint
- Código del proyecto con la implementación de las **historias del sprint**
<br/><br/>

## 5. Cronograma

---

| Fecha de inicio   | Fecha de fin  | Hito                      |
| ---------------   | ------------  | ---------                 |
| 20-12-2021        | 23-12-2021    | Sprint 0 completado       |
| 03-01-2022        | 04-02-2022    | Sprint 1 completado       |
| 07-02-2022        | 01-03-2022    | Sprint 2 completado       |
|                   | 07-03-2022    | Presentacion del proyecto |
<br/>

## 6. Actividades de verificación y validación

---

![Aspectos fundamentales de calidad](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/710f4a7e-cf41-4f7b-a924-167f588b6a04/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220302T014640Z&X-Amz-Expires=86400&X-Amz-Signature=0db95b646a7f9a1ff39414ac763c7fb4b9251fccd9b475b5f6dacaffce459403&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

Las actividades de verificación y validación del software empezaron desde la concepción del proyecto de software. Mediante la planificación del proyecto, se establecieron objetivos que debe cumplir el producto, por lo tanto, que pueden derivar en métricas para determinar el grado de conformidad del cliente y **validar** cuán apto es el producto para su uso. Adicionalmente, se establecieron las herramientas de apoyo para **verificar** que el producto se haga correctamente. 

A lo largo del ciclo de vida de desarrollo se adoptó un desarrollo dirigido por comportamiento, el cual nos proporcionó algunas prácticas y herramientas de apoyo a las actividades de verificación y validación, como las siguientes: 

### Etapa de requerimientos

- Mediante la herramienta de las historias de usuario, se logra establecer la comunicación con el cliente para comprender su necesidad y conversar cómo el sistema podría satisfacer este problema. Dado que esta herramienta comunica el valor de las funcionalidades del sistema por medio del leguaje natural, el cliente puede **validar** si el sistema es apto para el uso que él necesite mediante la conversación con el desarrollador y el tester.
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