import wfdb
import matplotlib.pyplot as plt
import numpy as np

def calcular_snr(signal_original, signal_ruidosa):
    potencia_signal = np.mean(signal_original ** 2)
    potencia_ruido = np.mean((signal_ruidosa - signal_original) ** 2)
    snr = 10 * np.log10(potencia_signal / potencia_ruido)
    return snr

# Leer el archivo de señal
signal = wfdb.rdrecord("emg_healthy")
valores = signal.p_signal.flatten()

# Definir factores de ruido
factor_ruido_alto = 5
factor_ruido_bajo = 2

# a. Contaminar la señal con ruido gaussiano (alta y baja amplitud)
mean_noise = 0
std_noise_alto = np.std(valores) * factor_ruido_alto
std_noise_bajo = np.std(valores) * factor_ruido_bajo

ruido_alto = np.random.normal(mean_noise, std_noise_alto, len(valores))
ruido_bajo = np.random.normal(mean_noise, std_noise_bajo, len(valores))

valores_contaminados_alto = valores + ruido_alto
valores_contaminados_bajo = valores + ruido_bajo

# b. Contaminar la señal con ruido impulsivo (alta y baja amplitud)
num_impulsos = int(0.01 * len(valores))
amplitud_impulso_alto = np.max(np.abs(valores)) * 5
amplitud_impulso_bajo = np.max(np.abs(valores)) * 2

ruido_impulsivo_alto = np.zeros_like(valores)
ruido_impulsivo_bajo = np.zeros_like(valores)

indices_impulsivos = np.random.choice(len(valores), num_impulsos, replace=False)
ruido_impulsivo_alto[indices_impulsivos] = amplitud_impulso_alto * (2 * np.random.randint(0, 2, num_impulsos) - 1)
ruido_impulsivo_bajo[indices_impulsivos] = amplitud_impulso_bajo * (2 * np.random.randint(0, 2, num_impulsos) - 1)

valores_contaminados_impulsivo_alto = valores + ruido_impulsivo_alto
valores_contaminados_impulsivo_bajo = valores + ruido_impulsivo_bajo

# c. Contaminar la señal con ruido tipo artefacto (alta y baja amplitud)
frecuencia_artefacto = 0.1
amplitud_artefacto_alto = np.max(np.abs(valores)) * 2
amplitud_artefacto_bajo = np.max(np.abs(valores)) * 0.8

ruido_artefacto_alto = amplitud_artefacto_alto * np.sin(2 * np.pi * frecuencia_artefacto * np.arange(len(valores)))
ruido_artefacto_bajo = amplitud_artefacto_bajo * np.sin(2 * np.pi * frecuencia_artefacto * np.arange(len(valores)))

valores_contaminados_artefacto_alto = valores + ruido_artefacto_alto
valores_contaminados_artefacto_bajo = valores + ruido_artefacto_bajo

# Lista con los ruidos y sus nombres
tipos_ruido = [
    ("Ruido Gaussiano Alto", valores_contaminados_alto, 'r'),
    ("Ruido Gaussiano Bajo", valores_contaminados_bajo, 'c'),
    ("Ruido Impulsivo Alto", valores_contaminados_impulsivo_alto, 'g'),
    ("Ruido Impulsivo Bajo", valores_contaminados_impulsivo_bajo, 'y'),
    ("Ruido Artefacto Alto", valores_contaminados_artefacto_alto, 'm'),
    ("Ruido Artefacto Bajo", valores_contaminados_artefacto_bajo, 'k')
]

# Generar una figura para cada tipo de ruido y calcular SNR
for titulo, valores_contaminados, color in tipos_ruido:
    snr = calcular_snr(valores, valores_contaminados)
    print(f"{titulo}: SNR = {snr:.2f} dB")
    
    plt.figure(figsize=(10, 6))

    # Señal original
    plt.subplot(2, 1, 1)
    plt.plot(valores, color='b', label='Señal Original')
    plt.title(f"Señal Original - {titulo}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Voltaje (mV)")
    plt.legend()

    # Señal con ruido
    plt.subplot(2, 1, 2)
    plt.plot(valores_contaminados, color=color, label=titulo)
    plt.title(f"{titulo} (SNR: {snr:.2f} dB)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Voltaje (mV)")
    plt.legend()

    plt.tight_layout()
    plt.show()
