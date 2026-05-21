# PCBTest — Wiki

Bienvenido a la wiki del repositorio **PCBTest**.

---

## Contenido de la wiki

| Página | Descripción |
|--------|-------------|
| [PCBTest – Aplicación de inspección](PCBTest) | Guía completa de la aplicación de inspección de placas PCB. |
| [Instalación en Jetson Orin Nano](Instalacion) | Instrucciones de instalación en Jetson Orin Nano con Docker. |
| [Guía de uso](Guia-de-Uso) | Cómo usar la GUI, la cámara y hacer inspecciones. |
| [2dDatasetCreator](2dDatasetCreator) | Generador sintético de datasets YOLO en 2D. |
| [SubsetMaker](SubsetMaker) | Herramienta GUI para gestión de datasets YOLO. |
| [Referencia técnica](Referencia-Tecnica) | Pipeline, estructura de archivos y parámetros. |
| [Licencia](Licencia) | Información sobre la licencia del proyecto. |

---

## Descripción del repositorio

**PCBTest** es un conjunto de herramientas para:

- **Inspección visual de placas PCB** mediante cámara, homografía y detección con YOLO.
- **Generación de datasets sintéticos** 2D para entrenar modelos YOLO (`tools/2dDatasetCreator`).
- **Gestión de datasets YOLO** (`tools/SUBSETMAKER`).

### Pipeline de inspección

```
Cámara → homografía → orientación → YOLO → comparación → OK / MAL
```

### Estructura del repositorio

```
PCBTest/
├── PCBTest/          # Aplicación principal de inspección de placas PCB
└── tools/
    ├── 2dDatasetCreator/   # Generador sintético de datasets 2D para YOLO
    └── SUBSETMAKER/        # GUI para gestión de datasets YOLO
```

---

*Código: GPL-3.0-or-later · Documentación: CC-BY-SA-4.0*
