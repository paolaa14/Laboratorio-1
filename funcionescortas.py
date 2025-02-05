import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Leer el archivo de señal
signal = wfdb.rdrecord("emg_healthy")
valores = signal.p_signal.flatten()

# a. Calcular la media de la señal
media = np.mean(valores)

# b. Calcular la desviación estándar
desviacion_estandar = np.std(valores)

# c. Calcular el coeficiente de variación
coeficiente_variacion = (desviacion_estandar / media) * 100

# Imprimir resultados
print(f"Media: {media}")
print(f"Desviación estándar: {desviacion_estandar}")
print(f"Coeficiente de variación: {coeficiente_variacion}%")

# d. Crear el histograma normalizado
hist, bins = np.histogram(valores, bins=30, density=True)
bin_centers = (bins[:-1] + bins[1:]) / 2

plt.hist(valores, bins=30, density=True, alpha=0.6, color='g')
plt.title("Histograma normalizado de la señal")
plt.xlabel("Voltios(mV)")
plt.ylabel("Frecuencia relativa")
plt.show()

# e. Crear la función de probabilidad de la señal
plt.plot(bin_centers, hist, linestyle='-', color='b', label='Función de probabilidad')
plt.title("Función de probabilidad de la señal")
plt.xlabel("Voltios(mV)")
plt.ylabel("Frecuencia relativa")
plt.legend()
plt.show()
