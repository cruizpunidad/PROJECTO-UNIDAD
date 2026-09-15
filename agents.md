# 🧠 UBPD Mediación Pedagógica - Registro Multiagente

## 📌 Resumen General del Proyecto
El proyecto es una herramienta digital de mediación pedagógica para la **Unidad de Búsqueda de Personas dadas por Desaparecidas (UBPD)** en Colombia. Su objetivo es informar y sensibilizar a la ciudadanía sobre el proceso de búsqueda (humanitario, extrajudicial y confidencial), ofrecer contención emocional y rutas seguras de aporte de información.
- **Frontend:** PWA, Offline-first (IndexedDB), construido en HTML/CSS/JS Vainilla. Diseño asimétrico, orgánico y empático (inspiración "Garden + Gather").
- **Backend:** Python + FastAPI con Strawberry (GraphQL) y REST. Diseñado para ser rápido, desplegable en contenedores ligeros (Railway) y con rate-limiting enfocado en UX.

## 🚦 Estado Actual
- [x] **Arquitectura Base:** Monorepo configurado (`/backend` y `/frontend`).
- [x] **Frontend MVP:** Interfaz estática implementada con 4 secciones visuales clave, tipografías personalizadas (Caveat/Montserrat) y sistema de colores en CSS.
- [x] **Backend MVP:** API inicial en FastAPI con esquema GraphQL levantada en entorno local.
- [ ] **Siguiente Paso Lógico:** Configuración del *Service Worker* para soporte Offline, y diseño del modelo de datos de historias en GraphQL.

---

## 📚 Índice de Memorias (Decisiones y Contexto Técnico)
- **Memoria 001 - Definición Arquitectónica (2026-08-25):** Se estableció usar HTML Vainilla puro para optimizar el rendimiento del frontend y FastAPI para el servidor. Sin CMS tradicionales.
- **Memoria 002 - Rediseño UI (2026-08-25):** El frontend pasó de una UI corporativa a un diseño orgánico/tipo collage, usando bloques de colores pastel, textos flotantes y doodles SVG.
- **Memoria 003 - Seguridad y Empatía (2026-08-25):** El Rate Limiting del backend no debe devolver un error 429 crudo. Debe enviar un JSON amigable para que el front muestre mensajes tipo "Respira, espera unos segundos".

---

## 🔒 Sistema de Claims (Flujo de Trabajo Multiagente)

Para evitar colisiones o pérdida de contexto en un entorno de desarrollo multiagente, cualquier agente (o humano) que modifique este proyecto debe seguir el protocolo de **Claims**.

### Reglas de Claims:
1. **Abrir Proyecto (Claim / Lock):** Antes de iniciar una tarea o invocar un subagente, el agente debe cambiar el estado de su Claim a `IN_PROGRESS` en la tabla de Tareas Activas y registrar la fecha de inicio.
2. **Cerrar Proyecto (Release / Unlock):** Al finalizar la tarea, el agente DEBE actualizar la tabla cambiando el estado a `COMPLETED` o `FAILED`, registrar el fin, y añadir una nueva línea en el **Índice de Memorias** con el resumen de sus cambios.

### 📋 Tareas Activas / Claims Log

| Claim ID | Agente Asignado | Componente a Intervenir | Estado | Inicio | Fin | Notas |
|---|---|---|---|---|---|---|
| `CLM-001` | Agente Principal | Scaffolding Inicial | `COMPLETED` | 2026-08-25 | 2026-08-25 | Setup Frontend/Backend estructurado |
| `CLM-002` | Agente Principal | Refactor Visual UI | `COMPLETED` | 2026-08-25 | 2026-08-25 | Integración estilo Garden+Gather al HTML |
| `CLM-003` | [Disponible] | Setup PWA Offline | `OPEN` | - | - | Configurar manifest.json y sw.js para el front |
| `CLM-004` | [Disponible] | Esquema GraphQL | `OPEN` | - | - | Diseñar queries/mutations para historias en FastAPI |
| `CLM-005` | [Disponible] | Lógica de IndexedDB | `OPEN` | - | - | Crear capa de persistencia en localForage/Vainilla JS |

### ✏️ Plantilla para Nuevo Claim
*(Los agentes deben copiar esta fila e insertarla en la tabla superior cuando reclamen una tarea)*
`| CLM-XXX | [ID/Rol del Agente] | [Nombre Tarea] | IN_PROGRESS | [Timestamp-Inicio] | - | [Descripción de lo que hará] |`
