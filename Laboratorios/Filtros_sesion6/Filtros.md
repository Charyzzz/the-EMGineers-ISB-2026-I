
# Filtros Digitales Utilizados en Señales Biomédicas

**Ingeniería Biomédica – 7mo Ciclo**  
**Procesamiento de Señales Biomédicas | 2025**

---

# 1. Introducción

El procesamiento de señales biomédicas representa uno de los pilares fundamentales de la ingeniería biomédica moderna. Las señales como el electrocardiograma (ECG), el electroencefalograma (EEG) y la electromiografía (EMG) contienen información clínica de gran valor; sin embargo, durante su adquisición se ven inevitablemente contaminadas por distintos tipos de ruido e interferencias que dificultan su análisis e interpretación.

En este contexto, los filtros digitales constituyen herramientas esenciales para la extracción de la información fisiológica relevante, permitiendo atenuar o eliminar componentes no deseadas sin comprometer la integridad de la señal original. A diferencia de los filtros analógicos, los filtros digitales ofrecen mayor flexibilidad, repetibilidad y facilidad de implementación en sistemas embebidos y plataformas computacionales.

---

# 2. Tipos de Filtros Digitales
<img width="1182" height="432" alt="Image" src="https://github.com/user-attachments/assets/66223dc6-a5e7-45f8-8d64-c45c4853e102" />
<img width="1138" height="410" alt="image" src="https://github.com/user-attachments/assets/d4891caa-2d0c-4c84-9b4f-b78adfd3512f" />
<div align="center">Figura 1. Señal base y sus componentes.</div>


## Código de generación de señal base

```python
# GENERACIÓN DE LA SEÑAL BASE

# Parámetros de muestreo
Fs = 20000  # Frecuencia de muestreo (Hz)
Ts = 1 / Fs # Periodo de muestreo (s)
M  = 320    # Número de muestras

n = np.arange(M)
t = n / Fs  # Eje de tiempo (s)

# Componentes de la señal
F1 = 70   # Frecuencia baja (Hz)
F2 = 970  # Frecuencia alta (Hz)

T1 = 1 / F1
T2 = 1 / F2

x1 = np.sin(7 * np.pi * F1 * n / Fs)   # Señal base
x2 = np.sin(3 * np.pi * F2 * n / Fs)   # Ruido de alta frecuencia

# Ruido de red eléctrica a 60 Hz
ruido_60hz = 0.5 * np.sin(2 * np.pi * 60 * t)

# Ruido blanco aleatorio
np.random.seed(42)
ruido_blanco = 0.3 * np.random.randn(M)

# Señal compuesta final
signal = x1 + x2 + ruido_60hz + ruido_blanco
```

---

## 2.1 Filtro Pasa Baja (Low-Pass Filter)

El filtro pasa baja permite el paso de frecuencias por debajo de una frecuencia de corte definida, atenuando las componentes de alta frecuencia. En el ámbito biomédico es especialmente útil para conservar las componentes lentas y principales de la señal fisiológica, como las ondas P, QRS y T en el ECG, eliminando simultáneamente interferencias de origen muscular o electrónico (1).

Su aplicación es amplia en señales ECG y EEG, donde el contenido espectral relevante se concentra en frecuencias relativamente bajas. En ECG se utiliza típicamente con una frecuencia de corte entre 35 y 45 Hz, mientras que en EEG el límite suele establecerse por debajo de los 40 Hz. Puede implementarse tanto con estructuras FIR, que garantizan estabilidad incondicional y fase lineal, como con filtros IIR, de mayor eficiencia computacional (1).

| Parámetro | Descripción |
|---|---|
| Señales | ECG, EEG |
| Ruido eliminado | Ruido electromiográfico, interferencia electrónica, componentes de alta frecuencia |
| Frecuencias típicas | ECG: 35–45 Hz · EEG: < 40 Hz |
| Implementación | FIR o IIR |

<img width="1195" height="503" alt="Image" src="https://github.com/user-attachments/assets/6bc51520-ac0c-4410-8c54-db0f8c143c27" />
<img width="1162" height="441" alt="Image" src="https://github.com/user-attachments/assets/ec014c5d-9a9d-422a-85a2-d70ebef615bb" />
<div align="center">Figura 2. Implementación de filtro pasa baja FIR y espectro (150 Hz). </div>

---

## 2.2 Filtro Pasa Alta (High-Pass Filter)

A diferencia del anterior, el filtro pasa alta atenúa las frecuencias inferiores a la frecuencia de corte y permite el paso de las superiores. Su principal utilidad es la eliminación de la deriva de línea base (*baseline wander*), que se manifiesta en el ECG como variaciones lentas debidas a la respiración o al movimiento del paciente, distorsionando el segmento ST y la amplitud de las ondas (2).

En señales EEG se emplea para eliminar componentes de muy baja frecuencia asociadas a fluctuaciones lentas del sistema de adquisición, mientras que en EMG es necesario para remover artefactos de movimiento que saturan las frecuencias más bajas del espectro muscular. Generalmente se implementa mediante filtros IIR por su eficiencia computacional (2).

| Parámetro | Descripción |
|---|---|
| Señales | ECG, EEG, EMG |
| Ruido eliminado | Baseline wander, movimiento respiratorio, artefactos lentos |
| Frecuencias típicas | ECG: 0.5 Hz · EEG: 0.1–1 Hz · EMG: 10–20 Hz |
| Implementación | IIR (preferente) |
<img width="1155" height="493" alt="Image" src="https://github.com/user-attachments/assets/90c08305-cbea-442e-b4e0-4184275151a1" />
<img width="1205" height="411" alt="Image" src="https://github.com/user-attachments/assets/ccb00d8a-22a5-4489-9197-3c9da5e44741" />
<div align="center">Figura 3. Implementación de filtro pasa alta IIR Butterworth y espectro (20 Hz – orden 4). </div>

---

## 2.3 Filtro Pasa Banda (Band-Pass Filter)

El filtro pasa banda resulta de la combinación en cascada de un filtro pasa alta y uno pasa baja, permitiendo únicamente el paso de un rango de frecuencias delimitado por dos frecuencias de corte. Esto lo convierte en una herramienta muy precisa para aislar la banda espectral de interés clínico, descartando tanto las componentes de muy baja frecuencia como las de muy alta frecuencia (3).

En señales EMG, donde la actividad muscular se distribuye principalmente entre 20 y 450 Hz, es prácticamente indispensable. En EEG se utiliza para aislar bandas de frecuencia cerebrales específicas (delta, theta, alfa, beta y gamma), permitiendo el estudio de estados cognitivos y patológicos (3).

| Parámetro | Descripción |
|---|---|
| Señales | EMG, EEG |
| Ruido eliminado | Ruido de baja y alta frecuencia, artefactos de movimiento |
| Frecuencias típicas | EMG: 20–450 Hz · EEG: 0.5–40 Hz |
| Implementación | Combinación de filtros pasa alta y pasa baja |
<img width="1241" height="585" alt="image" src="https://github.com/user-attachments/assets/a9b279ca-696b-40e6-a9f7-fb40af1cb149" />
<img width="1177" height="413" alt="Image" src="https://github.com/user-attachments/assets/f285ae76-f9c6-4298-bb5b-eb053622415e" />
<div align="center">Figura 4. Implementación de filtro pasa banda IIR y espectro (20 - 450 Hz – orden 4). </div>

---

## 2.4 Filtro Notch (Band-Stop Filter)

El filtro notch está diseñado para atenuar drásticamente una frecuencia muy específica mientras preserva el resto del espectro. Su aplicación más común en señales biomédicas es la eliminación de la interferencia de la red eléctrica de suministro, que introduce una componente sinusoidal muy definida en las tres señales biomédicas principales (1).

La frecuencia de interferencia varía según la región geográfica: 50 Hz en Europa y Asia, y 60 Hz en América. Dado que estas frecuencias coinciden parcialmente con el espectro de interés de varias señales biomédicas, el diseño del filtro notch debe ser muy selectivo para no distorsionar la señal útil. Se implementa típicamente con estructuras IIR por su eficiencia y alta selectividad frecuencial (1).

| Parámetro | Descripción |
|---|---|
| Señales | ECG, EEG, EMG |
| Ruido eliminado | Interferencia de red eléctrica (*powerline noise*) |
| Frecuencias típicas | 50 Hz (Europa/Asia) · 60 Hz (América) |
| Implementación | IIR (alta selectividad) |
<img width="1237" height="543" alt="Image" src="https://github.com/user-attachments/assets/d7e4208e-ce7f-4963-9877-b5ad6190f08b" />
<img width="1197" height="416" alt="Image" src="https://github.com/user-attachments/assets/f14f47a9-b0ce-4b9a-a289-f943d86204ac" />
<div align="center">Figura 5. Implementación de filtro Notch IIR (60 Hz). </div>

---

## 2.5 Filtro Adaptativo

A diferencia de los filtros convencionales con coeficientes fijos, el filtro adaptativo ajusta dinámicamente sus parámetros en función de las características estadísticas de la señal de entrada, lo que lo hace especialmente útil cuando el ruido es no estacionario, situación frecuente en registros biomédicos obtenidos durante movimiento o actividad (4).

Su principal aplicación es la remoción de artefactos oculares en registros EEG, donde los movimientos de los párpados generan componentes de gran amplitud que se superponen a la actividad cerebral. También se utiliza en ECG ambulatorio para eliminar artefactos de movimiento durante el ejercicio. Los algoritmos más comunes son el LMS (*Least Mean Squares*) y el RLS (*Recursive Least Squares*), que optimizan iterativamente los coeficientes del filtro (4).

| Parámetro | Descripción |
|---|---|
| Señales | EEG, ECG |
| Ruido eliminado | Artefactos oculares, movimiento, ruido no estacionario |
| Frecuencias típicas | Variables según señal y algoritmo utilizado |
| Implementación | Algoritmos LMS o RLS |
<img width="1271" height="582" alt="Image" src="https://github.com/user-attachments/assets/2e72b0b2-f680-4413-904f-f65fd8ffecc7" />
<img width="1255" height="347" alt="Image" src="https://github.com/user-attachments/assets/25425db1-7ede-44a3-8bc0-a5762ccbb3b2" />
<div align="center">Figura 6. Implementación de filtro adaptativo LMS (60 Hz). </div>

---

## 2.6 Filtro Butterworth

El filtro Butterworth se caracteriza por presentar una respuesta en frecuencia máximamente plana en la banda de paso, sin ondulaciones (*ripple*), lo que resulta crucial para preservar la morfología de la señal biomédica, especialmente en el análisis del complejo QRS del ECG o de los ritmos cerebrales en EEG (5).

Su respuesta gradual en la banda de transición lo hace apropiado para aplicaciones donde la distorsión de amplitud debe minimizarse. En la práctica se configura habitualmente como pasa banda combinando etapas pasa alta y pasa baja de tipo Butterworth. Su implementación mediante filtros IIR requiere un orden menor que los equivalentes FIR para lograr una selectividad comparable, reduciendo el costo computacional en sistemas embebidos o de tiempo real (5).

| Parámetro | Descripción |
|---|---|
| Señales | ECG, EEG, EMG |
| Ruido eliminado | Ruido de alta frecuencia, interferencia muscular, artefactos electrónicos, variaciones lentas |
| Frecuencias típicas | ECG: 0.5–40 Hz · EEG: 0.5–50 Hz · EMG: 20–450 Hz |
| Implementación | IIR (respuesta plana en banda de paso) |
<img width="1227" height="517" alt="Image" src="https://github.com/user-attachments/assets/99a6fd30-4b3a-4f54-8a30-8e3321303996" />
<img width="1198" height="470" alt="Image" src="https://github.com/user-attachments/assets/e2066e13-8501-4486-90b5-f149b35e9645" />
<div align="center">Figura 7. Implementación de filtro Butterworth pasa banda (0.5 - 150 Hz – orden 4). </div>

---

## 2.7 Filtro de Media Móvil (Moving Average Filter)

El filtro de media móvil es el filtro digital de implementación más sencilla. Su principio consiste en reemplazar cada muestra de la señal por el promedio aritmético de un número determinado de muestras consecutivas, produciendo un efecto de suavizado que reduce las fluctuaciones rápidas. Al ser un filtro FIR no recursivo, es incondicionalmente estable (6).

Su principal limitación es la falta de selectividad frecuencial fina: la frecuencia de corte efectiva depende del número de muestras promediadas y de la frecuencia de muestreo, sin una transición abrupta. Sin embargo, resulta muy efectivo para reducir ruido aleatorio en señales de monitoreo continuo como el ECG, especialmente en sistemas de bajo costo o recursos computacionales limitados (6).

| Parámetro | Descripción |
|---|---|
| Señales | ECG, señales de monitoreo continuo |
| Ruido eliminado | Ruido aleatorio, fluctuaciones rápidas, variaciones de alta frecuencia |
| Frecuencias típicas | Depende del número de muestras y la frecuencia de muestreo |
| Implementación | FIR no recursivo |
<img width="1267" height="557" alt="Image" src="https://github.com/user-attachments/assets/43dbe572-2191-42bd-a802-1ce2594e5548" />
<img width="1247" height="432" alt="Image" src="https://github.com/user-attachments/assets/e4f3fd42-0c0e-470e-ac57-11cac7d3bf1e" />
<div align="center">Figura 8. Implementación de filtro de media móvil (15 muestras). </div>

---

# 3. Estructuras de Implementación: FIR vs IIR

Todos los filtros descritos pueden clasificarse según su estructura en dos grandes grupos: filtros de respuesta finita al impulso (FIR) y filtros de respuesta infinita al impulso (IIR). La elección entre uno u otro depende del tipo de aplicación, los recursos computacionales y los requerimientos de fase y estabilidad.

---

## 3.1 Filtros FIR

Los filtros FIR calculan cada muestra de salida como una combinación lineal de un número finito de muestras de entrada pasadas, sin realimentación. Esto les confiere estabilidad incondicional y la posibilidad de lograr fase lineal exacta, lo que garantiza que todas las frecuencias de la señal sean retardadas por igual, preservando la forma de onda.

Su principal desventaja es que requieren un mayor número de coeficientes para lograr transiciones selectivas. El filtro de media móvil es el ejemplo más simple de esta categoría (6).

El diseño de filtros FIR generalmente se realiza mediante el método de ventaneo, utilizando funciones como Hamming, Hann o Bartlett para controlar el nivel de atenuación fuera de la banda de paso.

---

## 3.2 Filtros IIR

Los filtros IIR incorporan realimentación en su estructura: la salida actual depende tanto de muestras de entrada como de muestras de salida anteriores. Esto permite lograr una respuesta frecuencial selectiva con un orden significativamente menor que los FIR equivalentes.

Sin embargo, introducen distorsión de fase no lineal y pueden ser inestables si los polos del sistema se ubican fuera del círculo unitario. El filtro Butterworth, el notch y los filtros pasa alta convencionales pertenecen a esta categoría (5).

---

## 3.3 Comparativa general

| Característica | FIR | IIR |
|---|---|---|
| Estabilidad | Siempre estable | Condicional |
| Fase | Lineal (sin distorsión) | No lineal |
| Realimentación | No utiliza | Sí utiliza |
| Orden requerido | Mayor | Menor |
| Costo computacional | Mayor | Menor |
| Diseño típico | Ventaneo (Hamming, Hann, Bartlett) | Butterworth, Chebyshev, Elíptico |
| Ejemplos en biomédica | Media móvil, FIR ventaneados | Butterworth, Notch, Pasa alta |

---

# 4. Conclusiones

Los filtros digitales son herramientas indispensables en el procesamiento de señales biomédicas. La correcta selección del tipo de filtro depende no solo de la frecuencia del ruido a eliminar, sino también del tipo de señal, los recursos computacionales disponibles y los requerimientos de precisión.

Los filtros pasa baja y pasa alta actúan como bloques base para construir el filtro pasa banda, el más utilizado en sistemas de adquisición de EMG y EEG (3). El filtro notch es prácticamente obligatorio en cualquier sistema que opere en entornos clínicos, dada la ubiquidad de la interferencia de la red eléctrica (1). El filtro Butterworth destaca por su respuesta plana en la banda de paso (5), mientras que el filtro adaptativo ofrece la mayor flexibilidad frente a ruidos variables en el tiempo (4).

Desde el punto de vista de implementación, los filtros FIR garantizan estabilidad y fase lineal a costa de mayor orden, mientras que los IIR ofrecen mayor eficiencia con menor número de coeficientes. En muchos sistemas reales se combinan ambas estructuras para lograr el mejor resultado posible (5, 6).

---

# Referencias

1. Ahmed A, Al-obaidi M. *A review of ECG signal filtering approaches*. Global Journal of Engineering and Technology Advances. 2022.

2. van der Bijl K, Elgendi M, Menon C. *Automatic ECG Quality Assessment Techniques: A Systematic Review*. Diagnostics. 2022.

3. Boyer M, Bouyer L, Roy J, Campeau-Lecours A. *Reducing Noise, Artifacts and Interference in Single-Channel EMG Signals: A Review*. Sensors. 2023.

4. Queiroz C, et al. *Single channel approach for filtering electroencephalographic signals strongly contaminated with facial electromyography*. Frontiers in Computational Neuroscience. 2022.

5. Kim M, Yoo S, Kim C. *Miniaturization for wearable EEG systems: recording hardware and data processing*. Biomedical Engineering Letters. 2022.

6. Pravin C, Ojha V. *A novel ECG signal denoising filter selection algorithm based on conventional neural networks*. arXiv. 2022.# Filtros Digitales Utilizados en Señales Biomédicas
