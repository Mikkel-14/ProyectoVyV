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
| 03-01-2022        | 21-01-2022    | Sprint 1 completado       |
| 24-01-2022        | 11-02-2022    | Sprint 2 completado       |
| 14-02-2022        | 01-03-2022    | Sprint 3 completado       |
|                   | 07-03-2022    | Presentacion del proyecto |
<br/>

## 6. Actividades de verificación y validación

---

### 6.1 Verificación
- Matriz de calidad de requisitoos
- Buenas prácticas de programación de Python especificadas en PEP
- Análisis de trazabilidad

### 6.2 Validación
-  Pruebas de caja blanca basadas en escenarios de comportamiento