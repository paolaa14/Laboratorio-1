import wfdb
import matplotlib.pyplot as plt

# Ruta de los archivos
hea_file = 'emg_healthy'
dat_file = 'emg_healthy'

# Leer el registro
record = wfdb.rdrecord(hea_file.replace('.hea', ''))

# Extraer la señal y el tiempo
signal = record.p_signal
time = [i / record.fs for i in range(len(signal))]  # Tiempo en segundos

# Graficar la señal de EMG
plt.figure(figsize=(10, 6))
plt.plot(time, signal)
plt.title('Señal de Electromiografía (EMG)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.grid()
plt.show()
