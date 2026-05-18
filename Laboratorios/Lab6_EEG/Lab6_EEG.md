
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

<div align="center">
<img width="400" height="400" alt="bitalino_kit" src="https://github.com/user-attachments/assets/93c523c5-eeea-46d9-bde6-6dd9f19d75ca" />
</div>
<div align="center">  
Figura 1. Kit BITalino
</div><br>

### Laptop como módulo de procesamiento de datos

Se utilizó una laptop con Windows 11 y el software OpenSignals (r)evolution instalado para la adquisición, visualización y almacenamiento de las señales fisiológicas.

<div align="center">
<img width="650" height="150" alt="opensignals_logo_small-1024x241" src="https://github.com/user-attachments/assets/606cad60-55d1-401c-9253-378ab69e5927" />
</div>
<div align="center">  
Figura 2. Software OpenSignals
</div><br>

---

## 2.2 Sujetos de estudio

Participó voluntariamente un estudiante del curso *Introducción a Señales Biomédicas* de la Universidad Peruana Cayetano Heredia, sin antecedentes de enfermedades neurológicas ni otras afecciones clínicas.

---

## 2.3 Configuración de electrodos (EEG)

Se trabajó con una derivación reducida frontal referencial, conformada por tres electrodos:

- Frontal parietal 1 (Fp1) – Electrodo 1 (rojo)  
- Frontal parietal 2 (Fp2) – Electrodo 2 (negro)  
- Occipital 2 (O2) – Electrodo 3 (blanco), utilizado como tierra  

<div align="center">
<img width="390" height="388" alt="eeg1" src="https://github.com/user-attachments/assets/477d9520-8506-4d88-9ec8-542171bcca4b" />
</div>
<div align="center">  
Figura 3. Ubicación de los nodos en un EEG estándar. 
</div><br>


F = frontal, Fp = frontal parietal, Fz = frontal medio, T = temporal, C = central, Cz = central medio, O = occipital y P = parietal.

<div align="center">
<img width="349" height="266" alt="eeg2" src="https://github.com/user-attachments/assets/673b2d10-b31b-40e9-a79f-36dd52a2660f" />
</div>
<div align="center">  
Figura 4. Ejemplo de serie temporal correspondiente al EEG estándar de un paciente sano con los ojos abiertos.
</div><br>

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

- Documentos (Laboratorios/documentos/documentos_lab6.rar)
- Programa de ploteo (Jupyter Notebook) (Laboratorios/documentos/ploteo_laboratorio_6.ipynb)

---

# 3. Resultados

A continuación, se muestran los resultados obtenidos mediante procesamiento en Python. Las señales adquiridas fueron convertidas de ADC a microvoltios y posteriormente se eliminó la componente DC. Para la visualización se extrajeron segmentos de 10 segundos de cada registro.

---

## 3.1 EEG basal


https://github.com/user-attachments/assets/fe1bc717-b233-4f70-b79e-a32921b433b7


<div align="center">
<img width="602" height="232" alt="eeg3" src="https://github.com/user-attachments/assets/13fc6e34-ddf9-4d1f-bfd1-628476b478cb" />
</div>
<div align="center">  
Figura 5. EEG basal.
</div><br>

<div align="center">
<img width="602" height="273" alt="eeg4" src="https://github.com/user-attachments/assets/b0149136-c7f6-4631-9723-8bea6f38925c" />
</div>
<div align="center">  
Figura 6. FFT EEG basal.
</div><br>

## 3.2 EEG con ojos abiertos


https://github.com/user-attachments/assets/4b932008-85e7-4167-9c71-16bf6d2e4ee9


<div align="center">
<img width="602" height="232" alt="eeg5" src="https://github.com/user-attachments/assets/3e566354-bf55-4579-b2cc-11d996d10b61" />
</div>
<div align="center">  
Figura 7. EEG con ojos abiertos.
</div><br>

<div align="center">
<img width="602" height="271" alt="eeg6" src="https://github.com/user-attachments/assets/4c396fb5-0bb8-4463-9c85-adc1f0d3593f" />
</div>
<div align="center">  
Figura 8. FFT EEG con ojos abiertos.
</div><br>

## 3.3 EEG basal posterior a ojos abiertos

https://github.com/user-attachments/assets/6584e296-a505-4874-bf88-df4f4d8ffe25

<div align="center">
<img width="602" height="232" alt="eeg7" src="https://github.com/user-attachments/assets/587591bd-1b34-4eed-8182-f5b8200882e2" />
</div>
<div align="center">  
Figura 9. EEG basal posterior a ojos abiertos.
</div><br>

<div align="center">
<img width="602" height="273" alt="eeg8" src="https://github.com/user-attachments/assets/1e250ffc-3339-48af-96b3-5076b79dadea" />
</div>
<div align="center">  
Figura 10. FFT EEG basal posterior a ojos abiertos.
</div><br>

## 3.4 EEG con parpadeo y masticación constante

<div align="center">
<img width="602" height="235" alt="eeg9" src="https://github.com/user-attachments/assets/6b693c9f-3283-4648-b9de-32815eb6f304" />
</div>
<div align="center">  
Figura 11. EEG con parpadeo y masticación constante.
</div><br>

<div align="center">
<img width="602" height="271" alt="eeg10" src="https://github.com/user-attachments/assets/aea74639-6582-4181-8650-adb9338a7910" />
</div>
<div align="center">  
Figura 12. FFT EEG con parpadeo y masticación constante.
</div><br>

## 3.5 EEG basal posterior a parpadeo y masticación constante


https://github.com/user-attachments/assets/37d68a8d-ac2e-41cb-9c33-82eda981e3d1


<div align="center">
<img width="602" height="235" alt="eeg11" src="https://github.com/user-attachments/assets/eb10963c-6b69-4e70-b029-c8c1fca8715e" />
</div>
<div align="center">  
Figura 13. EEG basal posterior a parpadeo y masticación constante.
</div><br>

<div align="center">
<img width="602" height="271" alt="eeg12" src="https://github.com/user-attachments/assets/055c7499-62a4-4488-9e4b-60b510fa6ad2" />
</div>
<div align="center">  
Figura 14. FFT EEG basal posterior a parpadeo y masticación constante.
</div><br>

## 3.6 Toma libre

https://github.com/user-attachments/assets/673c1133-4ec7-42dc-95b1-f488992f9a86


### Música relajante

<div align="center">
<img width="602" height="233" alt="eeg13" src="https://github.com/user-attachments/assets/b618639b-a2c6-4646-84ca-56af8ed4a81e" />
</div>
<div align="center">  
Figura 15. EEG toma libre (Música relajante).
</div><br>

<div align="center">
<img width="602" height="271" alt="eeg14" src="https://github.com/user-attachments/assets/6ff61b5f-3414-40f0-bb0c-557a5bc35999" />
</div>
<div align="center">  
Figura 16. FFT EEG toma libre (Música relajante).
</div><br>

### Música estresante

<div align="center">
<img width="602" height="232" alt="eeg15" src="https://github.com/user-attachments/assets/59297d5c-3c91-4e65-81f9-87a0f319fd8c" />
</div>
<div align="center">  
Figura 17. EEG toma libre (Música estresante).
</div><br>

<div align="center">
<img width="602" height="271" alt="eeg16" src="https://github.com/user-attachments/assets/cc02b4d4-80a9-496f-ba2d-740266dff05d" />
</div>
<div align="center">  
Figura 18. FFT EEG toma libre (Música estresante).
</div><br>

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

El análisis espectral mostró un incremento muy marcado de actividad en la región de bajas frecuencias, principalmente entre 0 y 5 Hz. Esta elevada actividad se relaciona directamente con los potenciales generados por el parpadeo, ya que los movimientos oculares producen señales de gran amplitud que afectan especialmente a los electrodos ubicados en regiones frontales (4).

Adicionalmente, la masticación produjo contaminación electromiográfica proveniente de la musculatura facial, generando distorsión de la señal cerebral y aumentando la amplitud general del registro (5).

---

## 4.4 Toma libre: música relajante vs. música estresante

Durante la exposición a música relajante, el espectro FFT mostró una actividad predominante en frecuencias muy bajas, principalmente entre 0 y 2.5 Hz, mientras que el resto del espectro presentó amplitudes considerablemente menores. Esto sugiere un estado de relajación general y una menor activación cortical, compatible con una disminución de la carga cognitiva y una mayor estabilidad fisiológica del participante (7).

En contraste, la condición de música estresante presentó picos de amplitud mayores respecto a la condición relajante, aunque manteniendo la predominancia en el rango entre 0 y 2.5 Hz. A partir de este punto, la señal mostró una atenuación progresiva hacia frecuencias superiores. El incremento de amplitud observado podría relacionarse con una mayor activación emocional y cortical inducida por el estímulo auditivo, así como con posibles cambios fisiológicos involuntarios asociados al estrés, como tensión muscular o variaciones respiratorias (8).
Si bien ambas condiciones mostraron predominancia en bajas frecuencias, la música estresante generó señales de mayor amplitud y variabilidad, lo cual coincide cualitativamente con estudios relacionados con respuestas emocionales y modulación cortical inducida por estímulos auditivos.


---

## 4.5 Respuestas a las preguntas de la guía

### ¿Qué banda de frecuencia predomina al cerrar los ojos?

Al cerrar los ojos predomina la banda alfa (8–13 Hz), fenómeno descrito originalmente por Berger y ampliamente documentado en la literatura neurofisiológica. La ausencia de estímulos visuales favorece la sincronización neuronal en regiones posteriores y frontales, generando un incremento de la potencia alfa observable en el EEG (1,2). En los registros basales obtenidos durante el laboratorio, el análisis FFT mostró una mayor concentración de energía en frecuencias compatibles con dicha banda.

---

### ¿Qué filtro es imprescindible para EEG y por qué?

Uno de los filtros más importantes en el procesamiento EEG es el filtro notch o rechaza-banda centrado en 50 o 60 Hz, dependiendo de la frecuencia de la red eléctrica local. Este filtro permite reducir significativamente la interferencia electromagnética proveniente del suministro eléctrico, la cual puede superar ampliamente la amplitud de la señal EEG y afectar la interpretación de los resultados (9). De manera complementaria, el uso de filtros pasa-alto y pasa-bajo permite eliminar deriva de línea base, componente DC y ruido de alta frecuencia asociado a actividad muscular y artefactos.

---

### ¿Puedes modular conscientemente tu señal EEG? Da un ejemplo.

Sí. La actividad EEG puede modularse conscientemente mediante cambios en el estado cognitivo o sensorial. Un ejemplo simple es abrir y cerrar los ojos: al cerrarlos aumenta la actividad alfa, mientras que al abrirlos esta disminuye debido a la activación visual. Del mismo modo, actividades que requieren atención o cálculo mental pueden incrementar la actividad beta frontal. Este principio es utilizado en técnicas de neurofeedback, donde el sujeto aprende a modificar determinados patrones cerebrales mediante retroalimentación en tiempo real (7).

---

### ¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir?

Pueden existir diferencias entre Fp1 y Fp2 tanto por causas fisiológicas como técnicas. Desde el punto de vista fisiológico, ambos hemisferios cerebrales presentan especializaciones funcionales distintas relacionadas con procesamiento emocional, cognitivo y lingüístico (2). Técnicamente, diferencias en impedancia de contacto, colocación de electrodos, adherencia o influencia desigual de movimientos oculares pueden generar variaciones entre ambos registros (4). En el presente laboratorio, la adquisición mediante un único canal limitó la comparación simultánea entre ambas posiciones.

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

