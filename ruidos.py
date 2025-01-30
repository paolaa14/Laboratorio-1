import wfdb
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo de señal
signal = wfdb.rdrecord("emg_healthy")
valores = signal.p_signal.flatten()

# a. Contaminar la señal con ruido gaussiano
mean_noise = 0
factor_ruido = 5  # Factor de escala para aumentar la cantidad de ruido
std_noise = np.std(valores) * factor_ruido

# Generar ruido gaussiano
ruido = np.random.normal(mean_noise, std_noise, len(valores))

# Agregar el ruido a la señal
valores_contaminados = valores + ruido

# b. Calcular la relación señal a ruido (SNR) para el ruido gaussiano
potencia_senal = np.mean(valores ** 2)
potencia_ruido = np.mean(ruido ** 2)
snr = 10 * np.log10(potencia_senal / potencia_ruido)

# Imprimir el SNR
print(f"Relación señal a ruido (SNR) con ruido gaussiano: {snr:.2f} dB")

# Graficar la señal original y la señal contaminada con ruido gaussiano
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(valores, color='b', label='Señal Original')
plt.title("Señal Original")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(valores_contaminados, color='r', label='Señal Contaminada con Ruido Gaussiano')
plt.title(f'Señal Contaminada con Ruido Gaussiano (factor {factor_ruido})')
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.legend()

plt.tight_layout()
plt.show()

# b. Contaminar la señal con ruido impulsivo
num_impulsos = int(0.01 * len(valores))  # Ajustar el número de impulsos
amplitud_impulso = np.max(np.abs(valores)) * 5  # Ajustar la amplitud del impulso

# Generar ruido impulsivo
ruido_impulsivo = np.zeros_like(valores)
indices_impulsivos = np.random.choice(len(valores), num_impulsos, replace=False)
ruido_impulsivo[indices_impulsivos] = amplitud_impulso * (2 * np.random.randint(0, 2, num_impulsos) - 1)  # +amplitud o -amplitud

# Agregar el ruido impulsivo a la señal
valores_contaminados_impulsivo = valores + ruido_impulsivo

# Calcular la relación señal a ruido (SNR) para el ruido impulsivo
potencia_ruido_impulsivo = np.mean(ruido_impulsivo ** 2)
snr_impulsivo = 10 * np.log10(potencia_senal / potencia_ruido_impulsivo)

# Imprimir el SNR
print(f"Relación señal a ruido (SNR) con ruido impulsivo: {snr_impulsivo:.2f} dB")

# Graficar la señal original y la señal contaminada con ruido impulsivo
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(valores, color='b', label='Señal Original')
plt.title("Señal Original")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(valores_contaminados_impulsivo, color='g', label='Señal Contaminada con Ruido Impulsivo')
plt.title(f'Señal Contaminada con Ruido Impulsivo (amplitud {amplitud_impulso})')
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.legend()

plt.tight_layout()
plt.show()

# c. Contaminar la señal con ruido tipo artefacto
# Parámetros del ruido tipo artefacto
frecuencia_artefacto = 0.1  # Frecuencia de los artefactos
amplitud_artefacto = np.max(np.abs(valores)) * 2  # Amplitud de los artefactos

# Generar ruido tipo artefacto (sinusoide de baja frecuencia)
tiempo = np.arange(len(valores))
ruido_artefacto = amplitud_artefacto * np.sin(2 * np.pi * frecuencia_artefacto * tiempo)

# Agregar el ruido tipo artefacto a la señal
valores_contaminados_artefacto = valores + ruido_artefacto

# Calcular la relación señal a ruido (SNR) para el ruido tipo artefacto
potencia_ruido_artefacto = np.mean(ruido_artefacto ** 2)
snr_artefacto = 10 * np.log10(potencia_senal / potencia_ruido_artefacto)

# Imprimir el SNR
print(f"Relación señal a ruido (SNR) con ruido tipo artefacto: {snr_artefacto:.2f} dB")

# Graficar la señal original y la señal contaminada con ruido tipo artefacto
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(valores, color='b', label='Señal Original')
plt.title("Señal Original")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(valores_contaminados_artefacto, color='m', label='Señal Contaminada con Ruido Tipo Artefacto')
plt.title(f'Señal Contaminada con Ruido Tipo Artefacto (amplitud {amplitud_artefacto})')
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.legend()

plt.tight_layout()
plt.show()