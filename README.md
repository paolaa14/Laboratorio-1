Los códigos creados permiten observar la señal obtenida del sofware PHYSIONET, la cual es electromiografía (EMG) con electrodos aguja (son electrodos más específicos), donde se evidencia la señal captada del músculo tibial anterior (pierna- detrás de la tibia) . Es importante señalar que la EMG es una técnica que mostrará la condición en la que se encuentran los músculos ( en este caso el tibial anterior) y los nervios que los controlan, estos nervios envían señales eléctricas  por medio de neuronas para poder visualizar el movimiento del músculo.

1. En primer lugar, se realizó la descarga de la señal del software physionet. En github se evidencian los dos archivos del mismo: .dat y .hea.
2. ⁠En segundo lugar, se hizo la gráfica de dicha señal en spyder, este sería el archivo que tiene como nombre:  labo1 , donde se verá la señal emg del músculo mencionado.
<img width="617" alt="Figure 2025-02-04 195526 (0)" src="https://github.com/user-attachments/assets/a93a9324-af44-4cf0-b5a7-09eb5c7e0382" />


Es importante recordar estos conceptos antes de continuar: 

- Media:  es una herramienta de estadística esencial, ya que esta indica el promedio que se obtiene al dividir la suma del total de los datos que se tengan entre el total de los mismos, de manera similar, esta proporciona un punto de equilibrio en la distribución de llos diferentes datos.
 
• Desviación estándar ; esta permite medir la dispersión en el conjunto de datos que se este estudiando, y a su vez, se utiliza simultáneamente con la media para determinar los distintos intervalos estadísticos.

• Coeficiente variación; este posee una característica esencial y es comparar la desviación estándar en los datos que se evidencien, es decir es una herramienta para evaluar la precisión del sistema de medición, este se obtiene; desviación estándar/media.

• Función de probabilidad; consiste en una función matemática, que indica la probabilidad que una variable aleatoria discreta tome cierto valor.

• Curva de densidad: Es una línea que suaviza  la información del histograma, creando una representación continua de la distribución de los datos, permitiendo comprender si esta sesgado o simetrico.

• Histograma: Este tipo de grafico, consiste en la representación de una variable cuantitativa por medio de barras, agrupando los datos, donde en el eje x se representan los intervalos de los datos y en el eje y evidencia la frecuencia de los datos en cierto intervalo.

3. En tercer lugar, se importaron las bibliotecas, como la ¨numpy¨ para relizar operaciones matematicas, o la ¨matplotlib.pyplot¨ para poder realizar los graficos que en este caso son histogramas, para continuar se implemento una parte en el código para leer la señal del documento tomado de physionet, que en el codigo es ¨wfdb.rdrecord("emg_healthy")¨, que va a leer basicamente el archuivo de emg del physionet y lo guarda en una variable que le pusimos signal, después se calculó la media de la señal con ¨(np.add.reduce(valores))¨, la cual suma todos los valores y para dividirlo en el valor total de la señal es ¨(len(valores))¨, posterior a esto se huzo algo similar para la desviación estándar pero  restando los valores de la señal con la media y elevandolos al cuadrado para luego sumarlos, todo esto usando ¨((valores - media) ** 2)¨, y al dividirlo con el total se hace lo mismo que con la media pero tomando la raiz cuadrada de ese resultado, ahora para el coficiente de variación, se obtiene diviendo la desviación estándar por la media y multiplicnado por 100 para mostrarlo en términos de porcentaje, lo cual se refleja en el codigo,  y para la función de probabilidad para tener un menor análisis de esta, llamamos el archivo de funcioneslargas y codificamos los cálculos, la para luego en la consola de spyder observar lo mencionado previamente. Posterior, creamos un histograma , recalcando que en el eje “y” se encuentra la frecuencia relativa (repeticiones cada valor) , y en el eje “x” los valores de la amplitud (que tan alto llega cada barra) en voltaJe (mV) .Para continuar, después de crear el histograma hicimos la curva de densidad en forma de gráfico que nos enseña el centro, la extensión y la forma de los datos de esta señal. Todo esto lo evidenciamos en el archivo llamado funcioneslargas.

Se obtuvo esto: 

<img width="488" alt="Figure 2025-02-05 191250 (1)" src="https://github.com/user-attachments/assets/4a5223b2-a2c0-4d4b-a261-cc185445c142" />

Tenemos una distribución Centrada en Cero
El pico del histograma está alrededor de 0 mV, lo cual es esperado porque la señal EMG alterna rápidamente entre valores positivos y negativos, con un promedio cercano a cero.

La forma de la distribución es simétrica y tiene un pico en cero, lo que indica que la mayoría de los valores de la señal están cerca de este valor.


<img width="569" alt="Captura de pantalla 2025-02-04 a la(s) 7 58 58 p m" src="https://github.com/user-attachments/assets/301cef2d-ca7b-4981-8af3-04f6fe8d5ab0" />

Media: ~0.0002 mV
Esto indica que la señal está centrada cerca de cero, lo cual es típico en señales EMG crudas. Esto se debe a que la actividad muscular genera potenciales positivos y negativos que, al promediarse, tienden a equilibrarse cerca de cero.
Desviación Estándar: ~0.0816 mV
Refleja la variabilidad de la señal. En señales EMG, una desviación estándar baja sugiere que la mayoría de los valores están cerca de la media, lo cual es esperado en reposo o con baja actividad muscular.
Coeficiente de Variación: ~40822%
Este valor es extremadamente alto debido a que la media es muy cercana a cero, lo que provoca que el cociente entre la desviación estándar y la media sea muy grande. En EMG, este coeficiente puede no ser tan representativo debido a la naturaleza oscilante de la señal.



4. En cuarto lugar, se realizó el mismo procedimiento del ítem 3, pero esta vez con el método de las funciones de Python y esto lo podemos visualizar en el archivo ; funcionescortas.

<img width="376" alt="Figure 2025-02-04 200725 (3)" src="https://github.com/user-attachments/assets/6c440bfe-6257-431a-9a58-dac28a5ad736" />

<img width="376" alt="Figure 2025-02-04 204024 (1)" src="https://github.com/user-attachments/assets/485350e0-5026-4c3d-bba8-b79e90a86ef5" />

<img width="583" alt="Captura de pantalla 2025-02-04 a la(s) 8 40 30 p m" src="https://github.com/user-attachments/assets/f2b0b6b4-fc0d-4d93-ab42-2fb51c8609b6" />

Se visualizan los mismos datos que en funciónes largas

   
6. ⁠Para finalizar, queríamos contaminar la señal con diferentes tipos de ruidos, esto se hizo llamando nuevamente el archivo labo1, generando el ruido y agregándolo a la señal normal, luego analizamos el SNR que es la señal a ruido (es el ruido que afecta la calidad de la señal y se define como la proporción existente de la amplitud de la señal que se trasmite y la amplitud del ruido que la corrompe, se expresa en decibeles) , para así medir la calidad de nuestra señal.

Recordemos que hay distintos tipos de ruidos, los que analizaremos en nuestra señal son:
- RUIDO GAUSSIANO: se suma a la señal presentando un espectro plano y la distribución de sus valores sigue una distribución gaussiana (de ahí el nombre), quien posee un rango ideal o normal de -20 dB a +30dB. 

• RUIDO IMPULSIVO: tiene picos con una amplitud alta, y usualmente la duración no es tan extensa, aun así afecta la calidad de la señal, quien posee un rango normal de +40 dB a +50 dB.

• ⁠RUIDO TIPO ARTEFACTO: este tipo de ruido, usualmente surge cuando se realiza algo a la señal, es decir, cuando se realiza por ejemplo  un proceso de filtración quien posee un rango normal de + 5 dB a +30dB.

 Estos ruidos los agregamos en dos tipos de condiciones, con amplitudes altas y luego con amplitudes bajas con el objetivo de mirar cómo se comporta la señal (si está gravemente contaminada o si la señal es más fuerte que el ruido), los valores que nos dieron fueron:

<img width="713" alt="Figure 2025-02-04 204634 (0)" src="https://github.com/user-attachments/assets/bcfcc021-620a-4531-80fc-38d14a405034" />

<img width="713" alt="Figure 2025-02-04 204634 (1)" src="https://github.com/user-attachments/assets/d9232891-03d3-4102-b63c-a1998a7e0c92" />

1. SNR con ruido gaussiano alto: -13.99 dB
1.1. SNR con ruido gaussiano bajo: -5.99 dB

<img width="713" alt="Figure 2025-02-04 204634 (2)" src="https://github.com/user-attachments/assets/3e27569a-2d15-4c50-bfd0-7ba361616e05" />

<img width="713" alt="Figure 2025-02-04 204634 (3)" src="https://github.com/user-attachments/assets/5ceb72f6-1012-4005-af82-4d6833fb9b28" />


3. SNR con ruido impulsivo alto: -16.68 dB
2.1. SNR con ruido impulsivo bajo: -8.72 dB

<img width="713" alt="Figure 2025-02-04 204634 (4)" src="https://github.com/user-attachments/assets/3fc42bca-f16e-4bd6-af0e-1acae6a225bc" />

<img width="713" alt="Figure 2025-02-04 204634 (5)" src="https://github.com/user-attachments/assets/eb4c38a9-58e7-4a6c-96ae-04168853257a" />

5. SNR con ruido artefacto alto: -25.71 dB
3.1. SNR con ruido artefacto bajo: -17.75 dB

Los cuales se evidencian en el archivo llamado ruidos, para continuar, vamos analizar y explicar cómo interpretar los resultados anteriormente expuestos, para el ítem 1.  en el ruido gaussiano, al implementar amplitudes altas evidencia un valor negativo, lo cual indica que el ruido domina y la señal se encuentra altamente distorsionada, mientras que en el caso de amplitudes bajas, a pesar se poseer un valor negativo se puede observar mucho mejor la señal, ya que esta predomina más que el ruido, aún así sigue contaminada. Para el ítem 2. En el ruido impulsivo, en el caso de las amplitudes altas  y bajas se evidencia un valor negativo, lo que indica que los picos de ruido están sobre saturando la señal ( es más fuerte el ruido que la señal), lo que indica en términos generales que se pierde bastante información, por lo que este tipo de ruido está afectando gravemente la señal, no obstante en comparación se encuentra menos contaminada la de bajas amplitudes.Para el ítem 3, en el ruido artefacto los valores son semejantes en cuanto a que ambos son negativos, esto quiere decir que  las distorsiones o la contaminación es mucho más alta que la señal en sí, no quiere decir que esté mal, solo indica que la señal se encuentra altamente contaminada, sin embargo, esta un poco mejor la de amplitudes bajas, a pesar de estar igualmente contaminada, se acerca al rango anteriormente mencionado.  

Todos estos ruidos y distintas amplitudes  se llevaron a cabo con la intención de analizar la simulación en condiciones reales debido a que ayudan a simular las interferencias de dichas condiciones, ayuda a analizar la capacidad de precisión de la señal y su sensibilidad con relación a las perturbaciones. Esto lo podemos visualizar en el archivo llamado ruidos.
