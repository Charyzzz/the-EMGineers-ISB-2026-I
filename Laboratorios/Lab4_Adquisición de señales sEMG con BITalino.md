# LAB 4: Adquisición de señales sEMG con BITalino
## 1. Introducción
El presente laboratorio trabajó la adquisición y análisis de señales biomédicas como EMG utilizando el kit BITalino (r)evolution Board y el software OpenSignals (r)evolution. Estas herramientas permiten la captura y visualización de señales fisiológicas mediante electrodos conectados al músculo.

Durante la práctica, se realizó la configuración del sistema de adquisición, el cual incluye la conexión Bluetooth módulo-computadora y configuración del programa. Posteriormente, se llevó a cabo la visualización y registro de las señales obtenidas, permitiendo su análisis tanto en tiempo real como mediante procesamiento posterior en Python.

## 2. Metodología
### 2. 1. Objetivos

-   Adquirir señales biomédicas de EMG y ECG.
-   Configurar correctamente el sistema BITalino.
-   Extraer y procesar la información de las señales adquiridas mediante OpenSignals (r)evolution.

### 2.2. Materiales y equipos

#### Kit BITalino (r)evolution
Plataforma integrada para adquisición de señales fisiológicas. Incluye:
-   Placa BITalino (r)evolution
-   Electrodos
-   Cable de 3 vías (para EMG/ECG/EEG) de 30 cm.
-   Cable de 2 vías (para EDA) de 10 cm.
-   Batería Li-Po 3.7 V, 500 mAh

#### Laptop como módulo de procesamiento de datos
Laptop con Windows 11 y el software OpenSignals (r)evolution instalado para la adquisición, visualización y almacenamiento de las señales.

### 2.3. Sujetos de estudio
Participaron voluntariamente dos estudiantes del curso _Introducción a Señales Médicas_ de la Universidad Peruana Cayetano Heredia, sin antecedentes de lesiones musculoesqueléticas en miembros superiores o inferiores.

### 2.4. Procedimiento experimental
**Colocación de electrodos**
Para cada músculo evaluado, se siguió el siguiente protocolo:
-   Se trazó una línea imaginaria sobre el eje longitudinal del músculo.
-   Se colocaron dos electrodos activos alineados con las fibras musculares, separados entre 4 y 5 cm.
-   Se ubicó un electrodo de referencia en una zona ósea cercana a la articulación humero-radio-cubital.
-   Se conectó el cable de tres derivaciones al sensor EMG y este al canal analógico A1 del BITalino.
-   Se verificó que la señal basal presentara bajo nivel de ruido (pico a pico menor a 0.05 mV).

**Músculos y ejercicios evaluados**
Para el músculo Bíceps braquial:
1.  **Ejercicio 1 – Curl de bíceps:**
-   **Posición:** Sentado, con el antebrazo apoyado sobre una mesa y el brazo en abducción de 90°.
- **Medición basal:** 3 registros de 120 segundos cada uno, con el brazo relajado en extensión completa.
-   **Ejecución:** Desde la posición inicial de extensión completa del codo (0°), el sujeto realiza una flexión concéntrica hasta alcanzar 90° de flexión, sosteniendo una mancuerna de 2 kg.
-   **Protocolo de repeticiones:** Se realizan 5 repeticiones o más donde se realiza contracción y relajación (3 segundos cada uno). Se repite el proceso para obtener 3 mediciones del mismo ejercicio.
2.  **Ejercicio 2 – Curl martillo:**
-   **Posición:** El sujeto se coloca en posición sentada, con el brazo extendido en posición vertical, pegado al torso, y el antebrazo en posición neutra (pulgar hacia arriba, palma orientada hacia el cuerpo).
-   **Medición basal:** 3 registros de 120 segundos cada uno, con el brazo relajado en extensión completa.
-   **Ejecución:** Utilizando la misma mancuerna, el sujeto realiza una flexión del codo desde aproximadamente 180° hasta 45°, manteniendo en todo momento el antebrazo en posición neutra.
-   **Protocolo de repeticiones:** Se realizan 5 repeticiones o más donde se realiza contracción y relajación (3 segundos cada uno). Se repite el proceso para obtener 3 mediciones del mismo ejercicio.

Para el caso del músculo Cuádriceps femoral (miembro inferior):
1.  **Ejercicio 1 – Sentadilla (cuádriceps):**
-   **Posición:** El sujeto se coloca de pie, en bipedestación, con los pies separados al ancho de los hombros.
-   **Medición basal:** 3 registros de 30 segundos, de pie en bipedestación estática (sin flexión de rodillas).
-   **Ejecución:** Desde la posición inicial con rodillas extendidas, el sujeto realiza una sentadilla controlada hasta alcanzar aproximadamente 90° de flexión de rodilla (muslos paralelos al suelo). Durante el movimiento, las rodillas se desplazan hacia adelante, sobrepasando ligeramente la línea de los pies, con el objetivo de incrementar la activación del cuádriceps.
-   **Protocolo de repeticiones:** Se realizan 5 repeticiones o más de sentadilla (fase excéntrica y concéntrica) de 4 segundos de duración, con descanso de 4 segundos entre cada repetición. Se repite el proceso para obtener 3 mediciones del mismo ejercicio.

**Procedimiento de adquisición**
Para cada ejercicio se siguió el protocolo basado en el manual HomeGuide #1 de PLUX:
-   Se inició la grabación en OpenSignals.
-   Se registró una línea basal de 30 segundos mínimo sin contracción muscular.
-   Se realizaron 5 ciclos consecutivos de contracción-relajación, con intensidad creciente, siendo la última contracción a máxima fuerza voluntaria (MVC).
-   Se registró otra línea basal de 30 segundos.
-   Se guardó el archivo en formato .txt para su posterior procesamiento.
-   Todas las mediciones se realizaron en un ambiente con temperatura controlada (20–22 °C) y sin fuentes de interferencia electromagnética evidentes (celulares apagados, laptops alejadas del cable de alimentación).

**Visualización de señales**
Las señales almacenadas se procesaron con un script en Google Colab y python utilizando las siguientes etapas para visualizar su comportamiento durante la construcción muscular:
-   **Filtrado:** filtro Butterworth pasa banda de 4° orden entre 20 y 500 Hz, seguido de un filtro notch de 2° orden a 60 Hz.
-   **Rectificación:** completa (valor absoluto).
-    **Cálculo del RMS:** ventana deslizante de 250 ms con solapamiento de 125 ms.
-   **Normalización:** cada valor RMS se expresó como porcentaje de la contracción voluntaria máxima (%CVM) obtenida en el ciclo más intenso.

### 2.4. Procedimiento experimental
#### 2.5.1. Ploteo de las señales en OpenSignals
Con ayuda del software OpenSignals (r)evolution se importaron las señales crudas tomadas en cada ejercicio con el fin de visualizarlas gráficamente. Esto nos sirve para identificar la morfología de la señal e identificar cambios en ella al reaccionar al movimiento de los músculos.

**a. Ejercicio 1 – Curl de bíceps:**
|  **Primera toma**  | **Segunda toma** | **Tercera toma** |
|:------------:|:---------------:|:------------:|
**b. Ejercicio 2 - Curl martillo:**
|  **Video**  | **Señal en OpenSignals** |
|:------------:|:---------------:|:------------:|
**c. Ejercicio 3 - Sentadilla:**
|  **Video**  | **Señal en OpenSignals** |
|:------------:|:---------------:|:------------:|

#### 2.5.2. Ploteo de las señales en Python
Las señales adquiridas fueron pasadas a Python para plotear el momento de la contracción muscular.

**a. Ejercicio 1: Curl de bíceps**
**b. Ejercicio 2: Curl martillo**
**c. Ejercicio 3: Sentadilla**

#### 2.5.3. Archivo de datos de las señales adquiridas
-   Documentos
-   Programa de ploteo (Jupyter Notebook)

## 3. Discusión
### 3.1. Análisis de resultados
**Ejercicio 1 - Curl de bíceps**
En las tres tomas del curl de bíceps se observa la activación del músculo bíceps braquial durante la flexión del mismo. La señal EMG muestra momentos de gran amplitud, esto nos indica mayor activación del músculo y momentos de poca amplitud indicando relajación del músculo. En la primera toma los picos de amplitud alcanzan aproximadamente (valor que no veo), mientras que en las zonas de reposo la señal se mantiene cerca del valor basal. Esto es consistente con el reclutamiento progresivo de unidades motoras durante la contracción isotónica. En la segunda y tercera toma se observa cierta variabilidad durante las repeticiones, esto puede atribuirse a la fatiga muscular acumulada o ligeras diferencias en la ejecución del ejercicio.
La FFT del ejercicio muestra que la mayor parte de la energía espectral se concentra entre 20 y 150 Hz, que es el rango típico de actividad EMG superficial para músculos de miembro superior. El pico visible alrededor de 60 Hz en la FFT podría corresponder a interferencia de la red, esto es esperable en entornos no completamente aislados electromagnéticamente.

**Ejercicio 2 - Curl martillo**
La señal del curl martillo presenta un patrón similar al curl de bíceps, con algunas variaciones. Al mantener el antebrazo en posición neutra, la activación del bíceps braquial es parcialmente reducida en favor del músculo braquiorradial y braquial anterior, que son los principales en esta posición. Esto explica por qué visualmente la forma de la señal difiere ligeramente entre ambos ejercicios. La amplitud máxima registrada es comparable, picos que no conozco y la FFT muestra un comportamiento similar con mayor potencia en frecuencias bajas y caída progresiva hacia frecuencias altas.

**Ejercicio 3 - Sentadilla (cuádriceps)**
La señal EMG del cuádriceps durante la sentadilla muestra activación coherente con las fases excéntrica y concéntrica del movimiento. La fase de mayor activación muscular (número que no se)concentra aproximadamente entre las muestras num y num, lo que corresponde a la fase concéntrica, retorno a posición de pie, donde el cuádriceps trabaja como extensor de rodilla contra gravedad. La fase excéntrica, descenso,también muestra activación, aunque de menor amplitud. El cuádriceps, al ser un músculo de gran volumen, genera señales de mayor amplitud y con mayor contenido de frecuencias bajas comparado con músculos más pequeños.
### 3.2. Limitaciones (basado en referencias)
**Ruido e interferencia electromagnética**
A pesar de haber apagado los celulares y tener temperatura controlada, el entorno del laboratorio no es un ambiente clínicamente aislado. La presencia de equipos eléctricos cercanos puede introducir ruido de línea a 60 Hz, visible en las FFT. Hermens et al. establecen que el control del ambiente electromagnético es crítico para la validez de las mediciones sEMG superficiales [1].

**Colocación de electrodos y variabilidad inter-sujeto**
La colocación manual de electrodos introduce variabilidad en la señal adquirida. Pequeñas diferencias en la distancia entre electrodos, la posición sobre el músculo o el estado de la piel afectan directamente la amplitud y morfología de la señal. De Luca señala que incluso desplazamientos de pocos milímetros en la posición del electrodo pueden generar diferencias de hasta 30% en la amplitud registrada [2]. Adicionalmente, el proyecto SENIAM recomienda estandarizar la preparación cutánea mediante abrasión y limpieza con alcohol para reducir la impedancia electrodo-piel por debajo de 10 kΩ [1].

**Normalización y MVC**
La contracción voluntaria máxima (MVC) utilizada como referencia para la normalización en %CVM fue obtenida dentro del mismo protocolo experimental. Sin embargo, lograr una MVC verdadera requiere motivación verbal y familiarización previa. Konrad advierte que si la MVC registrada no corresponde al esfuerzo máximo real del sujeto, todos los valores normalizados quedarán sobreestimados, comprometiendo la comparabilidad entre sujetos y condiciones [3].

**Artefactos de movimiento**
Durante ejercicios dinámicos como la sentadilla el movimiento del cable y los electrodos respecto a la piel genera artefactos de baja frecuencia. Si bien el filtro pasa-banda desde 20 Hz ayuda a mitigarlos, Winter señala que en contracciones dinámicas estos artefactos pueden solaparse con componentes reales de la señal, especialmente cuando la velocidad del movimiento es elevada [4].

## 4. Referencias
- [1] H. J. Hermens, B. Freriks, C. Disselhorst-Klug, y G. Rau,
   "Development of recommendations for SENIAM surface electromyography
      sensors and sensor placement procedures," Journal of Electromyography
   and Kinesiology, vol. 10, no. 5, pp. 361–374, 2000.
 - [2] C. J. De Luca, "The use of surface electromyography in biomechanics," Journal of Applied Biomechanics, vol. 13, no. 2, pp. 135–163, 1997.
- [3] P. Konrad, The ABC of EMG: A practical introduction to kinesiological electromyography. Noraxon USA, 2005.
- [4] D. A. Winter, Biomechanics and motor control of human movement, 4th ed. Wiley, 2009.
