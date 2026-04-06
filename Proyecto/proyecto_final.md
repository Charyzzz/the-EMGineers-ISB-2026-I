# Proyecto Final

## Introducción
El transporte de cargas en estudiantes, especialmente mediante mochilas y bolsos, genera cambios biomecánicos que pueden afectar tanto la postura como el equilibrio corporal. En particular cuando la carga se distribuye de manera asimétrica el cuerpo tiende a realizar compensaciones como la inclinación del tronco o la elevación de un hombro con el objetivo de mantener estable el centro de masa [1].
Además, estudios electromiográficos han mostrado que el tipo de carga influye directamente en la activación muscular. Músculos como el trapecio y los erectores espinales cumplen un rol clave en la estabilización postural y su actividad varía dependiendo de cómo se transporta el peso [1].


## Problemática a abordar
Aunque existen estudios que analizan el  efecto del tipo de bolso en la activación muscular, la mayoría se realizan en condiciones controladas en laboratorios y no en contextos más realistas como el transporte público. Se ha demostrado que el uso de bolsos de un solo hombro incrementa significativamente la actividad muscular del trapecio y los erectores espinales en comparación con las mochilas de doble asa [2]. Este tipo de carga induce asimetrías musculares que derivan a desequilibrios posturales, incluso cuando el peso se mantiene constante. Se ha observado que la actividad muscular varía en función del tipo de carga utilizada, esto evidencia la influencia de la distribución  del peso en la respuesta biomecánica del cuerpo. Aunque aún es limitada la evidencia que analice estas diferencias en condiciones dinámicas reales  y mediante técnicas de  procesamiento de señales que permitan una caracterización cuantitativa adecuada.


## Propuesta de solución
Como propuesta tentativa de solución, se plantea el uso de un electromiógrafo portátil con electrodos de superficie colocados en los músculos trapecio superior (derecho e izquierdo, en punto motor) y erector espinal en L3 (bilateral), ya que estos músculos son comúnmente monitoreados en estudios de activación espinal y asimetrías posturales [3].

El registro de datos se realiza durante trayectos reales en transporte público. Cada participante se monitorea dos veces al día para capturar variabilidad diaria .

<u>Variables Esperadas</u>
El Índice de Asimetría Muscular (IAM) se calcula como:

$$
IAM = \frac{\left| RMS_{derecho} - RMS_{izquierdo} \right|}{\frac{RMS_{derecho} + RMS_{izquierdo}}{2}} \times 100\%
$$

Un IAM >10-15% indica descompensación clínicamente relevante en literatura de simetría espinal; en grupos con carga asimétrica (como bolso), confirmaría la hipótesis [4].


RMS normalizado se expresa como el porcentaje de la contracción voluntaria máxima (CVM), medida en posición estática antes del trayecto.


Respecto al procesamiento de la señal adquirida, se tienen las siguientes etapas:

### 1. Adquisición
Se utiliza EMG superficial (sEMG) para el monitoreo de activación muscular. Para el caso del contexto planteado, se necesitan 4 canales: trapecio superior derecho, trapecio superior izquierdo, y opcionalmente erectores espinales bilaterales. Un número bajo de canales es suficiente para monitoreo muscular simple de manera eficiente [5].
![img_adquisicion](https://github.com/user-attachments/assets/67b5c867-d91f-4143-be6f-763d94df5a61)



### 2. Amplificación


La señal EMG de por sí es muy débil (0–10 mV). Una ganancia de 500- 1000 es óptima para una correcta amplificación. El amplificador debe tener alta razón de rechazo de modo común (CMRR) y alta impedancia de entrada (Zi) para minimizar el ruido, en especial en el contexto planteado, uno que no es tan controlado como lo es un laboratorio [5].


### 3. Filtrado

Filtro pasa-bandas: la mayoría de los estudios de monitoreo muscular usan entre 10–500 Hz, que es donde se concentra la energía útil de la señal sEMG. Usar 20 Hz como frecuencia de corte inferior es el mejor compromiso para eliminar artefactos de movimiento sin perder información útil, información importante en este caso porque los participantes estarán en movimiento dentro del transporte público.

Filtro notch: a 60 Hz (en Perú 60 Hz) para eliminar la interferencia de la línea eléctrica, que en transporte público podría ser considerable.

Orden del filtro: Butterworth de 2do o 4to orden (los más usados) [5]. 

### 4. Conversión analógica-digital 

La frecuencia de muestreo más documentada es 1000 Hz, consistente con el teorema de Nyquist para señales sEMG que tienen su mayor energía hasta ~500 Hz. Para la resolución del ADC, con 8–12 bits se trabaja sin problemas [5].

### 5. Cálculo del RMS

Una vez digitalizada la señal, se realiza el proceso de obtención del IAM:
Aplicar ventana deslizante de 250 ms sobre la señal filtrada y rectificada
Calcular el RMS por ventana en cada canal
Promediar el RMS a lo largo de todo el trayecto para obtener un valor representativo por músculo y por sesión

Por último, usando los valores obtenidos de RMS, se calcula el IAM.

## Plan de actividades

![image alt](https://github.com/Charyzzz/the-EMGineers-ISB-2026-I/blob/cdf885507e0dc13867e976d33f91f6b04b2f2020/Proyecto/Se%C3%B1ales%20plan%20de%20trabajo

### Fase 1: Preparación y marco ético

Revisión del protocolo: Afinar criterios de inclusión (sin lesiones musculoesqueléticas, uso habitual de mochila/bolso).
Consentimiento informado: Redactar y hacer firmar a cada compañero participante. Explicar procedimiento, riesgos mínimos y confidencialidad.
Configuración del equipo: Verificar EMG (4 canales), electrodos, amplificador, ganancia (500-1000), filtros (20-500 Hz + notch 60 Hz).
Prueba piloto: Ajustar colocación de electrodos (trapecios superiores + erectores espinales bilaterales).

### Fase 2: Recolección de datos

Registro de CVM: Medir contracción voluntaria máxima (CVM) en estática para normalizar RMS (%CVM).
Recolección en campo: Cada participante es monitoreado 2 veces al día (mañana y tarde) en transporte público real.
Toma de notas: Registrar el tipo de carga (mochila/bolso), lado de carga, duración del trayecto, condiciones (lleno, parado, sentado).
Almacenar: Guardar señales crudas y etiquetar por participante, sesión, lado de carga.


### Fase 3: Procesamiento de señales / información

Filtrado: Aplicar filtro pasa-bandas (20-500 Hz) + notch (60 Hz) + rectificación completa.
Ventana RMS: 	Usar ventana de 250 ms, paso 125 ms. Calcular RMS por canal.
Promediado: Obtener un valor RMS promedio por músculo y por trayecto.
Normalización: Dividir cada RMS entre la CVM del mismo músculo (%CVM).


### Fase 4: Cálculo de IAM y análisis

Cálculo de IAM: Aplicar la fórmula anteriormente planteada
Clasificación: Identificar casos con IAM >10-15% (asimetría clínicamente relevante).
Comparación de cargas: Separar grupos, mochila vs. bolso; lado ipsilateral vs. contralateral.
Estadísticas: Boxplots del IAM, prueba t pareada u otra, según normalidad.


### Fase 5: Interpretación y reporte

Discusión:  Relacionar hallazgos con la literatura, usando referencias.
Limitaciones: Señalar las limitaciones del estudio como tamaño de muestra reducido, variabilidad diaria, ruido ambiental en transporte.
Conclusiones: ¿El transporte asimétrico genera IAM elevado en estudiantes? ¿En qué músculos más?
Preparación de entrega:  Realizar el póster e informe para la entrega final del curso. 


## Referencias
[1] M. H. Kim, J. H. Kim, and J. S. Shim, "The changes of electromyography in the upper trapezius and supraspinatus of women college students according to the method of bag-carrying and weight," J. Phys. Ther. Sci., vol. 25, no. 9, pp. 1129–1131, Oct. 2013. doi: 10.1589/jpts.25.1129. https://pmc.ncbi.nlm.nih.gov/articles/PMC3818749/

[2] S. H. Kim and J. H. Oh, "Correlations between muscle activities and strap length and types of school bag during walking," J. Phys. Ther. Sci., vol. 26, no. 12, pp. 1937–1939, Dec. 2014. doi: 10.1589/jpts.26.1937. https://pmc.ncbi.nlm.nih.gov/articles/PMC4273062/

[3] L. Y. Guo et al., "Comparison of the electromyographic activation level and unilateral selectivity of erector spinae during different selected movements," Int. J. Rehabil. Res., vol. 35, no. 4, pp. 345–351, Dec. 2012. doi: 10.1097/MRR.0b013e32835641c0. https://pubmed.ncbi.nlm.nih.gov/22785046/

[4] D. Rojas-Valverde, A. Sánchez García, D. Sáez Ulloa, and R. Gutiérrez-Vargas, "Does osteopathic manipulation lead to improvements in physical and muscle mechanical function and spinal symmetries in golfers?," Kronos, vol. 18, no. 1–2, Jan. 2019. doi: 10.64197/Kronos.18.01-02.863. https://erevistas.universidadeuropea.com/index.php/kronos/article/view/863

[5] L. A. G. Rodriguez, J. M. A. P. Gutierrez, and F. J. L. Hernandez, "Myoelectric interfaces and related applications: Current state of EMG signal processing – A systematic review," IEEE Access, vol. 8, pp. 7792–7805, Jan. 2020. doi: 10.1109/ACCESS.2020.2964222. https://ieeexplore.ieee.org/abstract/document/8949764
