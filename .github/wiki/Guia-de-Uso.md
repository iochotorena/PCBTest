# Guía de uso – pcbTest

*GPL-3.0-or-later / CC-BY-SA-4.0*

---

## Flujo de trabajo recomendado

```
1. Instalar y configurar → ver Instalacion
2. Probar la cámara
3. Verificar los ficheros de referencia
4. Ajustar parámetros de inspección
5. Realizar inspecciones
6. Interpretar y actuar sobre los resultados
```

---

## Lanzar la GUI

```bash
cd ~/pcbTest
./pcb_gui_inspeccion.sh
```

---

## Usar el pipeline por terminal (sin GUI)

```bash
cd ~/pcbTest
./pcb_realtime_pipeline.sh \
  --camera-source 0 \
  --output-dir results/prueba_terminal \
  --reference-dir referenceBoard \
  --config config_homografia.json \
  --orientation-template keypoints/serigrafia.png \
  --component-model weights/best.pt \
  --limit 1 \
  --interval 0 \
  --homography-method hough \
  --conf 0.49 \
  --max-center-distance 0.035 \
  --max-center-distance-relaxed 0.060
```

---

## Probar solo la cámara por terminal

```bash
cd ~/pcbTest
./pcb_camera_test.sh \
  --camera-source 0 \
  --camera-width 0 \
  --camera-height 0 \
  --output-path results/gui_pcb_inspection/camera_test/latest_camera_test.jpg
```

---

## Procedimiento de inspección paso a paso

1. Abra la GUI: `./pcb_gui_inspeccion.sh`
2. **Pestaña Rutas** → verifique todos los ficheros → guarde.
3. **Pestaña Cámara** → pulse **TEST cámara** → compruebe la imagen.
4. **Pestaña Inspección** → coloque la placa bajo la cámara (completa, bien iluminada, sin tocar bordes).
5. Pulse **Analizar placa**.
6. Espere: **PLACA OK** o **PLACA MAL**.

---

## Resultados generados

```
results/gui_pcb_inspection/
├── raw/latest_raw.jpg              ← imagen original de la cámara
├── corrected/latest_corrected.jpg  ← imagen tras homografía
├── overlay/latest_result.jpg       ← todas las detecciones
├── overlay_failures/latest_failures.jpg  ← solo los fallos
├── components/latest_components.csv
├── comparison/latest_comparison.csv
├── camera_test/latest_camera_test.jpg
├── debug/                          ← imágenes de depuración
└── summary_realtime.csv
```

---

## Interpretar los resultados

| Estado | Significado |
|--------|-------------|
| **OK** | Componente encontrado en posición aceptable. |
| **MISSING** | Componente esperado no detectado. |
| **MISPLACED** | Clase correcta detectada, posición insuficiente. |
| **EXTRA** | Detección sin equivalente en la referencia. |

**La placa es OK si:** `MISSING = 0` **y** `MISPLACED = 0`.

Las detecciones EXTRA son avisos por defecto (activar **EXTRA como fallo** en Configuración si se necesita).

---

## Ajustar parámetros

| Problema observado | Acción |
|--------------------|--------|
| Muchos EXTRA / falsos positivos | Subir confianza YOLO: `0.49 → 0.55 → 0.60` |
| Muchos MISSING | Bajar confianza YOLO: `0.60 → 0.55 → 0.49`; revisar iluminación/enfoque |
| Muchos MISPLACED | Subir distancia centro: `0.035 → 0.045 → 0.060` |
| Homografía incorrecta | Ver placa completa; sin reflejos; placa sin tocar bordes; revisar `debug/homography/` |
| Orientación incorrecta | Verificar `keypoints/serigrafia.png`; revisar `debug/orientation/` |

> **Regla de oro:** cambie **un solo parámetro a la vez**.

---

## Limpiar resultados

```bash
rm -rf results/gui_pcb_inspection
mkdir -p results
touch results/.gitkeep
```

---

## Reinicialización limpia

```bash
rm -f gui_config.json
rm -rf results/gui_pcb_inspection
./pcb_gui_inspeccion.sh
```

El fichero `gui_config.json` **no** debe copiarse entre máquinas (almacena rutas absolutas de la máquina local).
