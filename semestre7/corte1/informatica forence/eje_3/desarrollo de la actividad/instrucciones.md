# INSTRUCCIONES - EJE 3 (VERSION DETALLADA)

## 1) Proposito de este paquete

Estas instrucciones estan pensadas para que puedas ejecutar la actividad de Eje 3 de forma individual, con el mismo nivel de detalle y trazabilidad que se uso en Eje 1.

El flujo completo de trabajo es:

1. Seguir la guia operativa.
2. Tomar capturas en orden estricto.
3. Documentar hallazgos en Markdown.
4. Generar el DOCX final con Python.

Archivos clave:

- `guia.md`: pasos tecnicos de ejecucion en FTK Imager.
- `documento_entrega.md`: informe academico.
- `generar_dox.py`: conversion de Markdown a Word.
- `../img/`: carpeta de evidencias visuales.

---

## 2) Alcance tecnico de la actividad

Debes analizar, como minimo, estas dos rutas del Registro:

- `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`

Objetivo forense:

- Detectar posibles mecanismos de persistencia (Run).
- Reconstruir actividad reciente de usuario (RecentDocs).

---

## 3) Regla principal de evidencias (capturas)

Toda afirmacion tecnica en el informe debe tener respaldo visual.

Si escribes "se identifico X", debe existir una captura que lo demuestre.

### Reglas de captura obligatorias

1. Formato: `.png`.
2. Nomenclatura: `NN_descripcion_corta.png`.
3. Numeracion: continua, sin saltos (01, 02, 03...).
4. Calidad: texto legible en paneles de FTK Imager.
5. Contexto visible: no cortes la pantalla de forma que se pierda la ruta o el panel donde se ve el dato clave.

---

## 4) Checklist maestro de capturas (obligatorio)

> Esta seccion es la referencia principal para que no te falte ninguna evidencia.

### Capturas de preparacion

1. `01_entorno_preparado.png`
   - Debe mostrar: entorno listo (escritorio/VM de trabajo).
   - Validacion: se identifica claramente que es el equipo de analisis.

2. `02_ftk_instalado_version.png`
   - Debe mostrar: version de FTK Imager instalada.
   - Validacion: numero de version visible.

3. `03_ftk_interfaz_principal.png`
   - Debe mostrar: ventana principal de FTK Imager.
   - Validacion: panel de arbol y panel de contenido visibles.

### Capturas de carga de evidencia

4. `04_rutas_objetivo_registro.png`
   - Debe mostrar: rutas objetivo definidas para analisis (Run y RecentDocs).
   - Validacion: rutas completas legibles.

5. `05_add_evidence_item.png`
   - Debe mostrar: opcion `Add Evidence Item`.
   - Validacion: dialogo/menu visible.

6. `06_unidad_sistema_cargada.png`
   - Debe mostrar: unidad del sistema agregada en FTK Imager.
   - Validacion: evidencia montada en el arbol.

7. `07_hive_software_ubicado.png`
   - Debe mostrar: ubicacion de `Windows\System32\config\SOFTWARE`.
   - Validacion: ruta visible.

8. `08_hive_software_detalle.png`
   - Debe mostrar: detalle del hive SOFTWARE (vista de contenido).
   - Validacion: nombre del artefacto y metadatos visibles.

### Capturas de analisis de persistencia (Run)

9. `09_run_key_vista_general.png`
   - Debe mostrar: navegacion a `...CurrentVersion\Run`.
   - Validacion: ruta completa visible en la interfaz.

10. `10_run_key_valores.png`
	- Debe mostrar: listado de valores de la clave Run.
	- Validacion: nombres y datos de al menos 2 valores visibles.

11. `11_run_key_posible_sospechoso.png`
	- Debe mostrar: valor que consideras potencialmente atipico.
	- Validacion: se ve el nombre del valor, dato/ruta y por que llama la atencion.

### Capturas de analisis de actividad (RecentDocs)

12. `12_ntuser_dat_ubicado.png`
	- Debe mostrar: ubicacion de `NTUSER.DAT` del perfil analizado.
	- Validacion: ruta del perfil o evidencia equivalente visible.

13. `13_recentdocs_vista_general.png`
	- Debe mostrar: navegacion a `...Explorer\RecentDocs`.
	- Validacion: ruta completa visible.

14. `14_recentdocs_listado.png`
	- Debe mostrar: listado de entradas en RecentDocs.
	- Validacion: nombres/extensiones visibles.

15. `15_recentdocs_elemento_relevante.png`
	- Debe mostrar: entrada que consideras relevante para analisis.
	- Validacion: evidencia puntual + contexto de lista.

### Capturas de preservacion y trazabilidad

16. `16_exportacion_run_key.png`
	- Debe mostrar: proceso o resultado de exportacion de evidencia de Run.
	- Validacion: nombre de archivo o destino visible.

17. `17_exportacion_recentdocs.png`
	- Debe mostrar: proceso o resultado de exportacion de RecentDocs.
	- Validacion: nombre de archivo o destino visible.

18. `18_matriz_trazabilidad_hallazgos.png`
	- Debe mostrar: matriz o tabla donde conectas evidencia con hallazgo.
	- Validacion: columna de evidencia y columna de interpretacion visibles.

### Capturas de cierre analitico

19. `19_hallazgo_persistencia_resumen.png`
	- Debe mostrar: resumen visual del hallazgo de persistencia.
	- Validacion: relacion directa con seccion 7 u 8 del informe.

20. `20_conclusion_visual_hallazgos.png`
	- Debe mostrar: cierre visual de resultados (resumen general).
	- Validacion: evidencia final coherente con conclusiones.

---

## 5) Flujo de trabajo exacto (paso a paso)

1. Leer `../Actividad evaluativa eje3.md` y verificar rubrica.
2. Ejecutar `guia.md` de principio a fin.
3. Guardar las 20 capturas de la lista anterior en `../img/`.
4. Abrir `documento_entrega.md` y reemplazar hallazgos genericos por tus hallazgos reales.
5. Verificar que cada hallazgo tenga al menos 1 captura asociada por nombre.
6. Generar documento Word con:

```bash
python generar_dox.py
```

7. Validar el DOCX generado y copiarlo en `entrega/`.

---

## 6) Criterios de calidad para obtener alta calificacion

### Construccion y contenido

- Explica no solo que encontraste, sino por que es relevante.
- Distingue entre hecho observado (evidencia) e interpretacion (analisis).

### Evidencia y documentacion

- No dejes hallazgos sin respaldo visual.
- Usa nombres de captura exactamente iguales entre `img/` y el informe.

### Analisis de resultados

- Integra hallazgos de `Run` y `RecentDocs` en una narrativa unica.
- Prioriza riesgos (alto, medio, bajo) con criterio tecnico.

### Recomendaciones

- Propone acciones concretas y aplicables.
- Incluye mitigacion inmediata y accion preventiva.

### Redaccion

- Usa lenguaje tecnico claro y formal.
- Revisa ortografia antes de generar el DOCX final.

---

## 7) Validacion final antes de entregar

Checklist rapido:

- [ ] Existen 20 capturas en `../img/` con nombres correctos.
- [ ] `documento_entrega.md` ya tiene hallazgos reales (no solo texto base).
- [ ] `python generar_dox.py` ejecuta sin error.
- [ ] Existe `Analisis_Forense_Registro_Windows_MelquiRomero.docx`.
- [ ] El DOCX esta copiado en `entrega/`.

