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
plt.hist(valores, bins=30, density=True, alpha=0.6, color='g')
plt.title("Histograma normalizado de la señal")
plt.xlabel("Valor de la señal")
plt.ylabel("Densidad")
plt.show()

# e. Crear la curva de densidad de probabilidad ajustada (Distribución normal ajustada)
mu, std = norm.fit(valores)
xmin, xmax = min(valores), max(valores)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.hist(valores, bins=30, density=True, alpha=0.6, color='g', label='Histograma normalizado')
plt.plot(x, p, 'k', linewidth=2, label='Curva de densidad ajustada')
plt.title("Curva de densidad de probabilidad ajustada")
plt.xlabel("Valor de la señal")
plt.ylabel("Densidad")
plt.legend()
plt.show()