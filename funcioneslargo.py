import wfdb
import math
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo de señal
signal = wfdb.rdrecord("emg_healthy")
valores = signal.p_signal.flatten()

# a. Calcular la media de la señal manualmente
suma_informacion = 0
for valor_informacion in valores:  # Recorremos cada valor de los datos
    suma_informacion += valor_informacion  # Sumar cada valor a la suma total
num_informacion = len(valores)  # Obtenemos cuántos valores hay
media = suma_informacion / num_informacion
print(f"Media de la señal (Sin función): {media}")

# b. Calcular la desviación estándar manualmente
# 1. Calcular la suma de las diferencias al cuadrado
diferencia_al_cuadrado = 0
for valor_informacion in valores:  # Recorremos cada valor de los datos
    diferencia = valor_informacion - media  # Calculamos la diferencia entre el valor y la media
    diferencia_al_cuadrado += diferencia ** 2  # Sumamos el cuadrado de esa diferencia

# 2. Dividir por el número de valores (varianza)
varianza = diferencia_al_cuadrado / num_informacion

# 3. Calcular la raíz cuadrada de la varianza (desviación estándar)
desviacion_estandar = math.sqrt(varianza)
print(f"Desviación estándar de la señal (Sin función): {desviacion_estandar}")

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
plt.bar(bin_centers, hist_normalizado, width=bin_width, alpha=0.6, color='grey', label='Histograma')

# Graficar la función de probabilidad
plt.plot(bin_centers, hist_normalizado, linestyle='-', color='red', linewidth=2, label='Función de probabilidad')

# Configuración del gráfico
plt.title("Histograma y función de probabilidad de la señal")
plt.xlabel("Voltios (mV)")
plt.ylabel("Frecuencia relativa")
plt.legend()
plt.grid(True)

# Mostrar la gráfica combinada
plt.show()