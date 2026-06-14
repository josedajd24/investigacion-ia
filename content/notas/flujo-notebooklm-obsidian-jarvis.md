---
title: Flujo NotebookLM + Obsidian + Jarvis
tags:
  - tesis
  - ia-generativa
  - notebooklm
  - obsidian
  - jarvis-os
  - metodología
---

# Flujo NotebookLM + Obsidian + Jarvis

> Objetivo: usar NotebookLM como espacio de conversación con fuentes y usar Jarvis/Obsidian como sistema de organización, escritura académica y trazabilidad del trabajo de grado.

## 1. Principio de arquitectura

NotebookLM no debe ser el archivo maestro de la tesis. Debe funcionar como un **laboratorio de lectura**.

Obsidian/Quartz debe ser el **archivo maestro**, porque allí quedan:

- decisiones de investigación;
- fichas de lectura;
- matriz de estado del arte;
- borradores de capítulos;
- metodología;
- avances publicables;
- memoria del proceso.

Jarvis debe operar como **coordinador**:

1. prepara fuentes;
2. organiza materiales;
3. diseña preguntas para NotebookLM;
4. procesa respuestas;
5. convierte hallazgos en notas, matrices o borradores;
6. evita que la tesis se vuelva una colección caótica de resúmenes.

## 2. Dónde se arma

La base debe vivir en este repositorio Quartz/Obsidian:

`/home/daniel/Documents/TdG/investigacion-ia/content/`

Estructura recomendada:

```text
content/
  notas/
    flujo-notebooklm-obsidian-jarvis.md
    prompts-notebooklm-tesis.md
    bitacora-notebooklm.md
  referencias/
    investigaciones-clave/
    matriz_estado_del_arte_ia_generativa_comunicaciones.md
  fuentes-notebooklm/
    paquete-01-estado-del-arte.md
    paquete-02-marco-teorico.md
    paquete-03-metodologia.md
```

Nota: la carpeta `fuentes-notebooklm/` puede crearse después si se decide convertir documentos y PDFs en paquetes Markdown listos para subir o copiar a NotebookLM.

## 3. Rol de cada herramienta

### NotebookLM

Uso recomendado:

- conversar con PDFs, artículos, documentos y notas;
- pedir síntesis comparativas;
- detectar conceptos recurrentes;
- encontrar tensiones entre autores;
- generar preguntas de lectura;
- preparar guías de estudio o audio-resúmenes.

Límite:

- no debe decidir la estructura final de la tesis;
- no debe reemplazar la matriz de estado del arte;
- no debe usarse como fuente final sin volver a verificar los documentos originales.

### Obsidian / Quartz

Uso recomendado:

- guardar fichas de lectura;
- consolidar argumentos;
- escribir capítulos;
- mantener trazabilidad;
- publicar avances si José lo autoriza.

Límite:

- no debe llenarse con transcripciones completas sin criterio;
- cada nota debe tener propósito claro.

### Jarvis

Uso recomendado:

- seleccionar fuentes;
- preparar paquetes temáticos;
- redactar prompts;
- convertir respuestas de NotebookLM en material académico;
- limpiar duplicados;
- proponer estructura;
- verificar consistencia conceptual.

Límite:

- no inventar fuentes;
- no publicar cambios sin autorización;
- no modificar arquitectura sin aprobación.

## 4. Flujo operativo por ciclos

### Ciclo A — Preparar fuentes

Entrada:

- PDFs;
- artículos académicos;
- documentos de Google;
- notas existentes de Obsidian;
- correos o documentos del trabajo de grado.

Acción de Jarvis:

1. clasifica las fuentes por tema;
2. elimina ruido;
3. crea paquetes de lectura;
4. identifica qué fuente sirve para cada capítulo.

Salida:

- paquete de fuentes para NotebookLM;
- lista de fuentes prioritarias;
- preguntas iniciales de lectura.

### Ciclo B — Conversar con NotebookLM

José sube o añade las fuentes a NotebookLM y usa prompts diseñados por Jarvis.

Preguntas tipo:

- ¿Qué tensiones aparecen entre IA generativa, escritura académica y autoría?
- ¿Qué conceptos se repiten entre las fuentes?
- ¿Qué vacíos de investigación se pueden identificar?
- ¿Qué argumentos sirven para justificar una investigación en la Facultad de Comunicaciones?
- ¿Qué riesgos éticos aparecen sobre el uso de IA en procesos de escritura universitaria?
- ¿Qué diferencias hay entre usar IA como herramienta instrumental y usarla como mediación académica?

Salida de NotebookLM:

- síntesis;
- citas sugeridas;
- respuestas comparativas;
- ideas para marco teórico;
- preguntas nuevas.

### Ciclo C — Procesar salidas

José copia las respuestas importantes de NotebookLM y se las entrega a Jarvis.

Jarvis convierte esas salidas en:

- ficha de lectura;
- matriz de estado del arte;
- apartado del marco teórico;
- justificación;
- notas metodológicas;
- preguntas para entrevista o taller;
- resumen para exposición.

### Ciclo D — Consolidar en Obsidian

Todo hallazgo útil debe terminar en una nota clara, no perdido en NotebookLM.

Formato mínimo de cada nota:

```markdown
# Título de la nota

## Idea central

## Fuente o fuentes asociadas

## Aporte para la tesis

## Cita o evidencia verificable

## Relación con capítulos

## Pendientes
```

## 5. Paquetes iniciales recomendados para NotebookLM

### Paquete 01 — Estado del arte

Objetivo:

- entender qué se ha investigado sobre IA generativa en educación superior, escritura académica e integridad académica.

Fuentes candidatas:

- artículos en `content/referencias/investigaciones-clave/`;
- matriz de estado del arte;
- notas del estado del arte.

Preguntas clave:

- ¿Qué enfoques dominan la literatura?
- ¿Qué falta investigar desde comunicación?
- ¿Cómo aparece la relación profesor-estudiante?
- ¿La IA se entiende como herramienta, amenaza, mediación o infraestructura?

### Paquete 02 — Marco teórico

Objetivo:

- organizar conceptos centrales.

Conceptos posibles:

- IA generativa;
- escritura académica;
- comunicación académica;
- mediación;
- alfabetización en IA;
- autoría;
- integridad académica;
- prácticas de investigación y escritura.

Preguntas clave:

- ¿Qué conceptos son imprescindibles?
- ¿Qué autores ayudan a definir cada concepto?
- ¿Qué tensiones conceptuales existen?
- ¿Qué marco permite conectar IA, comunicación y escritura universitaria?

### Paquete 03 — Metodología

Objetivo:

- traducir la investigación en un diseño realizable durante el semestre.

Preguntas clave:

- ¿Qué tipo de estudio conviene: exploratorio, cualitativo, estudio de caso, investigación aplicada?
- ¿Qué técnicas son viables: entrevistas, talleres, análisis de flujos, diarios de uso?
- ¿Qué datos serían suficientes sin volver el proyecto inmanejable?
- ¿Cómo justificar ética y académicamente el uso de IA en el proceso?

## 6. Prompts base para NotebookLM

### Prompt 1 — Mapa de tensiones

```text
A partir de las fuentes cargadas, identifica las tensiones principales entre IA generativa, escritura académica, autoría, integridad académica y mediación profesor-estudiante. Organiza la respuesta en: tensión, autores o fuentes relacionadas, evidencia textual y posible aporte para una tesis en comunicación.
```

### Prompt 2 — Vacío de investigación

```text
Revisa las fuentes y señala qué aspectos están poco desarrollados respecto al uso de IA generativa en procesos de investigación y escritura académica en estudiantes universitarios de comunicación. No inventes fuentes. Diferencia claramente entre hallazgos respaldados por documentos y posibles inferencias.
```

### Prompt 3 — Marco teórico

```text
Propón una estructura de marco teórico para una tesis sobre IA generativa, comunicación académica, mediación profesor-estudiante y flujos de investigación/escritura. Para cada apartado indica qué fuentes del notebook lo respaldan y qué conceptos debería definir.
```

### Prompt 4 — Metodología viable

```text
Con base en las fuentes y en una tesis de pregrado realizable en un semestre, sugiere un diseño metodológico cualitativo para estudiar cómo estudiantes y profesores de comunicación usan o entienden la IA generativa en procesos de investigación y escritura académica. Incluye técnicas, participantes, datos esperados, límites y riesgos éticos.
```

### Prompt 5 — Matriz de lectura

```text
Convierte las fuentes cargadas en una matriz con estas columnas: fuente, objetivo del texto, metodología, concepto central, hallazgo relevante, aporte para mi tesis, limitaciones y cita textual útil. No agregues fuentes que no estén en el notebook.
```

## 7. ¿Hace falta MCP de n8n?

No para el MVP.

Para esta fase inicial, no hace falta conectar n8n ni MCP porque el cuello de botella no es la automatización, sino la calidad de selección, lectura y síntesis de fuentes.

La versión MVP debe ser manual-asistida:

1. Jarvis prepara fuentes y prompts.
2. José sube fuentes a NotebookLM.
3. NotebookLM genera síntesis.
4. José entrega salidas a Jarvis.
5. Jarvis consolida en Obsidian/Quartz.

Esto evita una arquitectura frágil.

## 8. Cuándo sí tendría sentido n8n

n8n tendría sentido en una segunda fase, cuando el flujo ya esté probado.

Automatizaciones posibles:

- detectar PDFs nuevos en Drive;
- guardar metadatos en una hoja de cálculo;
- crear una ficha Markdown en Obsidian;
- avisar por Telegram cuando haya fuentes nuevas;
- separar fuentes por tema;
- generar una tarea de revisión;
- alimentar una base de datos de estado del arte.

Pero n8n no debería intentar controlar NotebookLM directamente, porque NotebookLM no ofrece una API pública estable. Automatizarlo por navegador sería frágil.

## 9. Criterio de decisión

Recomendación Jarvis:

- **Ahora:** Obsidian/Quartz + Google Drive + NotebookLM manual + Jarvis.
- **Después:** n8n para ingestión y seguimiento de fuentes.
- **No todavía:** automatización directa de NotebookLM.

La prioridad es construir un flujo académico confiable, no una automatización vistosa pero débil.

## 10. Próximo paso sugerido

Crear dos notas complementarias:

1. `prompts-notebooklm-tesis.md`
   - banco limpio de prompts listos para copiar.

2. `bitacora-notebooklm.md`
   - registro de sesiones: fecha, fuentes usadas, preguntas hechas, hallazgos, decisiones para la tesis.

Después, seleccionar el primer paquete de fuentes: **estado del arte**.
