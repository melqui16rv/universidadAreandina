# Respuestas - Prueba Objetivo Eje 4

**Estudiante:** Informática Forense  
**Eje:** 4  
**Total preguntas:** 12 (1 punto cada una)  
**Fecha:** 29 de marzo de 2026

---

## Respuestas

### Pregunta 1: Actividad penalizada por la CFAA
**Enunciado:** La Ley de Fraude y Abuso Informático (CFAA) de Estados Unidos es una legislación clave que aborda el cibercrimen.

**Respuesta:** ✅ **Acceso no autorizado a un sistema informático**

**Justificación:** La CFAA penaliza explícitamente el acceso no autorizado a computadoras y el uso de malware para causar daños. Esta es su función principal como ley federal contra ciberdelitos.

---

### Pregunta 2: Responsabilidad principal del investigador forense digital
**Enunciado:** La informática forense se centra en la recuperación y análisis de evidencia digital para su uso en procesos judicales.

**Respuesta:** ✅ **Recuperar y preservar la evidencia digital**

**Justificación:** La responsabilidad fundamental del investigador forense es asegurar la integridad y validez de la evidencia, manteniéndola íntegra para su admisión en tribunales.

---

### Pregunta 3: Principio de Intercambio de Locard
**Enunciado:** El Principio de Intercambio de Locard establece que "todo contacto deja un rastro".

**Respuesta:** ✅ **Cada interacción digital deja huellas que pueden ser rastreadas**

**Justificación:** Este principio forense, piedra angular de la informática forense (Eje 1), establece que toda acción en un sistema informático genera evidencia detectable. Cuando un usuario interactúa con un computador —iniciando sesión, abriendo archivos, navegando— se crean rastros en forma de logs, metadatos, archivos de registro y otros artefactos. Este concepto es fundamental para desarrollar metodologías de investigación forense.

---

### Pregunta 4: Metodología para recolección de evidencia de discos duros
**Enunciado:** La recolección de evidencia digital debe realizarse siguiendo protocolos estrictos.

**Respuesta:** ✅ **Creación de imágenes forenses**

**Justificación:** La metodología estándar para discos duros y almacenamiento (Eje 3) es crear una copia exacta o imagen forense que preserva toda la información sin alterar el original. Esta técnica es implementada mediante herramientas como FTK Imager y garantiza la integridad de la evidencia mediante hash criptográfico, permitiendo análisis posterior del Registro y otros artefactos del sistema.

---

### Pregunta 5: Obligaciones de la Directiva NIS
**Enunciado:** La Directiva NIS de la Unión Europea busca fortalecer la ciberseguridad de infraestructuras críticas.

**Respuesta:** ✅ **Implementar medidas de ciberseguridad**

**Justificación:** La Directiva NIS impone obligaciones técnicas y legales a las organizaciones de servicios esenciales para garantizar la seguridad de sus redes e información.

---

### Pregunta 6: Característica útil de NTFS para análisis forense
**Enunciado:** NTFS incluye características especiales que impactan el análisis forense.

**Respuesta:** ✅ **Journaling o registro de transacciones**

**Justificación:** El journaling de NTFS permite rastrear las operaciones realizadas en archivos, lo que es crucial para reconstruir la línea de tiempo de eventos forenses.

---

### Pregunta 7: Tipo de evidencia más volátil
**Enunciado:** La evidencia digital se puede clasificar en varios tipos según su naturaleza.

**Respuesta:** ✅ **Memoria RAM**

**Justificación:** Los datos en memoria RAM son volátiles y se pierden inmediatamente cuando el dispositivo se apaga, a diferencia de los datos en disco duro o dispositivos móviles que persisten.

---

### Pregunta 8: Información de clave del registro HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
**Enunciado:** El registro de Windows almacena configuraciones del sistema y preferencias de usuario.

**Respuesta:** ✅ **Programas que se ejecutan al iniciar el sistema**

**Justificación:** Esta clave específica del registro (analizada en Eje 3 con FTK Imager) contiene los programas configurados para ejecutarse automáticamente al inicio de Windows. Es una fuente crítica de evidencia forense que revela mecanismos de persistencia, instalación de software sospechoso y comportamiento del usuario. Su análisis es esencial en investigaciones de acceso no autorizado y presencia de malware.

---

### Pregunta 9: Área de aplicación de informática forense
**Enunciado:** La informática forense no solo se utiliza en contextos judiciales.

**Respuesta:** ✅ **Seguridad informática**

**Justificación:** Las técnicas forenses se aplican en investigaciones corporativas, detección de incidentes de seguridad y auditorías de TI, no solo en procesos judiciales.

---

### Pregunta 10: Componente de Windows para rastrear eventos
**Enunciado:** Es crucial entender cómo Windows registra y gestiona información.

**Respuesta:** ✅ **Visor de Eventos de Windows**

**Justificación:** El Visor de Eventos (herramienta central del Eje 1) es fundamental para la investigación forense en Windows. Registra eventos del sistema, accesos de seguridad, inicios de sesión, modificaciones de privilegios y ejecución de aplicaciones. Su análisis permite reconstruir la línea de tiempo de incidentes, identificar accesos no autorizados y detectar huellas de actividad maliciosa con criterios de trazabilidad forense.

---

### Pregunta 11: Característica fundamental para que evidencia digital sea admitida en tribunal
**Enunciado:** La evidencia digital debe cumplir ciertos requisitos para ser válida en procesos judiciales.

**Respuesta:** ✅ **Integridad**

**Justificación:** Aunque todas las características mencionadas son importantes, la **integridad** es fundamental (Eje 1). Debe demostrarse que la evidencia no ha sido alterada, modificada o manipulada desde su recolección hasta su presentación en tribunal. Este principio es esencial en el análisis forense: se utiliza hashing criptográfico para verificar la integridad de imágenes forenses (Eje 3) y se mantiene una cadena de custodia rigurosa durante todo el proceso investigativo.

---

### Pregunta 12: Objetivo principal del Convenio de Budapest
**Enunciado:** El Convenio de Budapest es un tratado internacional sobre delitos cibernéticos.

**Respuesta:** ✅ **Armonización de las leyes sobre delitos cibernéticos**

**Justificación:** El Convenio de Budapest, primer tratado internacional sobre ciberdelitos (2001, en vigor 2004), busca precisamente que los países firmantes establezcan legislaciones coherentes y compatibles para combatir los ciberdelitos de manera efectiva internacionalmente.

---

## Resumen de Respuestas

| Pregunta | Respuesta | Puntos |
|----------|-----------|--------|
| 1 | Acceso no autorizado a un sistema informático | 1 |
| 2 | Recuperar y preservar la evidencia digital | 1 |
| 3 | Cada interacción digital deja huellas que pueden ser rastreadas | 1 |
| 4 | Creación de imágenes forenses | 1 |
| 5 | Implementar medidas de ciberseguridad | 1 |
| 6 | Journaling o registro de transacciones | 1 |
| 7 | Memoria RAM | 1 |
| 8 | Programas que se ejecutan al iniciar el sistema | 1 |
| 9 | Seguridad informática | 1 |
| 10 | Visor de Eventos de Windows | 1 |
| 11 | Integridad | 1 |
| 12 | Armonización de las leyes sobre delitos cibernéticos | 1 |
| **TOTAL** | **12 respuestas** | **12 puntos** |

---

## Notas importantes

- Todas las respuestas están fundamentadas en:
  - **Eje 1**: Referente de Pensamiento sobre análisis forense, Principio de Locard, cadena de custodia y valoración de evidencia
  - **Eje 3**: Análisis práctico del Registro de Windows con FTK Imager, creación de imágenes forenses, análisis de claves Run y RecentDocs
  - **Eje 4**: Referente de Pensamiento sobre delitos cibernéticos internacionales, marcos legales (CFAA, Directiva NIS, Convenio Budapest) e informática forense

- **Integración de conceptos clave:**
  - Locard ("todo contacto deja rastro") → base de todas las investigaciones forenses
  - Integridad de evidencia → uso de imágenes forenses con hash criptográfico
  - Registro de Windows → análisis de persistencia (Run) y actividad de usuario (RecentDocs, Visor de Eventos)
  - Cadena de custodia → documentación rigurosa desde recolección hasta presentación

- Recuerde cumplir con los 40 minutos de duración en la plataforma
- No cambiar de ventana durante el examen
- Entregar la evaluación al finalizar
