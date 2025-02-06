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
plt.figure(figsize=(8, 6))
counts, bin_edges, _ = plt.hist(valores, bins=30, density=True, alpha=0.6, color='grey', label="Histograma")

# e. Calcular la función de probabilidad
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Normalizar la función de probabilidad con el ancho de los bins para que se ajuste mejor
bin_width = bin_edges[1] - bin_edges[0]
pdf = counts / (np.sum(counts) * bin_width)

# Graficar la función de probabilidad sobre el histograma
plt.plot(bin_centers, pdf, 'r-', linewidth=2, label="Función de probabilidad")

# Configuración del gráfico
plt.title("Histograma y función de probabilidad de la señal")
plt.xlabel("Voltios (mV)")
plt.ylabel("Frecuencia relativa")
plt.legend()
plt.grid(True)
plt.show()
