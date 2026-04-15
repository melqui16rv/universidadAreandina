# Actividad evaluativa - Eje 3

**Fecha de entrega:** Lunes a las 23:59  
**Puntos:** 20  
**Tipo de entrega:** cuadro de entrada de texto, URL de página web, grabación multimedia o carga de archivo  
**Disponible:** 2 de marzo, 0:00 - 16 de marzo, 23:59

## Actividad evaluativa - Tarea Eje 3

**Tiempo de trabajo del estudiante:** 17 horas

## Habilidades de pensamiento a desarrollar

| Categoría | Habilidad | Marca | Habilidad | Marca | Habilidad | Marca |
| --- | --- | --- | --- | --- | --- | --- |
| Habilidades de orden básico | Observar |  | Identificar | X | Comparar |  |
| Habilidades de orden básico | Relacionar | X | Ordenar |  | Clasificar jerárquicamente |  |
| Habilidades de integración | Analizar | X | Sintetizar |  | Evaluar | X |
| Habilidades de orden superior | Metacognición |  | Toma de decisiones |  | Pensamiento crítico |  |
| Habilidades de orden superior | Pensamiento creativo | X |  |  |  |  |

## Nombre de la tarea

**Análisis forense del Registro de Windows con FTK Imager**

## Objetivo de aprendizaje

Realizar un análisis forense del Registro de Windows utilizando FTK Imager para identificar evidencia digital relevante.

## Descripción de la tarea

La tarea invita al estudiante a usar FTK Imager para recolectar y analizar el Registro de Windows, identificando posibles indicios de accesos no autorizados, cambios en la configuración o instalación de software sospechoso.

## Requisitos para la tarea

1. Realice la lectura del referente de pensamiento y de la lectura complementaria.
2. Revise todos los documentos, recursos y actividades asociadas con el Eje 3.
3. Lea con atención la rúbrica de evaluación.

## Instrucciones de entrega

### 1. Preparación del entorno

1. Descargar e instalar FTK Imager.
2. Abrir FTK Imager y seleccionar el sistema Windows en el que realizará el análisis. Puede ser un entorno virtual o una máquina de prueba.

### 2. Extracción de evidencia del Registro de Windows

1. Utilizar FTK Imager para extraer una copia del Registro de Windows.
2. Analizar las siguientes rutas:

   - HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
   - HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs

3. Guardar las copias de las claves en el equipo.

### 3. Análisis del Registro

1. Examinar las claves extraídas buscando programas que se inician automáticamente al arrancar el sistema.
2. Revisar los documentos recientes abiertos.
3. Documentar cualquier actividad sospechosa, como:

   - presencia de programas desconocidos
   - accesos recientes no autorizados

### 4. Informe forense

Elaborar un informe que incluya:

1. Descripción de las claves extraídas.
2. Evidencia de programas o archivos sospechosos.
3. Recomendaciones sobre cómo proceder en caso de actividad inusual.
4. Capturas de pantalla de FTK Imager mostrando las claves del Registro analizadas.

### 5. Estructura de entrega

Elabore un documento en formato Word con los siguientes elementos:

1. Portada.
2. Introducción.
3. Objetivos de la actividad.
4. Desarrollo de la tarea.
5. Conclusiones.
6. Bibliografía.

## Rúbrica Eje 3

| Criterio | Desempeño alto | Desempeño medio alto | Desempeño medio | Desempeño bajo | Puntos |
| --- | --- | --- | --- | --- | --- |
| Construcción y contenido del informe | **3.4 pts**. Identifica los riesgos y las alternativas de solución frente a un posible incidente de seguridad informática, los desglosa y puede aislar sus principales características. | **2.72 pts**. Evidencia comprensión de los contenidos, identifica conceptos y análisis de los temas planteados. | **2.04 pts**. El contenido se estructura de manera básica, identifica algunos conceptos, pero no realiza análisis de los temas planteados. | **0.68 pts**. No evidencia comprensión ni profundidad en el desarrollo de los contenidos propuestos. Los resultados no son visibles. | 3.4 pts |
| Evidencia y documentación | **3.3 pts**. Capturas de pantalla y documentación completa, claramente organizadas y directamente vinculadas a las conclusiones del análisis. | **2.64 pts**. Se presentan capturas de pantalla y documentación que respaldan el análisis realizado. | **1.98 pts**. Se presentan algunas capturas de pantalla, pero no están claramente documentadas o vinculadas al análisis. | **0.66 pts**. No se presentan capturas de pantalla ni documentación de los resultados obtenidos durante el análisis. | 3.3 pts |
| Análisis de resultados | **3.3 pts**. Se realiza un análisis profundo y crítico de los resultados, identificando patrones, tendencias y posibles implicaciones de los hallazgos. | **2.64 pts**. Se identifican y analizan adecuadamente los resultados, con observaciones relevantes sobre la información extraída. | **1.98 pts**. Se identifican algunos resultados, pero el análisis es superficial y carece de profundidad. | **0.66 pts**. No se identifican resultados o no se realizan observaciones sobre la información extraída del Registro. | 3.3 pts |
| Recomendaciones y soluciones | **3.4 pts**. Recomendaciones exhaustivas y bien justificadas, con un enfoque en la prevención y mitigación de futuros incidentes de seguridad informática. | **2.72 pts**. Se presentan recomendaciones claras y bien fundamentadas para abordar los incidentes de seguridad identificados. | **2.04 pts**. Se presentan recomendaciones básicas, pero carecen de justificación o análisis adecuado. | **0.68 pts**. No se presentan recomendaciones o soluciones a los incidentes de seguridad. | 3.4 pts |
| Capacidad de análisis y síntesis | **3.3 pts**. Los contenidos responden a un orden lógico que da respuesta a lo solicitado y generan reflexión. | **2.64 pts**. Construye contenidos y estos responden a un orden lógico que da respuesta a lo solicitado. | **1.98 pts**. Construye contenidos, sin embargo, falta mayor orden lógico que permita su comprensión. | **0.66 pts**. No evidencia construcción de contenidos, no tiene orden lógico. | 3.3 pts |
| Uso de la gramática | **3.3 pts**. El documento tiene una adecuada estructura gramatical, ortografía y puntuación, lo cual facilita la comprensión de las ideas. Emplea un léxico variado, facilita la comunicación e incluye todos los apartados solicitados en el documento. | **2.64 pts**. El documento tiene una adecuada estructura gramatical, ortografía y puntuación. Utiliza un vocabulario preciso y el escrito es claro. No incluye todos los apartados solicitados en el documento. | **1.98 pts**. El documento tiene una adecuada estructura gramatical; sin embargo, presenta algunos errores de ortografía. Utiliza un vocabulario preciso, aunque el escrito no es del todo claro y distrae al lector. | **0.66 pts**. El documento carece de una adecuada estructura gramatical, con errores de ortografía o puntuación. Además, utiliza un vocabulario impreciso. | 3.3 pts |

**Puntos totales:** 20
