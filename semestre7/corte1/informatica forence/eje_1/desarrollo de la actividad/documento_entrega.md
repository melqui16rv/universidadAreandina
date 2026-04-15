# Análisis Forense de un Registro de Eventos en Windows

---

## Portada

| | |
|---|---|
| **Título:** | Análisis Forense de un Registro de Eventos en Windows |
| **Asignatura:** | Informática Forense |
| **Eje:** | Eje 1 |
| **Estudiante:** | Melqui Romero |
| **Docente:** | *(por definir)* |
| **Institución:** | SENA |
| **Fecha:** | Febrero de 2026 |

---

## 1. Introducción

La informática forense es la disciplina que aplica técnicas científicas y analíticas especializadas para identificar, preservar, analizar y presentar datos que sean válidos dentro de un proceso legal o investigativo (Luna Felipez, s.f.). En un mundo cada vez más digitalizado, donde los sistemas informáticos son el eje de las comunicaciones, transacciones y operaciones cotidianas, el análisis forense digital se ha convertido en una herramienta imprescindible para la investigación de incidentes de ciberseguridad y cibercrimen.

El principio de intercambio de Locard, piedra angular de la ciencia forense, establece que **"todo contacto deja un rastro"**. En el contexto digital, esto significa que cada vez que un usuario interactúa con un sistema informático —ya sea un computador, una red o un dispositivo móvil— se generan rastros que evidencian dicha interacción: archivos, logs de actividad, metadatos, historiales de navegación y correos electrónicos, entre otros (De Haro Olmo, 2020). Estos rastros digitales constituyen la evidencia que un perito informático forense debe identificar, preservar y analizar con rigor metodológico.

El sistema operativo Windows, al ser uno de los más utilizados a nivel mundial, integra una herramienta nativa denominada **Visor de Eventos (Event Viewer)** que registra de manera automática y continua toda la actividad del sistema: inicios de sesión exitosos y fallidos, cambios de privilegios, instalación de servicios, errores del sistema y mucho más. Estos registros (logs) son una fuente primaria de evidencia digital en cualquier investigación forense.

El presente trabajo tiene como propósito realizar un análisis forense de los registros de eventos de un sistema Windows, simulando un escenario de investigación donde se busca identificar posibles huellas de actividad sospechosa o maliciosa. Se aplicarán los conceptos del principio de intercambio de Locard y las fases de la metodología forense digital: identificación, preservación, análisis y presentación de la evidencia.

---

## 2. Objetivos

### 2.1 Objetivo General

Aplicar técnicas de informática forense para analizar y documentar la actividad de un usuario sospechoso a través de los registros de eventos de Windows, identificando posibles huellas de actividad maliciosa.

### 2.2 Objetivos Específicos

- Configurar un escenario forense utilizando el Visor de Eventos (Event Viewer) de Windows.
- Identificar y clasificar eventos clave relacionados con actividades sospechosas en los registros de Seguridad y Sistema.
- Documentar detalladamente cada evento encontrado, incluyendo su ID, fecha y hora, usuario involucrado y posible interpretación forense.
- Analizar la correlación entre los eventos identificados para determinar patrones de comportamiento potencialmente malicioso.
- Presentar conclusiones fundamentadas sobre los hallazgos de la investigación.

---

## 3. Marco Teórico

### 3.1 El Principio de Intercambio de Locard en el Entorno Digital

El principio de Locard, formulado por el criminólogo francés Edmond Locard, establece que cuando dos objetos entran en contacto, siempre hay una transferencia de material entre ellos. Aplicado al ámbito digital, este principio se manifiesta en cuatro dimensiones fundamentales:

1. **Intercambio de información:** Cada interacción con un sistema digital genera datos. Los elementos clave incluyen archivos (documentos, imágenes, etc.), logs de actividad (registros de acciones realizadas en el sistema) y metadatos (datos sobre otros datos, como la fecha de creación o modificación de un archivo).

2. **Transferencia de evidencia:** Cada acción en el entorno digital deja huellas que pueden ser rastreadas, incluso si se intenta eliminarlas. Esto incluye archivos transferidos, historiales de navegación y correos electrónicos que pueden contener información crucial para una investigación.

3. **Persistencia de la evidencia:** La evidencia digital puede mantenerse accesible y recuperable, incluso después de intentos de eliminación. Los datos pueden existir en diversas formas y ubicaciones, como en la memoria de un dispositivo o en cachés temporales. Los elementos clave son la recuperabilidad (técnicas forenses que permiten recuperar datos eliminados) y el almacenamiento (discos duros, SSDs, servidores en la nube).

4. **Análisis del intercambio:** Los investigadores forenses analizan meticulosamente todos los rastros de intercambio digital para identificar acciones, responsables y cronología de eventos. Los elementos clave son el análisis de logs (examinar registros de actividad para reconstruir eventos) y la línea de tiempo (establecer un orden de eventos para entender cómo ocurrió un incidente).

### 3.2 El Visor de Eventos de Windows como Herramienta Forense

El Visor de Eventos (Event Viewer) es una herramienta integrada en Windows que registra eventos significativos del sistema operativo. Desde la perspectiva forense, los registros más relevantes son:

- **Registro de Seguridad:** Contiene eventos de auditoría como inicios de sesión, cambios de permisos, acceso a recursos y modificaciones de cuentas de usuario.
- **Registro de Sistema:** Contiene eventos generados por componentes del sistema operativo, incluyendo instalación de servicios, errores de drivers y cambios en la configuración del sistema.

### 3.3 Eventos Críticos para la Investigación Forense

| Event ID | Registro | Descripción | Relevancia Forense |
|----------|----------|-------------|---------------------|
| 4624 | Seguridad | Inicio de sesión exitoso | Identificar accesos en horarios inusuales |
| 4625 | Seguridad | Inicio de sesión fallido | Detectar intentos de acceso no autorizado (fuerza bruta) |
| 4611 | Seguridad | Proceso de inicio de sesión de confianza registrado | Detectar elevación de privilegios vía UAC (ConsentUI) |
| 4672 | Seguridad | Privilegios especiales asignados | Detectar escalación de privilegios |
| 4697 | Seguridad | Se instaló un servicio en el sistema | Detectar instalación de servicios sospechosos |
| 4720 | Seguridad | Cuenta de usuario creada | Detectar creación de cuentas de puerta trasera (backdoor) |
| 4726 | Seguridad | Cuenta de usuario eliminada | Detectar eliminación de evidencia |
| 4728 | Seguridad | Miembro agregado a grupo global | Detectar modificación de membresías de grupo |
| 4729 | Seguridad | Miembro removido de grupo global | Detectar eliminación de membresías de grupo |
| 7045 | Sistema | Servicio instalado | Detectar instalación de malware como servicio |
| 1102 | Seguridad | Registro de auditoría borrado | Detectar intento de eliminación de evidencia (anti-forense) |

---

## 4. Metodología

Para la realización de este análisis forense se siguió la metodología forense digital compuesta por las siguientes fases (De Haro Olmo, 2020):

1. **Identificación:** Se identificaron las fuentes de evidencia digital disponibles en el sistema operativo Windows, específicamente los registros de eventos accesibles mediante el Visor de Eventos.

2. **Preservación:** Se documentaron los eventos mediante capturas de pantalla que garantizan la integridad visual de la evidencia en el momento de su recolección.

3. **Análisis:** Se examinaron detalladamente los eventos registrados, correlacionando IDs de eventos, marcas de tiempo, cuentas de usuario involucradas y descripciones para identificar patrones de actividad sospechosa.

4. **Presentación:** Los hallazgos se organizaron de forma estructurada en el presente documento, con evidencia visual y análisis interpretativo de cada evento.

### 4.1 Herramientas Utilizadas

- **Sistema operativo:** Windows 11
- **Equipo analizado:** MELQUI
- **Herramienta de análisis:** Visor de Eventos (Event Viewer) — `eventvwr.msc`
- **Documentación:** Capturas de pantalla tomadas con la herramienta de recorte de Windows (`Win + Shift + S`)
- **Configuración adicional:** Se habilitó la auditoría de errores de inicio de sesión mediante el comando `auditpol /set /subcategory:"Logon" /success:enable /failure:enable` para garantizar el registro de intentos fallidos de acceso

### 4.2 Escenario de Investigación

Se configuró un escenario forense simulado en el cual se generaron deliberadamente eventos que replican el comportamiento típico de un atacante o usuario malintencionado:

- Análisis de inicios de sesión en horarios inusuales (identificación de accesos nocturnos sospechosos)
- Inicio de sesión con privilegios elevados de administrador
- Creación y eliminación de una cuenta de usuario temporal (simulación de backdoor)
- Instalación y eliminación de un servicio del sistema (simulación de persistencia de malware)
- Borrado de los registros de auditoría (simulación de técnica anti-forense)

---

## 5. Configuración del Escenario Forense

### 5.1 Acceso al Visor de Eventos

Se accedió al Visor de Eventos mediante el comando `eventvwr.msc` desde la ventana Ejecutar (`Win + R`). En la captura se puede observar simultáneamente la ventana "Ejecutar" con el comando ingresado y el Visor de Eventos ya abierto en segundo plano, mostrando la pantalla de "Introducción y resumen" con las secciones: Introducción, Resumen de eventos administrativos, Nodos vistos recientemente y Resumen de registro.

> **📸 Captura 1:** Ventana Ejecutar con `eventvwr.msc` y Visor de Eventos abierto

![Captura 1 - Abrir Event Viewer](../img/01_abrir_event_viewer.png)

### 5.2 Vista general del Visor de Eventos — Árbol de navegación

Al expandir el árbol de navegación del panel izquierdo, se observó la estructura completa del Visor de Eventos del equipo local, que incluye:

- **Vistas personalizadas** → Eventos administrativos
- **Registros de Windows** → Aplicación, Seguridad, Instalación, Sistema, Eventos reenviados
- **Registros de aplicaciones y servicios** → Eventos de hardware, HP Analytics, Interfaz de usuario de Microsoft, Internet Explorer, Microsoft, Microsoft Office Alerts, OpenSSH, Servicio de administración, Windows PowerShell
- **Suscripciones**

Esta estructura permite navegar hacia los registros de Seguridad y Sistema que son el foco del análisis forense.

> **📸 Captura 2:** Árbol de navegación completo del Visor de Eventos

![Captura 2 - Vista principal](../img/02_visor_eventos_principal.png)

### 5.3 Registro de Seguridad

Se navegó a **Registros de Windows > Seguridad** para revisar los eventos de auditoría del sistema. El registro contiene un total de **21.312 eventos** al momento del análisis. Los eventos predominantes corresponden al **Event ID 4662** (Se realizó una operación en un objeto), categoría "Other Object Access Events", con nivel de auditoría correcta. También se identificaron eventos de tipo **4624** (Logon — inicio de sesión exitoso) y **4634** (Logoff — cierre de sesión), los cuales registran la actividad de acceso del usuario al equipo **MELQUI** en diversas fechas entre el 13/2/2026 y el 15/2/2026.

En el detalle del evento 4662 se observa que el origen es "Microsoft Windows security auditing", registrado el 15/2/2026 a las 16:21:31, con categoría "Other Object Access Events", nivel "Información" y equipo "MELQUI".

> **📸 Captura 3:** Registro de Seguridad mostrando 21.312 eventos, predominando Event ID 4662

![Captura 3 - Registro de Seguridad](../img/03_registro_seguridad.png)

Adicionalmente, al filtrar los eventos de inicio y cierre de sesión, se identificaron múltiples eventos **4624 (Logon)** y **4634 (Logoff)** correspondientes a la actividad del usuario en los días 13, 14 y 15 de febrero de 2026:

| Fecha y hora | Event ID | Tipo | Observación |
|---|---|---|---|
| 14/2/2026 21:30:14 | 4624 | Logon | ⚠️ Horario nocturno inusual |
| 14/2/2026 21:35:47 | 4624 | Logon | ⚠️ Horario nocturno inusual |
| 14/2/2026 21:20:54 | 4624 | Logon | ⚠️ Horario nocturno inusual |
| 14/2/2026 23:19:25 | 4634 | Logoff | ⚠️ Cierre de sesión en madrugada |
| 14/2/2026 18:00:23 | 4624 | Logon | Horario fuera de jornada laboral |
| 14/2/2026 18:29:12 | 4624 | Logon | Horario fuera de jornada laboral |
| 14/2/2026 18:16:38 | 4624 | Logon | Horario fuera de jornada laboral |
| 14/2/2026 12:26:41 | 4624 | Logon | Horario laboral normal |
| 14/2/2026 12:46:49 | 4624 | Logon | Horario laboral normal |
| 15/2/2026 12:51:01 | 4624 | Logon | Horario laboral normal |
| 15/2/2026 12:46:37 | 4624 | Logon | Horario laboral normal |
| 15/2/2026 14:36:01 | 4624 | Logon | Horario laboral normal |
| 15/2/2026 12:42:19 | 4624 | Logon | Horario laboral normal |
| 14/2/2026 15:53:02 | 4624 | Logon | Horario laboral normal |
| 13/2/2026 17:03:58 | 4624 | Logon | Horario laboral normal |
| 13/2/2026 16:44:20 | 4624 | Logon | Horario laboral normal |
| 13/2/2026 21:59:13 | 4634 | Logoff | ⚠️ Cierre de sesión nocturno |

Del análisis de los registros de inicio y cierre de sesión se identificó un patrón relevante: existen múltiples accesos en **horarios nocturnos (después de las 21:00 horas)**, lo cual puede ser indicador de actividad sospechosa si el usuario habitual solo opera en jornada laboral diurna.

> **📸 Captura 5:** Registro de Seguridad filtrado mostrando eventos 4624 (Logon) y 4634 (Logoff) con horarios sospechosos

![Captura 5 - Eventos de inicio de sesión](../img/05_eventos_logon.png)

### 5.4 Registro de Sistema

Se navegó a **Registros de Windows > Sistema** para revisar los eventos del sistema operativo. El registro contiene un total de **28.280 eventos**. Se observaron los siguientes tipos de eventos predominantes:

- **Event ID 12 (BTHUSB)** — Nivel: Advertencia. Descripción: "El adaptador local devolvió un paquete de datos ACL incorrecto y éste se descartó." Múltiples ocurrencias a lo largo del 15/2/2026, lo que indica un problema recurrente con el adaptador Bluetooth del equipo.
- **Event ID 10016 (DistributedCOM)** — Nivel: Advertencia. Múltiples ocurrencias indicando problemas de permisos con componentes COM distribuidos.

El equipo analizado se identifica como **MELQUI**.

> **📸 Captura 4:** Registro de Sistema mostrando 28.280 eventos, con advertencias BTHUSB (ID 12) y DistributedCOM (ID 10016)

![Captura 4 - Registro de Sistema](../img/04_registro_sistema.png)

---

## 6. Resumen de Hallazgos

Durante el análisis forense de los registros de eventos del equipo **MELQUI** (21.365 eventos en Seguridad, 28.280 eventos en Sistema) se identificaron los siguientes eventos sospechosos:

| # | Event ID | Registro | Fecha y hora | Categoría | Interpretación |
|---|----------|----------|-------------|-----------|----------------|
| 1 | 4624 | Seguridad | 14/2/2026 21:20:54 | Logon — Horario nocturno | Primer acceso nocturno fuera de jornada laboral |
| 2 | 4624 | Seguridad | 14/2/2026 21:30:14 | Logon — Horario nocturno | Segundo acceso nocturno en 10 minutos |
| 3 | 4624 | Seguridad | 14/2/2026 21:35:47 | Logon — Horario nocturno | Tercer acceso nocturno en el mismo periodo |
| 4 | 4634 | Seguridad | 14/2/2026 23:19:25 | Logoff — Madrugada | Cierre de sesión en la madrugada |
| 5 | 4611 | Seguridad | 15/2/2026 17:02:38 | Security System Extension | Registro de proceso de confianza (ConsentUI — elevación UAC) |
| 6 | 4720 | Seguridad | 15/2/2026 20:57:16 | User Account Management | Creación de cuenta UsuarioPrueba por melqui.romero |
| 7 | 4728 | Seguridad | 15/2/2026 20:57:16 | Security Group Management | UsuarioPrueba agregado automáticamente al grupo Ninguno |
| 8 | 4726 | Seguridad | 15/2/2026 20:58:10 | User Account Management | Eliminación de cuenta UsuarioPrueba |
| 9 | 4729 | Seguridad | 15/2/2026 20:58:10 | Security Group Management | UsuarioPrueba removido del grupo Ninguno |
| 10 | 4697 | Seguridad | 15/2/2026 21:13:32 | Security System Extension | Instalación de ServicioPrueba (cmd.exe) como servicio |
| 11 | 1102 | Seguridad | 15/2/2026 21:23:32 | Log clear | Borrado intencional del registro de auditoría |

---

## 7. Descripción Detallada de Eventos Sospechosos

### 7.1 Evento: Inicios de Sesión en Horarios Inusuales (Event ID 4624)

**Tipo de evento:** Auditoría correcta — Inicio de sesión (Logon)  
**Registro:** Seguridad  
**Nivel de sospecha:** 🔴 Alto  

**Descripción del hallazgo:**

Durante la revisión de los registros de seguridad del equipo MELQUI, se identificó un patrón de **múltiples inicios de sesión exitosos en horarios nocturnos** que no corresponden a una jornada laboral convencional (8:00 – 18:00 horas). En particular, se detectaron tres sesiones en un intervalo de 15 minutos durante la noche del 14 de febrero de 2026, seguidas de un cierre de sesión casi dos horas después, en la madrugada.

Esta actividad podría indicar que un usuario no autorizado accedió al sistema aprovechando el horario nocturno, cuando es menos probable que el propietario legítimo del equipo esté presente para detectar la actividad.

| Campo | Valor |
|-------|-------|
| **ID del evento** | 4624 |
| **Acceso sospechoso #1** | 14/2/2026 21:20:54 |
| **Acceso sospechoso #2** | 14/2/2026 21:30:14 |
| **Acceso sospechoso #3** | 14/2/2026 21:35:47 |
| **Cierre de sesión** | 14/2/2026 23:19:25 (Event ID 4634) |
| **Duración estimada de la sesión** | Aproximadamente 2 horas |
| **Equipo** | MELQUI |
| **Origen** | Microsoft Windows security auditing |
| **Palabras clave** | Auditoría correcta |

**Posible interpretación forense:**

Los inicios de sesión en horarios inusuales son uno de los principales indicadores de compromiso (IoC — Indicator of Compromise) en una investigación forense. En este caso:

- Se registraron **3 inicios de sesión** entre las 21:20 y las 21:35, un intervalo de solo 15 minutos. La frecuencia de estos accesos sugiere actividad deliberada, no accidental.
- La sesión se mantuvo activa hasta las **23:19** (cierre de sesión), lo cual indica que alguien operó el equipo durante casi 2 horas en horario nocturno.
- En una investigación real, se correlacionaría esta actividad con otros indicadores: ¿se ejecutaron programas inusuales durante esas horas? ¿Se accedieron archivos sensibles? ¿Se realizaron conexiones de red sospechosas?
- También se observaron accesos en la tarde-noche del mismo día (18:00, 18:16, 18:29), lo que podría indicar un patrón de actividad extendida fuera de horario.

**Comparación de patrones de acceso:**

| Período | Cantidad de accesos (4624) | Evaluación |
|---------|---------------------------|------------|
| 13/2 - Jornada diurna (8:00-18:00) | 2 eventos | Normal |
| 14/2 - Jornada diurna (8:00-18:00) | 8 eventos | Normal / Alto |
| 14/2 - Horario nocturno (18:00-23:59) | 6 eventos | ⚠️ **Sospechoso** |
| 15/2 - Jornada diurna (8:00-18:00) | 5 eventos | Normal |

**Evidencia visual:**

> **📸 Captura 6:** Registro de Seguridad filtrado por eventos 4624 (Logon) y 4634 (Logoff), mostrando inicios de sesión en horarios nocturnos del 14/2/2026

![Captura 6 - Eventos 4624 con horarios sospechosos](../img/06_eventos_logon_sospechosos.png)

---

### 7.2 Evento: Escalación de Privilegios — Registro de Proceso de Confianza (Event ID 4611) y Privilegios Especiales (Event ID 4672)

**Tipo de evento:** Auditoría correcta — Security System Extension  
**Registro:** Seguridad  
**Nivel de sospecha:** 🔴 Alto  

**Descripción del hallazgo:**

Al abrir una sesión de **PowerShell como Administrador**, el sistema operativo invocó el proceso **ConsentUI** (la ventana de Control de Cuentas de Usuario — UAC) para autorizar la elevación de privilegios. Windows registró este evento como **Event ID 4611** ("Se registró un proceso de inicio de sesión de confianza con la autoridad de seguridad local. Se confiará en este proceso de inicio de sesión para enviar solicitudes de inicio de sesión"). Adicionalmente, en la lista de eventos se observó el **Event ID 4672** (Special Logon), que confirma la asignación efectiva de los privilegios especiales de administrador.

Esta secuencia de eventos (4611 + 4672) es un indicador directo de **escalación de privilegios**, técnica comúnmente empleada por atacantes para obtener control total del sistema.

| Campo | Valor |
|-------|-------|
| **ID del evento principal** | 4611 |
| **Fecha y hora** | 15/2/2026 17:02:38 |
| **Categoría de tarea** | Security System Extension |
| **Nombre de cuenta** | MELQUI$ |
| **Nombre de proceso de inicio de sesión** | ConsentUI |
| **Equipo** | MELQUI |
| **Evento complementario** | 4672 (Special Logon) — visible en la lista de eventos a las 15/2/2026 20:54:59 |

**Posible interpretación forense:**

La elevación de privilegios mediante UAC (ConsentUI) es un paso clave en la cadena de ataque. Un atacante con privilegios de administrador puede:
- Instalar software malicioso
- Crear cuentas de usuario para acceso futuro (backdoor)
- Modificar configuraciones de seguridad
- Borrar registros de auditoría para eliminar evidencia

El hecho de que Windows registre tanto el proceso de confianza (4611) como la asignación de privilegios (4672) demuestra que **cada escalación de privilegios queda documentada** en los logs de seguridad, lo cual es una manifestación directa del principio de Locard en el entorno digital.

**Evidencia visual:**

> **📸 Captura 7:** Event ID 4611 (Security System Extension — ConsentUI) generado al abrir PowerShell como Administrador. Se observa la ventana de propiedades del evento con los detalles del proceso de confianza, y la terminal de PowerShell con permisos elevados en segundo plano.

![Captura 7 - Evento 4611 detalle](../img/07_evento_4611_detalle.png)

---

### 7.3 Evento: Creación de Cuenta de Usuario (Event ID 4720)

**Tipo de evento:** Auditoría correcta — User Account Management  
**Registro:** Seguridad  
**Nivel de sospecha:** 🔴 Alto  

**Descripción del hallazgo:**

Se detectó la creación de una nueva cuenta de usuario en el sistema. En un contexto forense, la creación de cuentas no autorizadas es un indicador de que el atacante está estableciendo un **mecanismo de persistencia** (backdoor) para poder volver a acceder al sistema.

La cuenta fue creada mediante el comando `net user UsuarioPrueba Password123! /add` ejecutado desde una terminal de PowerShell con privilegios de administrador. El sistema registró este evento de forma inmediata, capturando tanto al sujeto que ejecutó la acción como los datos de la nueva cuenta.

Adicionalmente, al crear la cuenta, Windows generó automáticamente el **Event ID 4728** ("Se agregó un miembro a un grupo global con seguridad habilitada"), registrando que UsuarioPrueba fue añadido al grupo "Ninguno" del equipo MELQUI. Esto demuestra que una sola acción del usuario (crear cuenta) genera múltiples rastros forenses en los logs.

| Campo | Valor |
|-------|-------|
| **ID del evento** | 4720 |
| **Fecha y hora** | 15/2/2026 20:57:16 |
| **Categoría de tarea** | User Account Management |
| **Cuenta creada** | UsuarioPrueba |
| **Dominio de cuenta creada** | MELQUI |
| **Creada por (Sujeto)** | melqui.romero (SENA\melqui.romero) |
| **Id. de inicio de sesión del sujeto** | 0xF2F83D8 |
| **Equipo** | MELQUI |

| Campo (Evento asociado 4728) | Valor |
|------|-------|
| **ID del evento** | 4728 |
| **Fecha y hora** | 15/2/2026 20:57:16 |
| **Miembro agregado** | MELQUI\UsuarioPrueba |
| **Grupo destino** | Ninguno (MELQUI\Ninguno) |
| **Acción realizada por** | melqui.romero (SENA) |

**Posible interpretación forense:**

La creación de una cuenta de usuario sin justificación legítima es una técnica de persistencia empleada por atacantes. Permite:
- Mantener acceso al sistema incluso si la contraseña del usuario original es cambiada
- Operar bajo una cuenta diferente para dificultar la investigación
- Escalar privilegios si la cuenta es añadida a grupos de administradores

El evento complementario 4728 confirma que el sistema automatiza la adición del nuevo usuario a grupos, lo cual genera evidencia forense adicional que el atacante podría no anticipar.

**Evidencia visual:**

> **📸 Captura 8:** Terminal de PowerShell mostrando la ejecución del comando `net user UsuarioPrueba Password123! /add` con el mensaje "Se ha completado el comando correctamente". En la parte superior se observa el popup del Event ID 4720 confirmando la creación de la cuenta, con el sujeto SENA\melqui.romero y la nueva cuenta MELQUI\UsuarioPrueba.

![Captura 8 - Crear usuario y evento 4720](../img/08_crear_usuario_cmd.png)

> **📸 Captura 10:** Detalles del Event ID 4728 ("Se agregó un miembro a un grupo global con seguridad habilitada"). Muestra que UsuarioPrueba fue añadido automáticamente al grupo Ninguno del equipo MELQUI como parte del proceso de creación de la cuenta.

![Captura 10 - Evento 4728 detalle](../img/10_evento_4728_detalle.png)

---

### 7.4 Evento: Eliminación de Cuenta de Usuario (Event ID 4726)

**Tipo de evento:** Auditoría correcta — User Account Management  
**Registro:** Seguridad  
**Nivel de sospecha:** 🔴 Alto  

**Descripción del hallazgo:**

Se detectó la eliminación de la cuenta de usuario que había sido creada previamente. Esto indica un intento de **destrucción de evidencia**: el atacante crea una cuenta para operar y luego la elimina para cubrir sus huellas.

La eliminación se realizó mediante el comando `net user UsuarioPrueba /delete`, apenas **54 segundos después** de la creación (20:57:16 → 20:58:10). Este período extremadamente corto refuerza la interpretación de que la cuenta fue creada con un propósito específico y eliminada rápidamente para dificultar su detección.

De forma análoga a la creación, la eliminación de la cuenta generó automáticamente el **Event ID 4729** ("Se quitó un miembro de un grupo global con seguridad habilitada"), registrando la remoción de UsuarioPrueba del grupo "Ninguno".

| Campo | Valor |
|-------|-------|
| **ID del evento** | 4726 |
| **Fecha y hora** | 15/2/2026 20:58:10 |
| **Categoría de tarea** | User Account Management |
| **Cuenta eliminada** | UsuarioPrueba |
| **Eliminada por (Sujeto)** | melqui.romero (SENA\melqui.romero) |
| **Equipo** | MELQUI |
| **Tiempo entre creación y eliminación** | 54 segundos |

| Campo (Evento asociado 4729) | Valor |
|------|-------|
| **ID del evento** | 4729 |
| **Fecha y hora** | 15/2/2026 20:58:10 |
| **Miembro removido** | MELQUI\UsuarioPrueba |
| **Grupo** | Ninguno (MELQUI\Ninguno) |
| **Acción realizada por** | melqui.romero (SENA) |

**Posible interpretación forense:**

La eliminación de una cuenta recién creada es un indicador clásico de actividad anti-forense. Sin embargo, como demuestra el principio de Locard, esta acción también deja múltiples rastros: el evento 4726 (cuenta eliminada), el evento 4729 (miembro removido de grupo), y la correlación temporal con el evento 4720 (creación). Todos estos registros permiten al investigador reconstruir la secuencia completa de acciones del atacante.

**Evidencia visual:**

> **📸 Captura 9:** Terminal de PowerShell mostrando tanto el comando de creación (`net user UsuarioPrueba Password123! /add`) como de eliminación (`net user UsuarioPrueba /delete`), ambos con el mensaje "Se ha completado el comando correctamente". En la parte izquierda se observa la lista de eventos de seguridad con los Event IDs 4672 (Special Logon), 4624 (Logon), 4726 (User Account Management) y 4729 (Security Group Management) generados por estas acciones.

![Captura 9 - Eliminar usuario y lista de eventos](../img/09_eliminar_usuario_cmd.png)

> **📸 Captura 11:** Detalles del Event ID 4729 ("Se quitó un miembro de un grupo global con seguridad habilitada"). Muestra que UsuarioPrueba fue removido automáticamente del grupo Ninguno al eliminar la cuenta.

![Captura 11 - Evento 4729 detalle](../img/11_evento_4729_detalle.png)

---

### 7.5 Evento: Instalación de Servicio del Sistema (Event ID 4697)

**Tipo de evento:** Auditoría correcta — Security System Extension  
**Registro:** Seguridad  
**Nivel de sospecha:** 🔴 Alto  

**Descripción del hallazgo:**

Se detectó la instalación de un nuevo servicio en el sistema. Los atacantes frecuentemente instalan servicios maliciosos para lograr **persistencia**, es decir, que su malware se ejecute automáticamente cada vez que el sistema se inicie.

En este caso, el servicio fue creado mediante el comando `sc.exe create ServicioPrueba binPath= "C:\Windows\System32\cmd.exe" start= demand` y posteriormente eliminado con `sc.exe delete ServicioPrueba`. Windows registró esta instalación como **Event ID 4697** ("Se instaló un servicio en el sistema") en el registro de Seguridad, con categoría "Security System Extension".

> **Nota técnica:** La instalación de servicios puede registrarse como Event ID 7045 en el registro de Sistema o como Event ID 4697 en el registro de Seguridad, dependiendo de la configuración de auditoría del sistema. En este equipo, el registro se capturó en Seguridad como Event ID 4697, lo cual proporciona información adicional sobre el sujeto que realizó la instalación.

| Campo | Valor |
|-------|-------|
| **ID del evento** | 4697 |
| **Fecha y hora** | 15/2/2026 21:13:32 |
| **Categoría de tarea** | Security System Extension |
| **Nombre del servicio** | ServicioPrueba |
| **Ruta del archivo del servicio** | C:\Windows\System32\cmd.exe |
| **Tipo de servicio** | 0x10 (propio) |
| **Tipo de inicio del servicio** | 3 (demand / bajo demanda) |
| **Cuenta de servicio** | LocalSystem |
| **Instalado por (Sujeto)** | melqui.romero (SENA\melqui.romero) |
| **Id. de inicio de sesión** | 0xF2F83D8 |
| **Equipo** | MELQUI |

**Posible interpretación forense:**

La instalación de un servicio desconocido o con una ruta de archivo sospechosa es un fuerte indicador de compromiso. En este caso, el servicio apunta directamente a `cmd.exe`, lo cual es altamente sospechoso ya que:
- `cmd.exe` es el intérprete de comandos de Windows, no un servicio legítimo
- Un atacante podría usar este mecanismo para ejecutar comandos arbitrarios con privilegios de SYSTEM
- La cuenta de servicio es **LocalSystem**, el nivel más alto de privilegios en Windows
- El tipo de inicio "demand" indica que el servicio se ejecutaría cuando sea invocado, lo cual permite al atacante activar su payload en el momento deseado

El investigador forense debe verificar si la ruta del ejecutable corresponde a software legítimo y si existe correlación temporal con otros eventos sospechosos.

**Evidencia visual:**

> **📸 Captura 12:** Terminal de PowerShell mostrando la creación exitosa del servicio (`[SC] CreateService CORRECTO`) y su eliminación posterior (`[SC] DeleteService CORRECTO`). En la parte izquierda se observa el registro de Seguridad con 20.892 eventos, donde se aprecian los Event IDs 4662, 5061 y 4672 generados durante el proceso.

![Captura 12 - Crear y eliminar servicio](../img/12_crear_servicio_cmd.png)

> **📸 Captura 13:** Detalles del Event ID 4697 ("Se instaló un servicio en el sistema"). Se observa la información completa del servicio: nombre "ServicioPrueba", ruta del archivo "C:\Windows\System32\cmd.exe", tipo de servicio 0x10, tipo de inicio 3, cuenta de servicio LocalSystem, instalado por SENA\melqui.romero.

![Captura 13 - Evento 4697 detalle](../img/13_evento_4697_detalle.png)

---

### 7.6 Evento: Borrado del Registro de Auditoría (Event ID 1102)

**Tipo de evento:** Auditoría correcta — Log clear  
**Registro:** Seguridad  
**Nivel de sospecha:** 🔴 Crítico  

**Descripción del hallazgo:**

Se detectó que los registros de auditoría de seguridad fueron **borrados intencionalmente** mediante el comando `wevtutil cl Security` ejecutado desde PowerShell con privilegios de administrador. Este es quizas el evento más crítico desde el punto de vista forense, ya que indica que alguien intentó eliminar toda evidencia de sus acciones previas. Es una técnica **anti-forense** directa.

Tras la ejecución del comando, el registro de Seguridad quedó con **únicamente 1 evento**: el propio Event ID 1102 que documenta el borrado. Esto confirma la destrucción exitosa de todos los registros anteriores.

| Campo | Valor |
|-------|-------|
| **ID del evento** | 1102 |
| **Fecha y hora** | 15/2/2026 21:23:32 |
| **Categoría de tarea** | Log clear |
| **Origen** | Eventlog |
| **Usuario que borró los logs** | melqui.romero (SENA\melqui.romero) |
| **Id. de inicio de sesión** | 0xF2F83D8 |
| **Equipo** | MELQUI |
| **Eventos restantes después del borrado** | 1 (solo el propio 1102) |

**Posible interpretación forense:**

El borrado de registros de auditoría es una de las acciones más sospechosas que se pueden encontrar en un análisis forense. Paradójicamente, el propio sistema Windows genera un evento (1102) que registra esta acción, lo cual es un ejemplo perfecto del principio de Locard: **incluso el intento de eliminar los rastros deja un rastro**.

En una investigación real, este hallazgo indicaría con alta probabilidad que:
- El sistema fue comprometido por un atacante
- El atacante era consciente de que sus acciones quedaban registradas
- El atacante poseía privilegios de administrador (necesarios para borrar logs)
- Toda la evidencia previa al borrado de logs fue destruida (se necesitarían técnicas de recuperación avanzadas o fuentes de evidencia alternativas)

Es relevante notar que el Id. de inicio de sesión (0xF2F83D8) coincide con el de los eventos 4720, 4726 y 4697, lo que confirma que **todas estas acciones fueron realizadas dentro de la misma sesión de usuario**, formando una cadena de ataque coherente.

**Evidencia visual:**

> **📸 Captura 14:** Event ID 1102 ("Se borró el registro de auditoría") mostrando que el registro de Seguridad quedó con un único evento después del borrado. En la ventana de propiedades se observa el origen "Eventlog", categoría "Log clear", usuario melqui.romero (SENA), registrado el 15/2/2026 a las 21:23:32. En la terminal de PowerShell de fondo se visualiza el comando `wevtutil cl Security` que provocó el borrado.

![Captura 14 - Evento 1102 detalle](../img/14_evento_1102_detalle.png)

---

## 8. Línea de Tiempo del Incidente

A continuación, se presenta la reconstrucción cronológica del incidente basada en los eventos analizados:

| # | Fecha y hora | Evento | Interpretación |
|---|-------------|--------|----------------|
| 1 | 14/2/2026 21:20 | Inicio de sesión en horario nocturno (4624) | Acceso sospechoso fuera de jornada laboral |
| 2 | 14/2/2026 21:30 | Segundo inicio de sesión nocturno (4624) | Patrón de accesos repetidos en horario inusual |
| 3 | 14/2/2026 21:35 | Tercer inicio de sesión nocturno (4624) | Actividad sostenida fuera de horario |
| 4 | 15/2/2026 17:02 | Elevación de privilegios UAC (4611) | Escalación de privilegios mediante ConsentUI |
| 5 | 15/2/2026 20:57 | Cuenta de usuario creada (4720) + Miembro agregado a grupo (4728) | Creación de backdoor para acceso futuro |
| 6 | 15/2/2026 20:58 | Cuenta de usuario eliminada (4726) + Miembro removido de grupo (4729) | Destrucción de evidencia — 54 seg. después de la creación |
| 7 | 15/2/2026 21:13 | Servicio instalado en el sistema (4697) | Instalación de servicio sospechoso apuntando a cmd.exe |
| 8 | 15/2/2026 21:23 | Registros de auditoría borrados (1102) | Técnica anti-forense para eliminar toda evidencia |
| 9 | 14/2/2026 23:19 | Cierre de sesión (4634) | Fin de la actividad sospechosa |

Esta secuencia de eventos sigue un patrón de ataque conocido como **kill chain** o cadena de ataque:
1. **Acceso inicial** → Inicios de sesión en horarios nocturnos inusuales (posible acceso no autorizado)
2. **Escalación de privilegios** → Obtención de privilegios de administrador
3. **Persistencia** → Creación de cuentas backdoor e instalación de servicios
4. **Limpieza de huellas** → Eliminación de cuentas temporales y borrado de logs

---

## 9. Conclusiones

1. **Aplicación del principio de Locard:** El análisis realizado demuestra que el principio de intercambio de Locard se aplica plenamente en el entorno digital. Cada acción ejecutada en el sistema —desde un inicio de sesión hasta el borrado de registros— dejó un rastro identificable en los logs del sistema operativo. El equipo MELQUI registró más de 21.000 eventos de seguridad y 28.000 eventos de sistema, demostrando que Windows documenta exhaustivamente toda la actividad. Incluso las técnicas anti-forense como el borrado de logs generan su propio evento (ID 1102), confirmando que "todo contacto deja un rastro".

2. **Valor forense del Visor de Eventos:** El Event Viewer de Windows demostró ser una herramienta fundamental para la investigación forense de primer nivel. Los registros de Seguridad y Sistema proporcionan información detallada y cronológica de las acciones realizadas en el equipo, permitiendo la reconstrucción de la secuencia de eventos de un incidente.

3. **Detección de patrones de acceso sospechoso:** Se identificaron múltiples inicios de sesión (Event ID 4624) en horarios nocturnos inusuales, particularmente el 14/2/2026 entre las 21:20 y las 21:35, con un cierre de sesión a las 23:19. Este patrón, que se desvía del comportamiento habitual del usuario durante jornada diurna, constituye un indicador de compromiso (IoC) que en una investigación real requeriría correlación con otras fuentes de evidencia.

4. **Identificación de técnicas de ataque:** Las pruebas de simulación forense evidenciaron que un atacante con acceso al sistema puede elevar privilegios mediante UAC (4611), crear cuentas de backdoor (4720/4728), instalar servicios maliciosos (4697) y borrar registros de auditoría (1102). Este patrón corresponde al modelo de la **kill chain** descrito en la literatura de ciberseguridad (De Haro Olmo, 2020). Además, se comprobó que cada acción genera múltiples eventos complementarios (e.g., 4720+4728, 4726+4729), lo que multiplica las fuentes de evidencia disponibles para el investigador.

5. **Importancia de la cadena de custodia:** La documentación rigurosa de cada evento con capturas de pantalla, timestamps, IDs de eventos y descripción técnica es esencial para mantener la validez probatoria de la evidencia digital. Como señala Luna Felipez (s.f.), el perito informático forense debe garantizar la integridad de la evidencia para que sea admisible en un proceso judicial.

6. **Necesidad de monitoreo continuo:** Los hallazgos evidencian la importancia de implementar sistemas de monitoreo y alertas que detecten en tiempo real patrones sospechosos como accesos en horarios inusuales, escalación de privilegios, creación de cuentas no autorizadas o borrado de logs. La configuración adecuada de las políticas de auditoría (mediante herramientas como `auditpol`) es esencial para garantizar que TODOS los eventos relevantes queden registrados.



---

## 10. Bibliografía

- De Haro Olmo, F. J. (2020). *Crimen, cibercrimen y análisis forense informático*. I.E.S. Celia Viñas. Recuperado de https://iescelia.org/ciberseguridad/ceceti-afi-00

- Luna Felipez, J. P. (s.f.). *Perito Informático Judicial Forense*. Universidad Nacional "Siglo XX", Llallagua, Bolivia.

- Areito, G. (2008). *Seguridad de la Información: Redes, Informática y Sistemas de Información*.

- Microsoft. (2024). *Windows Security auditing*. Microsoft Learn. Recuperado de https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/

- NIST. (2012). *Guide to Computer Security Log Management (SP 800-92)*. National Institute of Standards and Technology.




