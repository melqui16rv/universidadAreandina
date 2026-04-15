# GUÍA PASO A PASO - EJE 3

## Análisis forense del Registro de Windows con FTK Imager

Esta guía te lleva desde cero hasta tener todas las capturas y el informe listo para entregar.  
Sigue cada paso en orden. No saltes capturas.

**Rutas obligatorias que debes analizar (según la actividad):**

- `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`

---

## Parte 1: Preparación del entorno

### Paso 1 — Preparar el equipo de trabajo

1. Usa el equipo donde harás el análisis (puede ser tu PC principal o una VM).
2. Cierra todas las aplicaciones que no necesites.
3. Crea la carpeta de capturas si no existe:  
   `c:\github\uni\informatica forence\eje_3\img\`
4. Ten abierto el Explorador de archivos apuntando a esa carpeta para guardar capturas fácilmente.

> **📸 CAPTURA 1:** Toma una captura del escritorio con la carpeta `img` abierta o visible.  
> Guárdala como `01_entorno_preparado.png`  
> Usa **`Win + Shift + S`** para capturar, luego pégala en Paint y guarda.

---

### Paso 2 — Instalar y abrir FTK Imager

1. Descarga **FTK Imager** desde el portal oficial de Exterro (es gratuito, no requiere licencia).
   - Versión recomendada: la más reciente disponible (4.7.x o superior).
   - El archivo es un instalador `.exe` de nombre similar a `FTKImager.exe`.
2. Ejecuta el instalador con opciones por defecto (Next → Next → Install).
3. Al terminar, busca **FTK Imager** en el menú Inicio.
4. Haz **clic derecho → Ejecutar como administrador**. Confirma en el diálogo de UAC.

> **📸 CAPTURA 2:** Toma una captura que muestre la versión de FTK Imager instalada.  
> Puedes verla en: menú `Help > About FTK Imager`.  
> Guárdala como `02_ftk_instalado_version.png`

> **📸 CAPTURA 3:** Toma una captura de la ventana principal de FTK Imager recién abierta.  
> Deben verse: panel izquierdo (árbol de evidencia), panel central (contenido) y panel inferior (vista hex).  
> Guárdala como `03_ftk_interfaz_principal.png`

---

## Parte 2: Cargar la evidencia en FTK Imager

### Paso 3 — Definir las rutas objetivo antes de navegar

Antes de agregar la evidencia, escribe o imprime las dos rutas que vas a buscar. Esto te ayuda a navegar sin perderte:

| # | Ruta del Registro | Qué buscas |
|---|---|---|
| 1 | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` | Programas que se inician automáticamente al encender el equipo |
| 2 | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | Documentos abiertos recientemente por el usuario |

> **📸 CAPTURA 4:** Toma una captura de esta tabla o de un documento donde tengas escritas las dos rutas.  
> Guárdala como `04_rutas_objetivo_registro.png`

---

### Paso 4 — Agregar la evidencia (unidad del sistema)

1. En FTK Imager, ve al menú: **`File > Add Evidence Item...`**
2. En el diálogo que se abre, selecciona el tipo de evidencia:
   - Si analizas el equipo en vivo: elige **`Logical Drive`**
   - Si tienes una imagen forense `.dd` o `.E01`: elige **`Image File`**
3. Haz clic en **Next**.
4. Selecciona la unidad del sistema (normalmente `C:\` o el disco donde está Windows).
5. Haz clic en **Finish**.

Verás que en el panel izquierdo aparece la unidad cargada como un árbol expandible.

> **📸 CAPTURA 5:** Toma una captura que muestre el diálogo **"Add Evidence Item"** con la opción seleccionada.  
> Guárdala como `05_add_evidence_item.png`

> **📸 CAPTURA 6:** Toma una captura que muestre la unidad ya cargada en el árbol de evidencia (panel izquierdo).  
> Guárdala como `06_unidad_sistema_cargada.png`

---

## Parte 3: Navegar al Registro de Windows (hives)

### Paso 5 — Ubicar el hive SOFTWARE (para HKLM)

Los archivos hive del Registro están en:

```
[Unidad]\Windows\System32\config\
```

En el árbol de FTK Imager:
1. Expande la unidad cargada (clic en el triángulo ▶).
2. Navega por: `[raíz] > Windows > System32 > config`
3. Dentro de `config` verás archivos como: `SOFTWARE`, `SYSTEM`, `SAM`, `SECURITY`, `DEFAULT`.
4. Haz clic en el archivo **`SOFTWARE`** (sin extensión). En el panel central aparecerá su contenido.

> **📸 CAPTURA 7:** Toma una captura que muestre la ruta `Windows\System32\config` expandida en el árbol  
> y el archivo `SOFTWARE` visible o seleccionado.  
> Guárdala como `07_hive_software_ubicado.png`

> **📸 CAPTURA 8:** Haz clic en el archivo `SOFTWARE` y toma una captura del panel de contenido/detalle  
> mostrando la información del hive (tamaño, metadatos o vista hex).  
> Guárdala como `08_hive_software_detalle.png`

---

## Parte 4: Análisis de la clave Run (persistencia)

### Paso 6 — Exportar y analizar el hive SOFTWARE

Para examinar las claves del Registro con FTK Imager debes **exportar el hive** y luego abrirlo con el Editor del Registro de forma offline, o usar la vista integrada de FTK si está disponible.

**Método A — Exportar el hive y montarlo (recomendado):**

1. Haz clic derecho sobre el archivo `SOFTWARE` en el árbol de FTK Imager.
2. Selecciona **`Export Files...`**
3. Guarda el hive en una carpeta temporal, por ejemplo: `C:\forense_temp\SOFTWARE`
4. Abre el **Editor del Registro** (`Win + R` → escribe `regedit` → Enter).
5. Selecciona la clave raíz **`HKEY_LOCAL_MACHINE`**.
6. Ve al menú: `Archivo > Cargar subárbol...`
7. Navega hasta `C:\forense_temp\SOFTWARE` y ábrelo.
8. Asígnale un nombre provisional, por ejemplo: `ANALISIS_EJE3`.

Ahora puedes navegar en el Editor del Registro como si fuera el sistema analizado, **sin modificar el original**.

**Método B — Usar Registry Viewer integrado de FTK (si disponible):**

1. En FTK Imager, con el hive `SOFTWARE` seleccionado, busca la opción  
   **`File > Obtain Protected Files...`** o el visor de registro integrado.
2. Navega directamente al hive desde el panel de árbol de FTK.

---

### Paso 7 — Navegar a la clave Run

Una vez tengas acceso al hive (por cualquier método):

1. Navega a:  
   `HKEY_LOCAL_MACHINE\ANALISIS_EJE3\Microsoft\Windows\CurrentVersion\Run`  
   *(o la ruta equivalente si usas el visor integrado de FTK)*

2. En el panel derecho verás un listado de **valores** (entradas). Cada valor tiene:
   - **Nombre**: identificador del programa
   - **Tipo**: normalmente `REG_SZ` o `REG_EXPAND_SZ`
   - **Datos**: ruta completa al ejecutable

3. Lee cada entrada y evalúa:
   - ¿La ruta está en `C:\Program Files\` o `C:\Windows\`? → Probablemente legítimo.
   - ¿La ruta está en `C:\Users\...\AppData\` o carpetas temporales? → Sospechoso.
   - ¿El nombre del valor es una cadena aleatoria o sin sentido? → Muy sospechoso.

> **📸 CAPTURA 9:** Toma una captura que muestre la navegación hasta la clave `Run` con la ruta completa visible.  
> Guárdala como `09_run_key_vista_general.png`

> **📸 CAPTURA 10:** Toma una captura del **listado completo de valores** de la clave Run.  
> Deben verse al menos los nombres, tipos y datos de 2 o más entradas.  
> Guárdala como `10_run_key_valores.png`

> **📸 CAPTURA 11:** Selecciona el valor que te parezca **más atípico o que llame la atención** y toma una captura  
> mostrando su nombre, tipo y datos completos.  
> Si todos parecen legítimos, selecciona el más inusual y explica por qué lo analizas.  
> Guárdala como `11_run_key_posible_sospechoso.png`

---

## Parte 5: Análisis de RecentDocs (actividad de usuario)

### Paso 8 — Ubicar el hive NTUSER.DAT (para HKCU)

La clave `RecentDocs` pertenece al hive de usuario, que está en:

```
C:\Users\[NombreDeUsuario]\NTUSER.DAT
```

En FTK Imager:
1. En el árbol, navega desde la raíz hacia: `Users > [NombreDeUsuario]`
2. Dentro del perfil del usuario verás el archivo **`NTUSER.DAT`**.
3. Haz clic sobre él para seleccionarlo.

> **📸 CAPTURA 12:** Toma una captura que muestre la ubicación de `NTUSER.DAT` dentro del perfil de usuario  
> en el árbol de FTK Imager.  
> Guárdala como `12_ntuser_dat_ubicado.png`

---

### Paso 9 — Exportar y analizar NTUSER.DAT

1. Haz clic derecho sobre `NTUSER.DAT` → **`Export Files...`**
2. Guárdalo en `C:\forense_temp\NTUSER.DAT`
3. En el Editor del Registro, selecciona **`HKEY_USERS`**.
4. Ve a: `Archivo > Cargar subárbol...`
5. Abre `C:\forense_temp\NTUSER.DAT` y nómbralo `USUARIO_EJE3`.
6. Navega a:  
   `HKEY_USERS\USUARIO_EJE3\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`

Aquí verás subclaves organizadas por extensión de archivo (`.pdf`, `.docx`, `.txt`, etc.)  
y la subclave principal `RecentDocs` con las entradas más recientes.

> **📸 CAPTURA 13:** Toma una captura de la navegación hasta `...Explorer\RecentDocs` con la ruta visible.  
> Guárdala como `13_recentdocs_vista_general.png`

> **📸 CAPTURA 14:** Toma una captura del **listado completo de subclaves y valores** en `RecentDocs`.  
> Deben verse las extensiones de archivos o las entradas con sus datos.  
> Guárdala como `14_recentdocs_listado.png`

> **📸 CAPTURA 15:** Entra en una subclave específica (por ejemplo `.pdf` o `.docx`) y toma una captura  
> de un elemento que consideres relevante para el análisis (nombre de archivo reciente, ruta, timestamp).  
> Guárdala como `15_recentdocs_elemento_relevante.png`

---

## Parte 6: Exportación y preservación de evidencia

### Paso 10 — Exportar los artefactos relevantes

Documenta que preservaste la evidencia, no solo que la viste.

**Para la clave Run:**
1. En el Editor del Registro, navega de vuelta a la clave `Run`.
2. Haz clic derecho sobre la clave → **`Exportar...`**
3. Guarda como: `run_key_export.reg` en `C:\forense_temp\`

> **📸 CAPTURA 16:** Toma una captura del proceso de exportación o del archivo `.reg` generado  
> con su nombre y ubicación visibles.  
> Guárdala como `16_exportacion_run_key.png`

**Para RecentDocs:**
1. Navega a la clave `RecentDocs` en el Editor del Registro.
2. Haz clic derecho → **`Exportar...`**
3. Guarda como: `recentdocs_export.reg`

> **📸 CAPTURA 17:** Toma una captura del proceso de exportación del archivo de RecentDocs.  
> Guárdala como `17_exportacion_recentdocs.png`

---

### Paso 11 — Construir la matriz de trazabilidad

Crea una tabla (puede ser en Word, Excel o incluso en un papel fotografiado) con esta estructura:

| # | Fuente (ruta exacta) | Nombre de captura | Hallazgo observado | Hipótesis |
|---|---|---|---|---|
| 1 | `HKLM\..\Run` → valor X | `10_run_key_valores.png` | Ejecutable en ruta no estándar | Posible persistencia |
| 2 | `HKCU\..\RecentDocs` → subclave Y | `15_recentdocs_elemento_relevante.png` | Documento .pdf reciente | Actividad de usuario reciente |

> **📸 CAPTURA 18:** Toma una captura de esta tabla/matriz con al menos 2 filas completadas.  
> Guárdala como `18_matriz_trazabilidad_hallazgos.png`

---

## Parte 7: Análisis y cierre

### Paso 12 — Sintetizar el hallazgo de persistencia

Revisa todas las capturas de la clave `Run` y escribe (en papel o pantalla) un resumen:

- ¿Cuántos valores encontraste?
- ¿Alguno es sospechoso? ¿Por qué?
- ¿Cuál es el riesgo potencial?

> **📸 CAPTURA 19:** Toma una captura de este resumen o del valor de `Run` más relevante  
> con anotaciones o destacado visual de por qué es de interés.  
> Guárdala como `19_hallazgo_persistencia_resumen.png`

---

### Paso 13 — Captura de cierre general

Con todas las capturas ya tomadas y la matriz de trazabilidad completa:

1. Abre la carpeta `img` y verifica que existan los 19 archivos anteriores.
2. Toma una captura final que muestre el resumen de resultados o la pantalla final de análisis.

> **📸 CAPTURA 20:** Toma una captura que muestre el cierre del análisis — puede ser la carpeta `img`  
> con todos los archivos, o una vista final de FTK Imager con la evidencia procesada.  
> Guárdala como `20_conclusion_visual_hallazgos.png`

---

## Parte 8: Redactar el informe

### Paso 14 — Completar documento_entrega.md con tus hallazgos reales

Abre `documento_entrega.md` y reemplaza el texto base con tus datos reales:

- En **sección 6**: describe exactamente lo que observaste, no lo que debería verse.
- En **sección 7** (tabla de hallazgos): completa con los valores reales que encontraste.
- En **sección 8**: redacta tu interpretación propia.
- En **sección 9**: escribe recomendaciones concretas basadas en TUS hallazgos.
- En **sección 10**: conclusiones en primera persona sobre lo que aprendiste.

> **Regla importante:** No copies el texto base tal como está. La rúbrica penaliza falta de análisis propio.  
> Si encontraste solo programas legítimos en `Run`, dilo y explica por qué aun así es importante verificarlos.

---

## Parte 9: Generar el documento Word

### Paso 15 — Ejecutar el script generador

Abre una terminal (PowerShell o CMD) en la carpeta:  
`c:\github\uni\informatica forence\eje_3\desarrollo de la actividad\`

Ejecuta:

```powershell
python generar_dox.py
```

Deberías ver:

```
DOCX generado correctamente: ...Analisis_Forense_Registro_Windows_MelquiRomero.docx
```

Si aparece un error de módulo, instala la dependencia primero:

```powershell
pip install python-docx
```

Verifica que el archivo Word generado:
- Contiene todas las secciones.
- Las imágenes aparecen (o los marcadores de imagen faltante si aún no tienes capturas reales).
- No tiene errores de formato visibles.

---

## Orden recomendado de capturas

| # | Archivo | Cuándo tomarla |
|---|---|---|
| 01 | `01_entorno_preparado.png` | Antes de abrir FTK |
| 02 | `02_ftk_instalado_version.png` | Al abrir Help > About |
| 03 | `03_ftk_interfaz_principal.png` | Con FTK abierto y vacío |
| 04 | `04_rutas_objetivo_registro.png` | Antes de cargar evidencia |
| 05 | `05_add_evidence_item.png` | Al abrir el diálogo Add Evidence |
| 06 | `06_unidad_sistema_cargada.png` | Con la unidad en el árbol |
| 07 | `07_hive_software_ubicado.png` | En System32\config con SOFTWARE visible |
| 08 | `08_hive_software_detalle.png` | Con SOFTWARE seleccionado y panel de detalle visible |
| 09 | `09_run_key_vista_general.png` | Navegando hasta la clave Run |
| 10 | `10_run_key_valores.png` | Con el listado completo de valores Run |
| 11 | `11_run_key_posible_sospechoso.png` | Entrada individual más atípica |
| 12 | `12_ntuser_dat_ubicado.png` | NTUSER.DAT en el perfil de usuario |
| 13 | `13_recentdocs_vista_general.png` | Navegando hasta RecentDocs |
| 14 | `14_recentdocs_listado.png` | Listado de subclaves/valores de RecentDocs |
| 15 | `15_recentdocs_elemento_relevante.png` | Elemento individual de interés |
| 16 | `16_exportacion_run_key.png` | Al exportar Run key como .reg |
| 17 | `17_exportacion_recentdocs.png` | Al exportar RecentDocs como .reg |
| 18 | `18_matriz_trazabilidad_hallazgos.png` | Con la tabla de hallazgos completa |
| 19 | `19_hallazgo_persistencia_resumen.png` | Resumen o anotación del hallazgo principal |
| 20 | `20_conclusion_visual_hallazgos.png` | Carpeta img con todos los archivos o vista final |

---

## Checklist final antes de entregar

- [ ] 20 capturas en `../img/` con nombres exactos de esta guía.
- [ ] `documento_entrega.md` completado con hallazgos reales (no texto base).
- [ ] Cada sección del informe tiene al menos una captura asociada por nombre.
- [ ] `python generar_dox.py` ejecutó sin errores.
- [ ] `Analisis_Forense_Registro_Windows_MelquiRomero.docx` existe y se ve bien.
- [ ] El DOCX fue copiado a `entrega/`.
- [ ] Se revisó ortografía y coherencia técnica del texto.

