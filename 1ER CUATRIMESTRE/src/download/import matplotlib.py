import matplotlib.pyplot as plt

intervalos = ['50-59', '60-69', '70-79', '80-89', '90-99', '100-109', '110-119']
frecuencias = [8, 10, 16, 14, 10, 5, 2]
puntos_medios = [54.5, 64.5, 74.5, 84.5, 94.5, 104.5, 114.5]

plt.figure(figsize=(10, 6))
plt.bar(intervalos, frecuencias, width=1, edgecolor='black', alpha=0.7, label='Histograma')
plt.plot(puntos_medios, frecuencias, 'ro-', label='Polígono de frecuencias')
plt.xlabel('Diámetro (cm)')
plt.ylabel('Número de árboles')
plt.title('Distribución de diámetros de árboles')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()