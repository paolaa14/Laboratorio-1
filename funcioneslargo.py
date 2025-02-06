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

# d. Crear el histograma largo

num_bins = 30
min_valores, max_valores = min(valores), max(valores)
bin_edges = np.linspace(min_valores, max_valores, num_bins + 1)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
histograma = np.zeros(num_bins)

# Contar frecuencia en cada bin
for val in valores:
    for i in range(num_bins):
        if bin_edges[i] <= val < bin_edges[i + 1]:
            histograma[i] += 1
            break

# Normalizar el histograma
bin_width = (max_valores - min_valores) / num_bins
total_samples = len(valores)
hist_normalizado = histograma / (total_samples * bin_width)

# Crear la figura y graficar ambas en la misma
plt.figure(figsize=(8, 6))

# Graficar el histograma
plt.bar(bin_centers, hist_normalizado, width=bin_width, alpha=0.6, color='blue', label='Histograma')

# Graficar la función de probabilidad
plt.plot(bin_centers, hist_normalizado, linestyle='-', color='black', linewidth=2, label='Función de probabilidad')

# Configuración del gráfico
plt.title("Histograma y función de probabilidad de la señal")
plt.xlabel("Voltios (mV)")
plt.ylabel("Frecuencia relativa")
plt.legend()
plt.grid(True)

# Mostrar la gráfica combinada
plt.show()