
# Laboratorio 6  
# Adquisición de señales EEG con BITalino

---

# 1. Introducción

El laboratorio realizado hizo uso del kit BITalino (r)evolution Board y el software OpenSignals (r)evolution. Estas herramientas permiten la adquisición y visualización de señales fisiológicas respectivamente. En el contexto del laboratorio, se utilizaron para obtener y analizar señales EEG mediante el uso de electrodos colocados en una configuración reducida frontal referencial.

---

# 2. Metodología

## 2.1 Materiales y equipos

### Kit BITalino (r)evolution

El kit utilizado corresponde a una plataforma todo-en-uno que contiene distintos sensores y electrodos necesarios para adquirir señales fisiológicas. Este kit contiene los siguientes componentes:

- Placa BITalino (r)evolution  
- Electrodos  
- Cable de 3 vías (para EMG/ECG/EEG) de 30 cm  
- Cable de 2 vías (para EDA) de 10 cm  
- Batería Li-Po 3.7 V, 500 mAh  

**Figura 1.** Kit BITalino.

### Laptop como módulo de procesamiento de datos

Se utilizó una laptop con Windows 11 y el software OpenSignals (r)evolution instalado para la adquisición, visualización y almacenamiento de las señales fisiológicas.

**Figura 2.** Software OpenSignals.

---

## 2.2 Sujetos de estudio

Participó voluntariamente un estudiante del curso *Introducción a Señales Biomédicas* de la Universidad Peruana Cayetano Heredia, sin antecedentes de enfermedades neurológicas ni otras afecciones clínicas.

---

## 2.3 Configuración de electrodos (EEG)

Se trabajó con una derivación reducida frontal referencial, conformada por tres electrodos:

- Frontal parietal 1 (Fp1) – Electrodo 1 (rojo)  
- Frontal parietal 2 (Fp2) – Electrodo 2 (negro)  
- Occipital 2 (O2) – Electrodo 3 (blanco), utilizado como tierra  

**Figura 3.** Ubicación de los nodos en un EEG estándar.  
F = frontal, Fp = frontal parietal, Fz = frontal medio, T = temporal, C = central, Cz = central medio, O = occipital y P = parietal. [a]

[a]: https://www.researchgate.net/publication/308892147_Diagnosis_of_epilepsy_from_the_reconstruction_of_the_attractor_of_EEG

**Figura 4.** Ejemplo de serie temporal correspondiente al EEG estándar de un paciente sano con los ojos abiertos. [a]

---

## 2.4 Actividades realizadas

### Colocación de electrodos

Para la adquisición de la señal EEG se utilizaron tres electrodos desechables conectados al sensor EEG ensamblado de BITalino. Los electrodos utilizados correspondieron a:

- Positivo  
- Negativo  
- Referencia  

Siguiendo la configuración descrita anteriormente, se realizó la colocación de los electrodos y posteriormente una prueba basal para verificar la correcta adquisición de la señal EEG. Los electrodos permanecieron fijos durante todo el procedimiento experimental.

---

### Adquisición de señales

Cada adquisición se realizó bajo una condición experimental distinta, con el objetivo de estudiar las diferencias de las señales EEG frente a diversos estímulos fisiológicos y sensoriales.

---

### EEG basal

El participante permaneció sentado en un ambiente con mínima estimulación sensorial, con los ojos cerrados y cubiertos mediante una casaca negra para bloquear completamente la luz. Se indicó evitar movimientos oculares y corporales, además de mantener una respiración controlada.

Se utilizaron audífonos apagados para disminuir la percepción del ruido ambiental sin generar interferencias eléctricas. La adquisición tuvo una duración de un minuto.

---

### EEG con ojos abiertos

Se retiró la cubierta oscura y se indicó al participante abrir los ojos y fijar la mirada en un punto estacionario, evitando movimientos corporales y parpadeos excesivos. El registro se realizó durante un minuto.

---

### EEG basal posterior a ojos abiertos

Finalizada la adquisición anterior, se restablecieron las condiciones basales iniciales para obtener un nuevo registro EEG. Esta adquisición tuvo una duración de 30 segundos.

---

### EEG con parpadeo y masticación constante

En esta condición, el participante realizó movimientos constantes de masticación junto con parpadeo rápido y continuo mientras fijaba la mirada en un punto de referencia. El objetivo fue evidenciar la presencia de artefactos fisiológicos en la señal EEG. El registro tuvo una duración de un minuto.

---

### EEG basal posterior a parpadeo y masticación constante

Posteriormente se realizó una nueva adquisición basal bajo las mismas condiciones iniciales, con el objetivo de comparar la señal respecto a la condición anterior. Esta toma tuvo una duración de 30 segundos.

---

### Toma libre

Esta adquisición tuvo como objetivo registrar señales EEG bajo dos condiciones emocionales distintas:

1. Música relajante  
2. Música estresante  

El participante permaneció con los ojos cerrados y cubiertos, evitando movimientos oculares y corporales durante la adquisición. Los estímulos auditivos fueron reproducidos mediante audífonos sin cancelación de ruido. Cada estímulo tuvo una duración aproximada de un minuto.

---

## 2.5 Archivos utilizados

- Archivo de datos de las señales adquiridas  
- Documentos del laboratorio  
- Programa de procesamiento y ploteo en Jupyter Notebook  

---

# 3. Resultados

A continuación, se muestran los resultados obtenidos mediante procesamiento en Python. Las señales adquiridas fueron convertidas de ADC a microvoltios y posteriormente se eliminó la componente DC. Para la visualización se extrajeron segmentos de 10 segundos de cada registro.

---

## 3.1 EEG basal

*(Insertar figura correspondiente)*

---

## 3.2 EEG con ojos abiertos

*(Insertar figura correspondiente)*

---

## 3.3 EEG basal posterior a ojos abiertos

*(Insertar figura correspondiente)*

---

## 3.4 EEG con parpadeo y masticación constante

*(Insertar figura correspondiente)*

---

## 3.5 EEG basal posterior a parpadeo y masticación constante

*(Insertar figura correspondiente)*

---

## 3.6 Toma libre

### Música relajante

*(Insertar figura correspondiente)*

### Música estresante

*(Insertar figura correspondiente)*

---

# 4. Discusión

## 4.1 Condiciones basales

Durante el estado basal, el participante permaneció en reposo, con los ojos cerrados y en un entorno con mínima estimulación sensorial. Estas condiciones favorecen la aparición de ritmos asociados al estado de relajación cerebral, principalmente actividad alfa y theta (1).

En el análisis espectral mediante FFT se observó un pico predominante en frecuencias menores a 5 Hz, cercano al límite superior de la banda theta, así como un segundo incremento alrededor de los 8 Hz, compatible con actividad alfa de baja frecuencia. Este comportamiento es consistente con un estado de reposo y mínima estimulación visual, donde se incrementa la sincronización neuronal cortical (2).

El registro basal posterior a la toma con ojos abiertos presentó características similares al basal inicial, manteniéndose los picos observados en frecuencias menores a 5 Hz y alrededor de 8 Hz. Sin embargo, también apareció un incremento adicional entre 12 y 15 Hz, correspondiente a actividad en el límite superior de la banda alfa e inicio de la banda beta. Este comportamiento podría relacionarse con una persistencia parcial de la activación cortical generada durante la exposición visual previa, así como con fluctuaciones fisiológicas normales del estado de atención del participante (1,3).

---

## 4.2 Condiciones con ojos abiertos

Durante la condición con ojos abiertos se observó una distribución espectral similar a la registrada en estado basal, manteniéndose un pico importante en frecuencias menores a 5 Hz y otro cercano a los 8 Hz. Sin embargo, la señal presentó mayor irregularidad temporal y una distribución espectral ligeramente más extendida hacia frecuencias superiores, compatible con una mayor activación cortical asociada al procesamiento visual y al estado de alerta (1,3).

Aunque el bloqueo alfa clásico suele evidenciar una disminución marcada de la actividad alfa al abrir los ojos, en este registro la presencia de un pico cercano a los 8 Hz podría explicarse por las limitaciones del sistema BITalino, la corta duración de la adquisición o el hecho de que el participante permaneciera relativamente relajado durante la prueba.

---

## 4.3 Condiciones con parpadeo y masticación constante

En esta condición se introdujeron deliberadamente artefactos fisiológicos con el objetivo de evidenciar su influencia sobre el registro EEG.

El análisis espectral mostró un incremento muy marcado de actividad en la región de bajas frecuencias, principalmente entre 0 y 5 Hz. Esta elevada actividad se relaciona directamente con los potenciales generados por el parpadeo, ya que los movimientos oculares producen señales de gran amplitud que afectan especialmente a los electrodos ubicados en regiones frontales (4).

Adicionalmente, la masticación produjo contaminación electromiográfica proveniente de la musculatura facial, generando distorsión de la señal cerebral y aumentando la amplitud general del registro (5).

---

## 4.4 Toma libre: música relajante vs. música estresante

Durante la exposición a música relajante, el espectro FFT mostró una actividad predominante en frecuencias muy bajas, principalmente entre 0 y 2.5 Hz, mientras que el resto del espectro presentó amplitudes considerablemente menores. Esto sugiere un estado de relajación general y una menor activación cortical (7).

En contraste, la condición de música estresante presentó picos de amplitud mayores respecto a la condición relajante, aunque manteniendo la predominancia en el rango entre 0 y 2.5 Hz. A partir de este punto, la señal mostró una atenuación progresiva hacia frecuencias superiores.

El incremento de amplitud observado podría relacionarse con una mayor activación emocional y cortical inducida por el estímulo auditivo, así como con posibles cambios fisiológicos involuntarios asociados al estrés (8).

---

## 4.5 Respuestas a las preguntas de la guía

### ¿Qué banda de frecuencia predomina al cerrar los ojos?

Al cerrar los ojos predomina la banda alfa (8–13 Hz), debido a la disminución de estímulos visuales y el aumento de sincronización neuronal cortical (1,2).

---

### ¿Qué filtro es imprescindible para EEG y por qué?

El filtro notch o rechaza-banda centrado en 50 o 60 Hz resulta indispensable para eliminar la interferencia de la red eléctrica, la cual puede alterar significativamente la señal EEG adquirida (9).

---

### ¿Puedes modular conscientemente tu señal EEG? Da un ejemplo.

Sí. La actividad EEG puede modificarse mediante cambios cognitivos o sensoriales. Un ejemplo es abrir y cerrar los ojos: al cerrarlos aumenta la actividad alfa y al abrirlos disminuye debido a la activación visual.

---

### ¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir?

Sí. Las diferencias pueden deberse tanto a causas fisiológicas como técnicas, incluyendo diferencias hemisféricas funcionales, variaciones en la impedancia de contacto o influencia desigual de movimientos oculares (2,4).

---

## 4.6 Limitaciones

El sistema BITalino utilizado presenta limitaciones relacionadas con su resolución de 10 bits y adquisición monocanal, lo cual restringe la resolución espacial en comparación con sistemas EEG clínicos multicanal (9).

Además, la ubicación frontal de los electrodos incrementa la susceptibilidad a artefactos oculares y musculares. La ausencia de un entorno electromagnéticamente aislado favoreció la presencia de interferencia de red eléctrica y ruido ambiental.

Finalmente, el estudio se realizó sobre un único participante y con registros de corta duración, por lo que los resultados obtenidos poseen un carácter demostrativo y no generalizable.

---

# Referencias

1. Niedermeyer E, Lopes da Silva FH. *Electroencephalography: Basic Principles, Clinical Applications, and Related Fields*. 6th ed. Philadelphia: Lippincott Williams & Wilkins; 2011.

2. Sanei S, Chambers JA. *EEG Signal Processing*. Chichester: Wiley; 2007.

3. Barry RJ, Clarke AR, Johnstone SJ, Magee CA, Rushby JA. EEG differences between eyes-closed and eyes-open resting conditions. *Clin Neurophysiol*. 2007;118(12):2765-73.

4. Urigüen JA, Garcia-Zapirain B. EEG artifact removal—state-of-the-art and guidelines. *J Neural Eng*. 2015;12(3):031001.

5. Muthukumaraswamy SM. High-frequency brain activity and muscle artifacts in MEG/EEG: a review and recommendations. *Front Hum Neurosci*. 2013;7:138.

6. Ferree TC, Luu P, Russell GS, Tucker DM. Scalp electrode impedance, infection risk, and EEG data quality. *Clin Neurophysiol*. 2001;112(3):536-44.

7. Davidson RJ. What does the prefrontal cortex “do” in affect: perspectives on frontal EEG asymmetry research. *Biol Psychol*. 2004;67(1-2):219-33.

8. Koelsch S. Towards a neural basis of music-evoked emotions. *Trends Cogn Sci*. 2010;14(3):131-7.

9. PLUX Biosignals. *BITalino (r)evolution Lab Guide: HomeGuide #5 - Electroencephalography (EEG)*. Lisboa: PLUX Wireless Biosignals SA; 2021.

10. Cohen MX. *Analyzing Neural Time Series Data: Theory and Practice*. Cambridge: MIT Press; 2014.
