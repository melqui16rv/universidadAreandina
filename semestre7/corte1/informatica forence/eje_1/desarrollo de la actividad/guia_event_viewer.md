# GUÍA PASO A PASO: Cómo usar Event Viewer (Visor de Eventos) en Windows

Esta guía te llevará desde cero hasta capturar todos los eventos que necesitas para tu actividad de informática forense. Sigue cada paso en orden.

---

## Parte 1: Abrir el Visor de Eventos

### Paso 1 — Abrir Event Viewer

1. Presiona las teclas **`Win + R`** (la tecla de Windows + la letra R) al mismo tiempo. Se abrirá una ventana pequeña que dice "Ejecutar".
2. Escribe: **`eventvwr.msc`**
3. Presiona **Enter** o haz clic en "Aceptar".

> **📸 CAPTURA 1:** Toma una captura de pantalla de la ventana "Ejecutar" con `eventvwr.msc` escrito.  
> Usa **`Win + Shift + S`** para tomar capturas de pantalla y guárdalas en la carpeta `eje_1\img\`.

Se abrirá el **Visor de Eventos de Windows** (Event Viewer). Verás una ventana con un panel izquierdo de navegación tipo árbol.

> **📸 CAPTURA 2:** Toma una captura de pantalla de la ventana principal del Visor de Eventos recién abierta.

---

## Parte 2: Navegar por los registros

### Paso 2 — Explorar los Registros de Windows

En el **panel izquierdo**, expande (haz clic en la flecha ▶) la carpeta:

```
Registros de Windows
```

Verás las siguientes subcategorías:
- **Aplicación** — Eventos de programas instalados
- **Seguridad** — Inicios de sesión, cambios de permisos, auditorías
- **Instalación** — Eventos de instalación de Windows
- **Sistema** — Eventos del sistema operativo, servicios, drivers
- **Eventos reenviados** — Eventos de otros equipos

### Paso 3 — Abrir el registro de Seguridad

1. Haz clic en **"Seguridad"** dentro de "Registros de Windows".
2. En el panel central verás una lista de eventos con columnas:
   - **Nivel** (Información, Advertencia, Error)
   - **Fecha y hora**
   - **Origen**
   - **Id. del evento** (este es el Event ID que necesitas documentar)
   - **Categoría de la tarea**

> **📸 CAPTURA 3:** Toma una captura del registro de Seguridad mostrando la lista de eventos.

### Paso 4 — Abrir el registro de Sistema

1. Haz clic en **"Sistema"** dentro de "Registros de Windows".
2. Observa los eventos del sistema. Aquí aparecen eventos de servicios, errores del sistema, instalación de drivers, etc.

> **📸 CAPTURA 4:** Toma una captura del registro de Sistema mostrando la lista de eventos.

---

## Parte 3: Cómo leer un evento individual
********
### Paso 5 — Ver los detalles de un evento

1. Haz **doble clic** en cualquier evento de la lista (o selecciónalo y presiona Enter).
2. Se abrirá una ventana con dos pestañas:
   - **General**: Muestra la descripción del evento en texto legible, incluyendo:
     - Nombre de usuario
     - Tipo de acción
     - Resultado (éxito o error)
   - **Detalles**: Muestra la información técnica en formato XML.

**Lo que debes anotar de cada evento:**

| Campo | Dónde encontrarlo |
|-------|-------------------|
| **ID del evento** | Columna "Id. del evento" en la lista, o en la parte superior de la ventana de detalles |
| **Fecha y hora** | Columna "Fecha y hora" en la lista |
| **Usuario** | En la pestaña "General", busca "Nombre de cuenta" o "Cuenta de sujeto" |
| **Descripción** | Texto de la pestaña "General" |

---

## Parte 3.5: IMPORTANTE — Habilitar auditoría de errores de inicio de sesión

> ⚠️ **HACER ESTO ANTES DE LAS PRUEBAS (si quieres intentar la Prueba 2 opcional).** Por defecto, Windows puede NO registrar los inicios de sesión fallidos (Event ID 4625). Si no habilitas esto, la Prueba 2 (opcional) no generará eventos.

### Paso 6 — Habilitar la auditoría de errores

1. Abre **PowerShell como Administrador**:
   - Haz clic derecho en el botón de **Inicio** de Windows.
   - Selecciona **"Windows PowerShell (Administrador)"** o **"Terminal (Administrador)"**.
   - Haz clic en **"Sí"** en la ventana de control de cuentas.

2. Escribe el siguiente comando y presiona Enter:

```powershell
auditpol /set /subcategory:"Logon" /success:enable /failure:enable
```

3. Deberías ver: **"El comando se ejecutó correctamente."**

4. Para verificar que se aplicó, escribe:

```powershell
auditpol /get /subcategory:"Logon"
```

5. Deberías ver algo como:

```
  Logon                                     Correcto y erróneo
```

> Si el comando del paso 2 da error porque tu Windows está en español, intenta con:
> ```powershell
> auditpol /set /subcategory:"Inicio de sesión" /success:enable /failure:enable
> ```

> **📸 CAPTURA 5b (opcional):** Toma una captura mostrando el resultado del comando auditpol.

**¡Listo!** Ahora sí Windows registrará los inicios de sesión fallidos. Continúa con las pruebas.

---

## Parte 4: Provocar eventos de prueba para el ejercicio

Ahora vas a provocar eventos "sospechosos" en tu propio equipo para tener evidencia que documentar. Esto es completamente seguro.

### Prueba 1 — Analizar inicios de sesión en horarios inusuales (Event ID 4624)

Este es el análisis principal del ejercicio. Vas a revisar los eventos de inicio de sesión exitoso (4624) y cierre de sesión (4634) para identificar **accesos en horarios sospechosos** (nocturnos, madrugada, fines de semana).

1. Ve a **Registros de Windows > Seguridad**.
2. En el panel derecho, haz clic en **"Filtrar registro actual..."**
3. En el campo **"Id. del evento"** escribe: **4624,4634** (separados por coma, sin espacios).
4. Haz clic en **Aceptar**. Se mostrarán todos los inicios y cierres de sesión.

> **📸 CAPTURA 5:** Toma una captura mostrando la lista filtrada de eventos 4624 y 4634 con sus fechas y horas.  
> Guárdala como `05_eventos_logon.png`

5. Revisa las **fechas y horas** de cada evento. Busca inicios de sesión en horarios inusuales:
   - Después de las 21:00 horas (nocturnos)
   - Antes de las 7:00 horas (madrugada)
   - Fines de semana si el equipo es de uso laboral

6. Haz **doble clic** en uno de los eventos 4624 con horario sospechoso para ver sus detalles.

> **📸 CAPTURA 6:** Toma una captura de los eventos 4624 que tengan horarios sospechosos, resaltando las horas nocturnas.  
> Guárdala como `06_eventos_logon_sospechosos.png`

**¿Por qué esto es importante?**

Los inicios de sesión en horarios fuera de la jornada laboral son uno de los principales **indicadores de compromiso** (IoC) en informática forense. Si un equipo normalmente se usa entre las 8:00 y las 18:00, y de repente aparecen accesos a las 21:00 o 23:00, puede indicar que un atacante accedió al sistema.

---

### Prueba 2 (OPCIONAL) — Generar un inicio de sesión fallido (Event ID 4625)

> ⚠️ Este evento puede **NO aparecer** en todos los sistemas Windows. Si no aparece después de seguir los pasos, no te preocupes — el análisis de horarios inusuales (Prueba 1) es suficiente para el documento.

> ⚠️ **REQUISITO:** Asegúrate de haber completado el **Paso 6** (habilitar auditoría) ANTES de hacer esta prueba.

1. Presiona **`Win + L`** para bloquear tu sesión de Windows.
2. En la pantalla de inicio de sesión, **escribe una contraseña incorrecta** a propósito.
3. Presiona Enter. Verás un mensaje de "Contraseña incorrecta".
4. **Repite esto 3 veces** para generar múltiples intentos fallidos.
5. Ahora ingresa tu **contraseña correcta** para volver al escritorio.

**Verificar el evento:**
1. Ve a **Registros de Windows > Seguridad**.
2. Filtra por **Id. del evento: 4625**
3. Si aparecen eventos, toma capturas. Si NO aparecen, salta esta prueba.

---

### Prueba 3 — Asignación de privilegios especiales (Event ID 4672)

Este evento se genera cuando un usuario inicia sesión con privilegios de administrador.

1. Haz clic derecho en el botón de **Inicio** de Windows (esquina inferior izquierda).
2. Selecciona **"Windows PowerShell (Administrador)"** o **"Terminal (Administrador)"**.
3. Si te aparece una ventana de control de cuentas de usuario (UAC), haz clic en **"Sí"**.
4. Se abrirá una ventana de PowerShell con permisos elevados. Puedes cerrarla después.

**Verificar el evento:**
1. En **Registros de Windows > Seguridad**, busca eventos con **Id. del evento: 4672**.

> **📸 CAPTURA 7:** Toma una captura del evento 4672 mostrando la asignación de privilegios especiales.
> Guárdala como `07_evento_4611_detalle.png`

---

### Prueba 4 — Crear y eliminar un usuario temporal (Event IDs 4720 y 4726)

Esto simula la creación sospechosa de una cuenta de usuario (algo que un atacante podría hacer).

1. Abre **PowerShell como Administrador** (como en la Prueba 3).
2. Escribe el siguiente comando para **crear un usuario temporal**:

```powershell
net user UsuarioPrueba Password123! /add
```

3. Presiona Enter. Verás un mensaje: "El comando se completó correctamente".

> **📸 CAPTURA 8:** Toma una captura de la terminal mostrando el comando y el resultado.
> Guárdala como `08_crear_usuario_cmd.png`

4. Ahora **elimina ese usuario** para limpiar:

```powershell
net user UsuarioPrueba /delete
```

5. Presiona Enter. Verás nuevamente: "El comando se completó correctamente".

> **📸 CAPTURA 9:** Toma una captura de la terminal mostrando la eliminación.
> Guárdala como `09_eliminar_usuario_cmd.png`

**Verificar los eventos:**
1. En **Registros de Windows > Seguridad**, busca:
   - **Id. del evento: 4720** → Se creó una cuenta de usuario.
   - **Id. del evento: 4726** → Se eliminó una cuenta de usuario.

> **📸 CAPTURA 10:** Toma una captura del evento 4720 (cuenta creada) con sus detalles.  
> Guárdala como `10_evento_4720_detalle.png`  
> **📸 CAPTURA 11:** Toma una captura del evento 4726 (cuenta eliminada) con sus detalles.
> Guárdala como `11_evento_4726_detalle.png`

---

### Prueba 5 — Instalación de un servicio (Event ID 7045)

Este evento aparece en el registro de **Sistema** y puede indicar que un atacante instaló software malicioso.

1. En la ventana de **PowerShell como Administrador**, escribe:

```powershell
sc.exe create ServicioPrueba binPath= "C:\Windows\System32\cmd.exe" start= demand
```

2. Presiona Enter. Verás: "[SC] CreateService SUCCESS".

> **📸 CAPTURA 12:** Toma una captura de la terminal mostrando la creación del servicio.
> Guárdala como `12_crear_servicio_cmd.png`

3. **Elimina el servicio** inmediatamente:

```powershell
sc.exe delete ServicioPrueba
```

4. Presiona Enter. Verás: "[SC] DeleteService SUCCESS".

**Verificar el evento:**
1. Ve a **Registros de Windows > Sistema**.
2. Busca eventos con **Id. del evento: 7045** → Se instaló un servicio en el sistema.

> **📸 CAPTURA 13:** Toma una captura del evento 7045 con sus detalles.
> Guárdala como `13_evento_7045_detalle.png`

---

### Prueba 6 — Borrado de logs de auditoría (Event ID 1102)

Este es un evento MUY sospechoso: indica que alguien limpió los registros de seguridad (un atacante haría esto para cubrir sus huellas).

1. En la ventana de **PowerShell como Administrador**, escribe:

```powershell
wevtutil cl Security
```

> ⚠️ **IMPORTANTE:** Este comando borrará los registros de seguridad anteriores. Asegúrate de haber tomado TODAS las capturas de las pruebas anteriores ANTES de ejecutar este comando.

2. Presiona Enter. No mostrará mensaje, pero los logs se habrán borrado.

**Verificar el evento:**
1. Ve a **Registros de Windows > Seguridad**.
2. Ahora verás muy pocos eventos. Busca el **Id. del evento: 1102** → El registro de auditoría fue borrado.
3. Este evento se genera automáticamente incluso DESPUÉS de borrar los demás logs.

> **📸 CAPTURA 14:** Toma una captura del evento 1102 mostrando que se borró el registro de auditoría.
> Guárdala como `14_evento_1102_detalle.png`

---

## Parte 5: Cómo filtrar eventos (Tip útil)

Si hay muchos eventos y no encuentras los que buscas:

### Opción A — Filtrar el registro actual

1. En el panel derecho (Acciones), haz clic en **"Filtrar registro actual..."**
2. En el campo **"Id. del evento"**, escribe el número del evento que buscas (ej: `4624`).
3. Haz clic en **Aceptar**. Solo se mostrarán eventos con ese ID.
4. Para quitar el filtro: haz clic en **"Borrar filtro"** en el panel de Acciones.

> **📸 CAPTURA 15 (opcional):** Toma una captura de la ventana de filtrado mostrando cómo filtrar por ID.

### Opción B — Buscar un evento

1. En el panel derecho, haz clic en **"Buscar..."**
2. Escribe el texto o ID que buscas.
3. Haz clic en "Buscar siguiente".

---

## Parte 6: Tabla resumen de Event IDs importantes

| Event ID | Registro | Significado | Nivel de sospecha |
|----------|----------|-------------|-------------------|
| **4624** | Seguridad | Inicio de sesión exitoso | 🟡 Medio (revisar horario) |
| **4625** | Seguridad | Inicio de sesión fallido | 🔴 Alto |
| **4672** | Seguridad | Privilegios especiales asignados a nuevo inicio de sesión | 🔴 Alto |
| **4720** | Seguridad | Se creó una cuenta de usuario | 🔴 Alto |
| **4726** | Seguridad | Se eliminó una cuenta de usuario | 🔴 Alto |
| **4732** | Seguridad | Un miembro fue agregado a un grupo local de seguridad | 🔴 Alto |
| **7045** | Sistema | Se instaló un servicio en el sistema | 🔴 Alto |
| **1102** | Seguridad | El registro de auditoría fue borrado | 🔴 Crítico |
| **4688** | Seguridad | Se creó un nuevo proceso | 🟡 Medio |
| **4697** | Seguridad | Se intentó instalar un servicio | 🔴 Alto |

---

## Orden recomendado para hacer las pruebas

1. ✅ Abre Event Viewer y toma capturas generales (Capturas 1-4)
2. ✅ Prueba 1: Analizar inicios de sesión en horarios inusuales (Capturas 5-6)
3. ⚠️ Prueba 2 (OPCIONAL): Intento de inicio de sesión fallido
4. ✅ Prueba 3: Abrir PowerShell como admin (Captura 7)
5. ✅ Prueba 4: Crear/eliminar usuario temporal (Capturas 8-11)
6. ✅ Prueba 5: Crear/eliminar servicio de prueba (Capturas 12-13)
7. ⚠️ Prueba 6: Borrar logs de auditoría — **HACER AL FINAL** (Captura 14)
8. ✅ (Opcional) Captura de filtrado (Captura 15)

---

## Cómo guardar las capturas

1. Usa **`Win + Shift + S`** para seleccionar el área de la pantalla.
2. La captura se copia al portapapeles. Abre **Paint** (busca "Paint" en el menú Inicio).
3. Presiona **`Ctrl + V`** para pegar.
4. Guarda con **`Ctrl + S`** en la carpeta:  
   `eje_1\img\` con nombres descriptivos como:
   - `01_abrir_event_viewer.png`
   - `02_visor_eventos_principal.png`
   - `03_registro_seguridad.png`
   - `04_registro_sistema.png`
   - `05_eventos_logon.png`
   - `06_eventos_logon_sospechosos.png`
   - `07_evento_4672_detalle.png`
   - `08_crear_usuario_cmd.png`
   - `09_eliminar_usuario_cmd.png`
   - `10_evento_4720_detalle.png`
   - `11_evento_4726_detalle.png`
   - `12_crear_servicio_cmd.png`
   - `13_evento_7045_detalle.png`
   - `14_evento_1102_detalle.png`
   - `15_filtrado_eventos.png` (opcional)

> **Tip:** También puedes usar la tecla **`PrtSc`** (Print Screen) para capturar toda la pantalla, o **`Alt + PrtSc`** para capturar solo la ventana activa.
