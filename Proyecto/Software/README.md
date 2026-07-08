# Análisis EMG

**Activación y asimetría bilateral de los músculos estabilizadores del tronco
durante una simulación de transporte público: estudio piloto mediante
electromiografía de superficie.**

## Descripción

El archivo .ipynb para el procesamiento de las señales se encuentra en 
**processing_all_signal.ipynb**. En él se aplica el filtrado correspondiente
a cada señal adquirida y se grafica una comparación bilateral para el par
muscular del trapecio de cada participante, así como su FFT, periodograma
Welch y el RMS. <br>
Asimismo, se cuenta con una aplicación web interactiva desarrollada
en **Streamlit** para visualizar y analizar señales EMG de superficie (trapecio
derecho e izquierdo) adquiridas con **BITalino** a través de **OpenSignals**,
durante tres condiciones experimentales que simulan el uso de transporte público:
Basal, Una Asa y Doble Asa.

## Estructura del proyecto

```
Proyecto/
├── Raw/                         # Archivos .txt de OpenSignals
│   ├── basal_trapecio_priv1.txt
│   ├── basal_trapecio_priv2.txt
│   └── ...
├── utils/
│   ├── lectura.py               # Localización, lectura y conversión
│   ├── procesamiento.py         # Pipeline de filtros, recorte y normalización
│   ├── estadisticas.py          # Estadísticos descriptivos y asimetría bilateral
│   ├── espectral.py             # FFT, PSD y espectrograma
│   ├── graficas.py              # Figuras
│   └── filtros.py               # Filtros digitales
├── app.py                       # Aplicación principal Streamlit
├── config.py                    # Constantes, rutas y parámetros globales
├── processing_all_signal.ipynb  # ipynb independiente que procesa y plotea todas las señales
├── requirements.txt
├── proyecto_inicio.md           # Breve resumen del concepto del proyecto (Inicio del ciclo 2026-I)
└── README.md
```

## Formato de datos esperado

Cada archivo `.txt` exportado por OpenSignals debe seguir el patrón:

```
<condicion>_trapecio_<participante>.txt
```

Deben colocarse dentro de la carpeta `Datos/`. Las tres primeras líneas de
cada archivo (cabecera de OpenSignals) se ignoran automáticamente. Las
columnas usadas son A1 (Trapecio Derecho) y A2 (Trapecio Izquierdo),
muestreadas a 1000 Hz.

## Instalación

```bash
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en el navegador
(por defecto en `http://localhost:8501`).

## Funcionalidades principales

- **Selección de registro**: participante, condición y carga bajo demanda.
- **Conversión automática a milivoltios (mV)**: las cuentas ADC crudas de
  BITalino se convierten a mV mediante la fórmula estándar de PLUX/OpenSignals;
  todas las gráficas, estadísticas y exportaciones usan esta unidad.
- **Selección interactiva de intervalo temporal**: un control deslizante
  permite acotar el análisis a una ventana específica del registro; todas
  las estadísticas, gráficas y el análisis espectral se recalculan sobre
  ese intervalo.
- **Visualización interactiva** (Plotly): canal derecho, canal izquierdo y
  comparación sincronizada (zoom compartido entre ambos canales).
- **Procesamiento configurable**: rectificación de onda completa, filtro
  pasa banda Butterworth (frecuencias y orden ajustables) y filtro notch de
  60 Hz para interferencia de línea.
- **Normalización respecto a Basal**: expresa la señal como porcentaje del
  RMS de la condición Basal del mismo participante (cargada automáticamente).
- **Estadísticas descriptivas** por canal: media, mediana, desviación
  estándar, máximo, mínimo, RMS, MAV, varianza y energía, en mV.
- **Asimetría bilateral**: sección destacada con indicador tipo gauge,
  RMS de ambos canales e interpretación automática (Simetría adecuada /
  Asimetría leve / moderada / severa).
- **Análisis espectral**: FFT, Densidad Espectral de Potencia (método de
  Welch) y espectrograma (STFT), para ambos canales.
- **Exportación a CSV** del resumen de resultados del intervalo analizado.

## Notas técnicas

- Toda la configuración de la app vive en `config.py` como constantes, y el
  estado de la sesión de usuario se maneja mediante `st.session_state` de
  Streamlit.
- Los filtros se implementan con `scipy.signal` utilizando secciones de
  segundo orden (`sosfiltfilt`) para el pasa banda, garantizando estabilidad
  numérica y fase cero.
- El análisis espectral (`utils/espectral.py`) usa `numpy.fft`, `scipy.signal.welch`
  y `scipy.signal.spectrogram`.
- La conversión ADC -> mV usa la resolución del ADC, el voltaje de referencia
  y la ganancia del sensor EMG de BITalino, definidas en `config.py`.
