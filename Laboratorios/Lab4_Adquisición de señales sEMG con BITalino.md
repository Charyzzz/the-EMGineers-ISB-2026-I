# LAB 4: Adquisición de señales sEMG con BITalino
## 1. Introducción
El presente laboratorio trabajó la adquisición y análisis de señales biomédicas como EMG utilizando el kit BITalino (r)evolution Board y el software OpenSignals (r)evolution. Estas herramientas permiten la captura y visualización de señales fisiológicas mediante electrodos conectados al músculo.

Durante la práctica, se realizó la configuración del sistema de adquisición, el cual incluye la conexión Bluetooth módulo-computadora y configuración del programa. Posteriormente, se llevó a cabo la visualización y registro de las señales obtenidas, permitiendo su análisis tanto en tiempo real como mediante procesamiento posterior en Python.

## 2. Metodología
### 2.1. Objetivos

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

<div align="center">
<img width="400" height="400" alt="bitalino_kit" src="https://github.com/user-attachments/assets/93c523c5-eeea-46d9-bde6-6dd9f19d75ca" />
</div>

#### Laptop como módulo de procesamiento de datos
Laptop con Windows 11 y el software OpenSignals (r)evolution instalado para la adquisición, visualización y almacenamiento de las señales.
<div align="center">
<img width="650" height="150" alt="opensignals_logo_small-1024x241" src="https://github.com/user-attachments/assets/606cad60-55d1-401c-9253-378ab69e5927" />
</div>

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

---
**Músculos y ejercicios evaluados**
---
Para el músculo Bíceps braquial:

**Ejercicio 1 – Curl de bíceps:**
-   **Posición:** Sentado, con el antebrazo apoyado sobre una mesa y el brazo en abducción de 90°.
- **Medición basal:** 3 registros de 120 segundos cada uno, con el brazo relajado en extensión completa.
-   **Ejecución:** Desde la posición inicial de extensión completa del codo (0°), el sujeto realiza una flexión concéntrica hasta alcanzar 90° de flexión, sosteniendo una mancuerna de 2 kg.
-   **Protocolo de repeticiones:** Se realizan 5 repeticiones o más donde se realiza contracción y relajación (3 segundos cada uno). Se repite el proceso para obtener 3 mediciones del mismo ejercicio.

**Ejercicio 2 – Curl martillo:**
-   **Posición:** El sujeto se coloca en posición sentada, con el brazo extendido en posición vertical, pegado al torso, y el antebrazo en posición neutra (pulgar hacia arriba, palma orientada hacia el cuerpo).
-   **Medición basal:** 3 registros de 120 segundos cada uno, con el brazo relajado en extensión completa.
-   **Ejecución:** Utilizando la misma mancuerna, el sujeto realiza una flexión del codo desde aproximadamente 180° hasta 45°, manteniendo en todo momento el antebrazo en posición neutra.
-   **Protocolo de repeticiones:** Se realizan 5 repeticiones o más donde se realiza contracción y relajación (3 segundos cada uno). Se repite el proceso para obtener 3 mediciones del mismo ejercicio.

---
Para el caso del músculo Cuádriceps femoral (miembro inferior):

**Ejercicio 1 – Sentadilla (cuádriceps):**
-   **Posición:** El sujeto se coloca de pie, en bipedestación, con los pies separados al ancho de los hombros.
-   **Medición basal:** 3 registros de 30 segundos, de pie en bipedestación estática (sin flexión de rodillas).
-   **Ejecución:** Desde la posición inicial con rodillas extendidas, el sujeto realiza una sentadilla controlada hasta alcanzar aproximadamente 90° de flexión de rodilla (muslos paralelos al suelo). Durante el movimiento, las rodillas se desplazan hacia adelante, sobrepasando ligeramente la línea de los pies, con el objetivo de incrementar la activación del cuádriceps.
-   **Protocolo de repeticiones:** Se realizan 5 repeticiones o más de sentadilla (fase excéntrica y concéntrica) de 4 segundos de duración, con descanso de 4 segundos entre cada repetición. Se repite el proceso para obtener 3 mediciones del mismo ejercicio.

**Procedimiento de adquisición**
---
Para cada ejercicio se siguió el protocolo basado en el manual HomeGuide #1 de PLUX:
-   Se inició la grabación en OpenSignals.
-   Se registró una línea basal de 30 segundos mínimo sin contracción muscular.
-   Se realizaron 5 ciclos consecutivos de contracción-relajación, con intensidad creciente, siendo la última contracción a máxima fuerza voluntaria (MVC).
-   Se registró otra línea basal de 30 segundos.
-   Se guardó el archivo en formato .txt para su posterior procesamiento.
-   Todas las mediciones se realizaron en un ambiente con temperatura controlada (20–22 °C) y sin fuentes de interferencia electromagnética evidentes (celulares apagados, laptops alejadas del cable de alimentación).

**Visualización de señales**
Las señales almacenadas se procesaron con un script en Google Colab y python para visualizar su comportamiento durante la construcción muscular.

### 2.4. Procedimiento experimental

#### 2.5.1. Tomas basales

| **Brazo (Curl de bíceps y martillo)** | **Sentadilla** |
|--------------------------------------|---------------|
| <video src="https://github.com/user-attachments/assets/bf00e819-c284-45f9-baec-3188c64ee684"></video> | <video src="https://github.com/user-attachments/assets/9d720962-1ae8-4c7a-99a4-9c86c06da28e"></video> |


#### 2.5.2. Ploteo de las señales en OpenSignals
Con ayuda del software OpenSignals (r)evolution se importaron las señales crudas tomadas en cada ejercicio con el fin de visualizarlas gráficamente. Esto nos sirve para identificar la morfología de la señal e identificar cambios en ella al reaccionar al movimiento de los músculos.

**a. Ejercicio 1 – Curl de bíceps:**
| **Primera toma** | **Segunda toma** | **Tercera toma** |
|------------------|------------------|------------------|
| <img width="400" height="200" alt="primera_toma" src="https://github.com/user-attachments/assets/0c8353f8-30e7-4826-b307-2a681783e4b3" /> | <img src="https://github.com/user-attachments/assets/bd78f8a6-5d9e-4fe4-9ea6-eabb752bf703" width="400" height="200"/> | <img src="https://github.com/user-attachments/assets/d77e09e5-85df-4734-912e-4fa5fa9222ea" width="400" height="200"/> |
| <video src="https://github.com/user-attachments/assets/e9a9ed3d-07c8-4932-99e1-79b0f457e0c5"></video> | <video src="https://github.com/user-attachments/assets/eceda03f-e60c-4ec4-9cc7-454650f6fa4b"></video> | <video src="https://github.com/user-attachments/assets/0762b003-6127-404a-99e5-076aec44c52a"></video> |




**b. Ejercicio 2 - Curl martillo:**
|  **Video**  | **Señal en OpenSignals** |
|-------------|--------------------------|
| <video src="https://github.com/user-attachments/assets/b9bd6c89-998f-4593-b312-d6b748f7e981"></video> | <img width="850" height="400" alt="ejercicio2" src="https://github.com/user-attachments/assets/f492de79-dafb-459f-99fa-5381b54f6ee3" /> |


**c. Ejercicio 3 - Sentadilla:**
|  **Video**  | **Señal en OpenSignals** |
|-------------|--------------------------|
| <video src="https://github.com/user-attachments/assets/308a993f-9b1d-4181-b3ce-323f7f5a97f6"></video> | <img width="712" height="390" alt="ejercicio3" src="https://github.com/user-attachments/assets/073492d3-4db9-4deb-8bc5-57a44dd5a472" /> |

#### 2.5.3. Ploteo de las señales en Python
Las señales adquiridas fueron pasadas a Python para plotear el momento de la contracción muscular.

**a. Ejercicio 1: Curl de bíceps**
|  **Señal**  | **FFT** |
|-------------|--------------------------|
| <img width="589" height="451" alt="grap1" src="https://github.com/user-attachments/assets/4f19678b-542a-4d34-b15e-87f028f52a49" /> | <img width="577" height="448" alt="fft1" src="https://github.com/user-attachments/assets/3c009e72-c86f-4f15-aff9-efdf2f5d9786" /> |


**b. Ejercicio 2: Curl martillo**
|  **Señal**  | **FFT** |
|-------------|--------------------------|
| <img width="589" height="451" alt="grap1" src="https://github.com/user-attachments/assets/673f30f0-bd33-43c8-82e6-5caad54ff203" /> | <img width="577" height="448" alt="fft1" src="https://github.com/user-attachments/assets/db1f29d3-1172-4bec-bb5d-1078754a16dd" /> |


**c. Ejercicio 3: Sentadilla**
|  **Señal**  | **FFT** |
|-------------|--------------------------|
| <img width="584" height="443" alt="grap3" src="https://github.com/user-attachments/assets/ce65a018-3ffa-4839-8fad-1e1b80725939" /> | <img width="575" height="445" alt="fft3" src="https://github.com/user-attachments/assets/46a26249-9cb8-42f1-bd48-f61bdf08d79f" /> |

#### 2.5.4. Archivo de datos de las señales adquiridas
-   [Documentos (.rar)](Laboratorios/documentos/documentos_signals.rar)
-   [Programa de ploteo (Jupyter Notebook)] (Laboratorios/documentos/ploteo_lab4.ipynb)

##  3. Discusión
### 3.1. Análisis de resultados

**Ejercicio 1 - Curl de bíceps**
---
En las tres tomas del curl de bíceps se observa la activación del músculo bíceps braquial durante la flexión del mismo. La señal EMG muestra momentos de gran amplitud, esto nos indica mayor activación del músculo y momentos de poca amplitud indicando relajación del músculo. En la primera toma los picos de amplitud alcanzan aproximadamente 1000 teniendo en cuenta que el valor de referencia es 500, mientras que en las zonas de reposo la señal se mantiene cerca del valor basal. Esto es consistente con el reclutamiento progresivo de unidades motoras durante la contracción isotónica. En la segunda y tercera toma se observa cierta variabilidad durante las repeticiones, esto puede atribuirse a la fatiga muscular acumulada o ligeras diferencias en la ejecución del ejercicio.

La FFT del ejercicio muestra que la mayor parte de la energía espectral se concentra entre 20 y 150 Hz, rango que se acerca al mencionado por Phinyomark respecto a la actividad EMG del bíceps en FFT la cual se concentra principalmente en el rango de 50-150 Hz (1). El pico visible alrededor de 60 Hz en la FFT podría corresponder a interferencia de la red, esto es esperable en entornos no completamente aislados electromagnéticamente.

  

**Ejercicio 2 - Curl martillo**
---
La señal del curl martillo presenta un patrón similar al curl de bíceps. Al mantener el antebrazo en posición neutra, la activación del bíceps braquial es parcialmente reducida en favor del músculo braquiorradial y braquial anterior, que son los principales en esta posición. Esto explica porqué visualmente la forma de la señal difiere ligeramente entre ambos ejercicios. La amplitud máxima registrada es similar en los ejercicios 1 y 2. Además, la FFT muestra un comportamiento similar con mayor potencia en frecuencias bajas y caída progresiva hacia frecuencias altas.


**Ejercicio 3 - Sentadilla (cuádriceps)**
---
La señal EMG del cuádriceps durante la sentadilla muestra activación coherente con las fases excéntrica (descenso) y concéntrica (ascenso) del movimiento. La fase concéntrica (1000 de amplitud aprox.) muestra mayor activación EMG que la excéntrica (700 de amplitud aprox.), con picos un 30% más altos en amplitud, Orantes-Gonzalez indica que esto es debido a que la fase concéntrica realiza un mayor reclutamiento de fibras rápidas, mientras la fase excéntrica presenta una menor velocidad de conducción (2). Respecto a la FFT, se evidencia un rango más predominante entre 20-150 Hz., el cual mantiene mejor su amplitud en ese rango de Hz.

  
---
### 3.2. Limitaciones (basado en referencias)

**Ruido e interferencia electromagnética**
A pesar de haber apagado los celulares y tener temperatura controlada, el entorno del laboratorio no es un ambiente clínicamente aislado. La presencia de equipos eléctricos cercanos puede introducir ruido de línea a 60 Hz, visible en las FFT. Hermens et al. establece que el control del ambiente electromagnético es crítico para la validez de las mediciones sEMG superficiales (3).

**Colocación de electrodos y variabilidad inter-sujeto**
La colocación manual de electrodos introduce variabilidad en la señal adquirida. Pequeñas diferencias en la distancia entre electrodos, la posición sobre el músculo o el estado de la piel afectan directamente la amplitud y morfología de la señal. De Luca señala que incluso desplazamientos de pocos milímetros en la posición del electrodo pueden generar diferencias de hasta 30% en la amplitud registrada (4). Adicionalmente, el proyecto SENIAM recomienda estandarizar la preparación cutánea mediante abrasión y limpieza con alcohol para reducir la impedancia electrodo-piel por debajo de 10 kΩ (3).

**Normalización y MVC**
La contracción voluntaria máxima (MVC) utilizada como referencia para la normalización en %CVM fue obtenida dentro del mismo protocolo experimental. Sin embargo, lograr una MVC verdadera requiere motivación verbal y familiarización previa. Konrad advierte que si la MVC registrada no corresponde al esfuerzo máximo real del sujeto, todos los valores normalizados quedarán sobreestimados, comprometiendo la comparabilidad entre sujetos y condiciones (5).

**Artefactos de movimiento**
Durante ejercicios dinámicos como la sentadilla el movimiento del cable y los electrodos respecto a la piel genera artefactos de baja frecuencia. Si bien el filtro pasa-banda desde 20 Hz ayuda a mitigarlos, Winter señala que en contracciones dinámicas estos artefactos pueden solaparse con componentes reales de la señal, especialmente cuando la velocidad del movimiento es elevada (6).

---
### 3.3. Quiz
En esta sección encontrarás algunas preguntas para que trabajes durante tu sesión en casa y explores el sensor EMG.

- **Q1. Which are the significant frequencies for EMG acquisitions? Are they the same in all body areas such as facial area?**
- **Q2. Which kind of filter is essential when working with EMG signals? Why do we need to apply such a filter?**
Un filtro pasa bajas es esencial para el trabajo con señales EMG, este elimina ruido no deseado de la señal y lo adecúa solo a las frecuencias que contienen actividad muscular.
- **Q3. How does the amplitude differ in each muscular contraction? Is there a difference for body locations?**
La amplitud de la señal EMG varía según el tamaño del músculo y la cantidad de fibras musculares involucradas, los músculos más grandes generan voltajes mayores y los más pequeños generan voltajes menores. Las señales suelen estar en el rango de milivoltios. Además, durante un experimento, las fases de activación muestran amplitudes distintas dependiendo de la intensidad de la contracción. Por ejemplo:
En la segunda toma del curl de bíceps podemos ver en qué momento se recluta mayor número de fibras musculares y saber en qué parte del ejercicio estaba.
- **Q4. Show a screenshot of a relevant portion of Electromyography (EMG) data within the experiment proposed on Section D of a facial muscle of interest. Does this signal correspond to what you expected? Why? Which emotion and action did you perform to trigger the muscle? Which muscle did you trigger?**
- **Q5. To the best of your knowledge, does the EMG amplitude equal to the amount of force that you have generated with your muscle?**
La amplitud de la señal es una manifestación eléctrica de los potenciales de acción y dependen del número de fibras musculares activadas. Si bien un aumento en la amplitud refleja una mayor actividad muscular y generalmente más fuerza, no se puede asegurar que sean iguales, sino que la amplitud es un indicador de la activación de las fibras durante la contracción.

## 4. Referencias
1. Phinyomark A, Thongpanja S, Hu H, Phukpattaranont P, Tukulakan K. Time-dependent EMG power spectrum parameters of biceps brachii during fatiguing isometric contraction. In: 2012 IEEE-EMBS Conference on Biomedical Engineering and Sciences (IECBES); 2012; Langkawi, Malaysia. p. 953-958.
2. Orantes-Gonzalez E, Heredia-Jimenez J, Lindley SB, Richards JD, Chapman GJ. An exploration of the motor unit behaviour during the concentric and eccentric phases of a squat task performed at different speeds. Sports Biomech. 2023;24(10):3081-3092.
3. Hermens HJ, Freriks B, Disselhorst-Klug C, Rau G. Development of recommendations for SENIAM surface electromyography sensors and sensor placement procedures. J Electromyogr Kinesiol. 2000;10(5):361-374.
4. De Luca CJ. The use of surface electromyography in biomechanics. J Appl Biomech. 1997;13(2):135-163.
5. Konrad P. The ABC of EMG: a practical introduction to kinesiological electromyography. Scottsdale (AZ): Noraxon USA; 2005.
6. Winter DA. Biomechanics and motor control of human movement. 4th ed. Hoboken (NJ): Wiley; 2009.


