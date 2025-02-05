import wfdb
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo de señal
signal = wfdb.rdrecord("emg_healthy")
valores = signal.p_signal.flatten()

# a. Calcular la media de la señal
media = np.add.reduce(valores) / len(valores)

# b. Calcular la desviación estándar
suma_cuadrados = np.add.reduce((valores - media) ** 2)
desviacion_estandar = (suma_cuadrados / len(valores)) ** 0.5

# c. Calcular el coeficiente de variación
coeficiente_variacion = (desviacion_estandar / media) * 100

# Imprimir resultados
print(f"Media: {media}")
print(f"Desviación estándar: {desviacion_estandar}")
print(f"Coeficiente de variación: {coeficiente_variacion}%")

# d. Crear el histograma
plt.hist(valores, bins=30, density=True, alpha=0.6, color='g')
plt.title("Histograma de la señal")
plt.xlabel("Voltios(mV)")
plt.ylabel("Frecuencia relativa")
plt.show()

# e. Crear la función de probabilidad (aproximada con el histograma)
counts, bin_edges = np.histogram(valores, bins=30, density=True)
pdf = counts / np.add.reduce(counts)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

plt.plot(bin_centers, pdf, label='Función de probabilidad')
plt.title("Función de probabilidad de la señal")
plt.xlabel("Voltios(mV)")
plt.ylabel("Frecuencia relativa")
plt.legend()
plt.show()
