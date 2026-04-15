# Caracterización de Ataques Informáticos y Aportes de la Informática Forense
## Eje 4 - Actividad Complementaria Sincrónica

**Estudiante:** Melqui Romero  
**Asignatura:** Informática Forense  
**Eje:** 4 - Delitos Cibernéticos y Marcos Legales Internacionales  
**Fecha:** 6 de abril de 2026  
**Puntos:** 5

---

## CASO 1: PHISHING - CAMPAÑAS AMAZON PRIME DAY

### 1. Caracterización del Ataque

| Aspecto | Descripción |
|---------|-------------|
| **Nombre del Ataque** | Cuidado en el próximo Amazon Prime Day: aumentan las webs falsas |
| **País/Región** | Estados Unidos (Nivel general) |
| **Tipo de Ataque** | Phishing |
| **Fecha** | 8 de julio de 2024 |
| **Concepto** | Envío masivo de correos simulando problemas con compras para redireccionar a sitios fraudulentos y capturar datos personales |

### 2. Análisis Técnico y Operacional

**Metodología de ataque:**
- Creación de sitios web clonados similares a Amazon oficial
- Campaña de phishing mediante correo electrónico masivo
- Suplantación de identidad corporativa
- Captura de credenciales y datos de tarjeta de crédito

**Vulnerabilidad explotada:**
- Confianza del usuario en marcas reconocidas
- Falta de verificación de URL en correos
- Ausencia de educación en seguridad del usuario final

### 3. Marco Legal

**Ley Aplicable:** Ley 1273 de 2009 (Colombia) - Art. 269G  
**Tipo de Delito:** Suplantación de Sitios Web para adquirir y capturar datos personales

**Penas:**
- Prisión: 48 a 96 meses
- Multa: 100 a 1,000 salarios mínimos legales vigentes

### 4. Aporte de la Informática Forense

**Investigación Forense:**
- Rastreo de encabezados de correo electrónico (SMTP headers, SPF, DKIM)
- Análisis de metadatos en URLs y sitios fraudulentos
- Identificación de registros DNS falsificados
- Análisis de logs de servidor de correo
- Reconstrucción de cadena de envío

**Evidencia Recolectable:**
- Encabezados y contenido de correos electrónicos maliciosos
- URLs y metadatos de sitios web fraudulentos
- Registros de actividad en redes y dispositivos
- Archivos de registro de autenticación y accesos fallidos
- Direcciones IP de origen
- Cuentas bancarias o correos electrónicos de remitentes sospechosos

### 5. Prevención y Mitigación

- Verificación exhaustiva del remitente y dominio
- Inspección de errores ortográficos en mensajes
- Validación de URL (https:// y icono de candado)
- Implementación de DMARC, SPF y DKIM
- Educación continua en seguridad de usuarios
- Filtros de correo electrónico avanzados

---

## CASO 2: APT (ADVANCED PERSISTENT THREAT) - AVIANCA

### 1. Caracterización del Ataque

| Aspecto | Descripción |
|---------|-------------|
| **Nombre del Ataque** | Avianca Attack (APT Blind Eagle) |
| **País/Región** | Colombia |
| **Tipo de Ataque** | Spear Phishing / APT |
| **Fecha** | Febrero - Marzo 2025 |
| **Concepto** | Campaña APT dirigida usando emails con adjuntos maliciosos (archivos URL) explotando vulnerabilidades para robo de credenciales y despliegue de malware (AsyncRAT, Quasar RAT) |

### 2. Análisis Técnico y Operacional

**Metodología de ataque:**
- Spear phishing altamente dirigido a empleados específicos
- Explotación de vulnerabilidades recientes
- Despliegue de RATs (Remote Access Trojans): AsyncRAT y Quasar RAT
- Movimiento lateral dentro de la infraestructura
- Acceso no autorizado y robo de datos
- Disrupción de servicios como LifeMiles

**Cadena de infección:**
1. Correo spear phishing dirigido
2. Descarga de archivo URL malicioso
3. Ejecución de payload RAT
4. Establecimiento de acceso remoto
5. Movimiento lateral en la red
6. Exfiltración de datos

### 3. Marco Legal

**Leyes Aplicables:** Ley 1273 de 2009 (Ley de Ciberdelitos de Colombia)
- Art. 269A: Acceso no autorizado
- Art. 269B: Obstrucción ilegal
- Art. 269C: Interceptación de datos
- Art. 269F: Suplantación de sitios web

**Penas:**
- Prisión: 48 a 120 meses según el delito
- Multas: 100 a 1,000 salarios mínimos legales vigentes

### 4. Aporte de la Informática Forense

**Investigación Forense:**
- Análisis de emails maliciosos y archivos URL
- Identificación de malware (AsyncRAT, Quasar RAT)
- Reconstrucción de movimiento lateral en la red
- Análisis de logs de autenticación y acceso
- Determinación del alcance de compromiso de datos
- Atribución a grupo APT Blind Eagle

**Evidencia Recolectable:**
- Encabezados y contenido de correos maliciosos
- Archivos URL maliciosos (análisis estático y dinámico)
- Logs de red y tráfico (tráfico WebDAV sospechoso)
- Artefactos de ejecución de malware
- Credenciales comprometidas
- Logs de acceso a sistemas internos
- Registros de actividad LifeMiles

### 5. Prevención y Mitigación

- Capacitación en conciencia de phishing
- Verificación de email
- Autenticación multifactor (MFA)
- Actualizaciones de sistema inmediatas
- Monitoreo de red y detección de anomalías
- Uso de antivirus/EDR (Endpoint Detection and Response)
- Políticas de seguridad robustas

---

## CASO 3: DATA BREACH - HACIENDA (ESPAÑA)

### 1. Caracterización del Ataque

| Aspecto | Descripción |
|---------|-------------|
| **Nombre del Ataque** | Hacienda Attack - Ministerio de Hacienda España |
| **País/Región** | España / Madrid |
| **Tipo de Ataque** | Data Breach / Unauthorized Access |
| **Fecha** | 2 de febrero de 2026 |
| **Concepto** | Acceso no autorizado a bases de datos de Hacienda comprometiendo datos personales, bancarios y fiscales de 47.3 millones de ciudadanos |

### 2. Análisis Técnico y Operacional

**Vulnerabilidades explotadas:**
- IDOR (Insecure Direct Object Reference) en sistemas legacy
- Falta de control de acceso adecuado
- Credenciales reutilizadas de brechas anteriores
- Ausencia de MFA (Multiple Factor Authentication)
- Falta de monitoreo de actividad sospechosa

**Datos comprometidos:**
- Números de DNI (Documento Nacional de Identidad)
- Nombres completos
- Direcciones
- Números telefónicos
- Direcciones de correo electrónico
- IBANs (Números de Cuenta Bancaria)
- Información fiscal

**Impacto:**
- Exposición de 47.3 millones de ciudadanos
- Riesgo de fraude bancario
- Riesgo de robo de identidad
- Ataques de phishing dirigidos

### 3. Marco Legal

**Leyes Aplicables:**
- Ley 1273 de 2009 (Delitos Informáticos - Colombia)
  - Art. 269A: Acceso no autorizado (48-96 meses)
  - Art. 269C: Interceptación de datos (36-72 meses)
  - Art. 269G: Suplantación de sitios web (48-96 meses)
  - Art. 269J: Transferencia no autorizada de activos (48-120 meses)
- GDPR (Reglamento General de Protección de Datos)
- Notificación obligatoria en 72 horas

**Penas:**
- Prisión: 48 a 120 meses
- Multas: 100 a 1,500 salarios mínimos vigentes

### 4. Aporte de la Informática Forense

**Investigación Forense:**
- Análisis de logs de acceso a bases de datos
- Identificación de intentos de autenticación fallidos
- Reconstrucción de cadena de acceso
- Análisis de actividad IDOR
- Determinación de volumen de datos exfiltrados
- Identificación de patrones de consulta masiva
- Análisis de tráfico de red (transferencias de datos masivas)

**Evidencia Recolectable:**
- Logs de sistema: accesos a base de datos, intentos de autenticación fallidos, actividad anormal del servidor
- Tráfico de red: para identificar transferencias de datos masivas o conexiones externas sospechosas
- Copias de bases de datos comprometidas: para comparar con datos filtrados
- Posts en foros y redes sociales: análisis OSINT para rastrear al atacante
- Dispositivos y cuentas con acceso privilegiado: para determinar si hubo abuso de credenciales internas
- Chain of Custody: documentación rigurosa de todos los pasos

### 5. Prevención y Mitigación (5 Capas)

**Capa 1 - Autenticación:**
- MFA (Autenticación Multifactor)
- Verificación de credenciales en HaveIBeenPwned

**Capa 2 - Control de Acceso:**
- Implementación correcta de control de acceso (IDOR fix)
- Principio de menor privilegio

**Capa 3 - Monitoreo:**
- Detección automática de patrones sospechosos
- Alertas de consultas masivas a registros

**Capa 4 - Encriptación:**
- Encriptación de datos en reposo
- Encriptación en tránsito (TLS/SSL)

**Capa 5 - Respuesta:**
- Protocolo de incidente predefinido
- Notificación a usuarios en 72 horas (GDPR)

---

## CASO 4: RANSOMWARE - WANNACRY

### 1. Caracterización del Ataque

| Aspecto | Descripción |
|---------|-------------|
| **Nombre del Ataque** | WannaCry Ransomware |
| **País/Región** | Reino Unido (impacto global) |
| **Tipo de Ataque** | Ransomware / Worm |
| **Fecha** | 12 de mayo de 2017 |
| **Concepto** | Gusano ransomware que explotaba vulnerabilidad EternalBlue para cifrar datos y exigir rescate |

### 2. Análisis Técnico y Operacional

**Vulnerabilidad explorada:**
- EternalBlue (exploit NSA robado por Shadow Brokers)
- Afectaba solo versiones viejas sin parches de Windows

**Propagación:**
- Más de 200,000 computadoras en 150+ países infectadas
- Víctimas de alto perfil: FedEx, Honda, Nissan, NHS (Servicio Nacional de Salud UK)

**Kill Switch:**
- Marcus Hutchins descubrió que WannaCry verificaba dominio: iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea.com
- Hutchins registró el dominio por $10.69
- La verificación del dominio detuvo la propagación del malware

**Impacto:**
- Cifrado de datos críticos
- Paralización de servicios hospitalarios
- Pérdidas económicas masivas

### 3. Marco Legal

**Leyes Aplicables:**
- Budapest Convention on Cybercrime (2001)
- Criminal Code - Art. 269: Software malicioso
- Ley 1273 de 2009 (Colombia) para delitos similares

### 4. Aporte de la Informática Forense

**Investigación Forense:**
- Análisis de muestras de malware (reverse engineering)
- Identificación de cadena de propagación
- Análisis de comportamiento del ransomware
- Identificación de mecanismo de kill switch
- Recuperación de datos donde sea posible
- Análisis de pagos en Bitcoin (blockchain forense)

**Evidencia Recolectable:**
- Muestras del malware WannaCry
- Logs de sistema infectados
- Tráfico de red de propagación
- Pagos en Bitcoin a direcciones del atacante
- Comunicaciones de comando y control (C2)

### 5. Prevención y Mitigación

- **Actualización inmediata** de sistemas operativos
- Instalación de parches de seguridad
- Backups regulares y desconectados
- Segmentación de red
- EDR (Endpoint Detection and Response)
- Educación de usuarios sobre amenazas

---

## CASO 5: RANSOMWARE - IFX NETWORKS (COLOMBIA)

### 1. Caracterización del Ataque

| Aspecto | Descripción |
|---------|-------------|
| **Nombre del Ataque** | IFX Networks Ransomware Attack |
| **País/Región** | Colombia |
| **Tipo de Ataque** | Ransomware / Secuestro Digital de Información |
| **Fecha** | 12-16 de septiembre de 2023 |
| **Concepto** | Ataque ransomware que paralizó infraestructura cloud afectando >4,200 empresas en América Latina |

### 2. Análisis Técnico y Operacional

**Alcance del impacto:**
- 4,200+ empresas en América Latina afectadas
- 1,800 empresas en Colombia
- Sectores críticos: Salud, Justicia, Educación

**Tipo de servicio afectado:**
- Centro de datos en la nube
- Servicios críticos de múltiples instituciones
- Infraestructura de e-government

**Riesgo:**
- Exposición de datos sensibles
- Paralización de servicios esenciales
- Impacto a ciudadanos dependientes de servicios públicos

### 3. Marco Legal

**Leyes Aplicables:**
- Ley 1273 de 2009 (Delitos Informáticos - Colombia)
  - Art. 269G: Obstrucción no autorizada de sistemas informáticos

**Penas:**
- Prisión: 4 a 8 años
- Multas: 50 a 1,000 salarios mínimos mensuales

### 4. Aporte de la Informática Forense

**Investigación Forense:**
- Identificación de variante de ransomware
- Reconstrucción de línea temporal del ataque
- Recuperación de datos cifrados donde sea posible
- Atribución a actores de amenaza específicos
- Análisis de comunicaciones C2

**Evidencia Recolectable:**
- Archivos y logs de servidor
- Capturas de tráfico de red
- Entradas del registro de Windows
- Archivos cifrados y notas de rescate
- Muestras de malware
- Comunicaciones con servidores C2

### 5. Prevención y Mitigación

- Backups regulares y redundantes
- Segmentación de red
- MFA en todos los accesos
- Capacitación en conciencia de seguridad
- Arquiteyctura Zero Trust
- Monitoreo continuo

---

## COMPARATIVA DE ATAQUES Y MÉTODOS FORENSES

| Tipo de Ataque | Vector Principal | Evidencia Clave | Tiempo Detección | Integridad Datos |
|---|---|---|---|---|
| **Phishing** | Correo electrónico | Headers, URLs, metadatos | Minutos a horas | Compromiso de credenciales |
| **APT** | Email dirigido + exploits | Malware, logs de red, UAC | Horas a días | Acceso completo a sistemas |
| **Data Breach** | Vulnerabilidades web (IDOR) | Logs de acceso, tráfico, credenciales | Días a semanas | Exfiltración masiva |
| **Ransomware** | Vulns + movimiento lateral | Archivos cifrados, logs, pagos BTC | Minutos a horas | Cifrado irreversible |

---

## CONCLUSIONES Y RECOMENDACIONES

### Principios Forenses Aplicables

1. **Cadena de Custodia:** Documentación rigurosa desde recolección hasta presentación
2. **Integridad de Evidencia:** Uso de hash criptográfico (MD5, SHA-256)
3. **Principio de Locard:** Todo contacto deja rastro - logs, metadatos, artifacts
4. **Trazabilidad:** Cada paso de investigación debe ser verificable
5. **Relevancia Legal:** Evidencia debe ser admisible en procedimientos judiciales

### Recomendaciones para Marco Legal (Ey 4)

- Aplicación consistente de **Ley 1273 de 2009** en Colombia
- Alineación con **Convenio de Budapest** para cooperación internacional
- Implementación de **Directiva NIS** (sectores críticos)
- Cumplimiento de **GDPR** para datos de ciudadanos europeos
- **CFAA** (18 U.S.C. § 1030) para casos en EE.UU.

### Recomendaciones para Informática Forense

- Certificación de peritos en herramientas: EnCase, FTK, Volatility
- Protocolo estandarizado de recolección (NIST, SANS)
- Laboratorio forense acreditado
- Cadena de custodia documentada desde primer momento
- Análisis independiente y verificable

---

**Analyst Name:** Melqui Romero  
**Forensic Specialization:** Digital Forensics & Cybercrime Investigation  
**Date:** April 6, 2026  
**Status:** Completed
