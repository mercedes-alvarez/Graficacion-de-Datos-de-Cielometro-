#Se importan las librerías
import sys
import pandas as pd
import numpy as np
import pylab as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

#Se importa el documento a graficar
data = pd.read_csv("20230920.txt",sep= ",", engine='python',skiprows=4, names=["time","N","laser","retro"])

#Se toma el tiempo y se le da el formato de año,mes,día, hora,minutos y segundos
hora = data['time']
Tiempo = pd.to_datetime(hora,format="%Y-%m-%d %H:%M:%S") 

#Se toman los datos de retrodispersión
S = data[:]['retro']

#Se convierten los datos de hexadecimal a decimales
times = []
for each in S:
    levels = []
    N = 5
    for level in np.arange(0,10240,5):
        thisLevel = each[level:level+5]
        levels.append(int(thisLevel,base=16))
    times.append(levels)
    
times = np.array(times)

#Se realiza una correción 
for i in np.arange(0,240):
    for j in np.arange(0,2028):
        if times[i][j] > 524287:
            times[i][j] = times[i][j] - 1048576
        else:
            times[i][j] = times[i][j]

#Se transpone la matriz y se mutilica por el factor E-8
x = times.transpose()*1E-8

#Se crea la figura

fig, ax = plt.subplots(1,figsize=(10,5),dpi=100)

# Escala de color usada 'nipy_spectral'
plt.imshow(x, interpolation='bicubic', origin='lower', cmap='jet', vmin=0, vmax=0.004)
plt.colorbar(orientation = 'horizontal', shrink=0.6)

horas_deseadas = [
    Tiempo[0].time(),
    Tiempo[1436].time(),
    Tiempo[2876].time(),
    Tiempo[4316].time(),
    Tiempo[5755].time()
]

# Buscar los índices correspondientes de las horas deseadas en la lista Tiempo
posiciones = [i for i, tiempo in enumerate(Tiempo) if tiempo.time() in horas_deseadas]

# Establecer las posiciones de las marcas del eje x
ax.set_xticks(posiciones)

# Asignar las etiquetas deseadas a esas posiciones
etiquetas = [tiempo.time() for tiempo in Tiempo if tiempo.time() in horas_deseadas]
ax.set_xticklabels(etiquetas)
plt.xlabel('Hora')

#Se asignan etiqutas en el eje y
ax.set_yticklabels([0, 0, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000])
plt.ylabel('Altura (m)')

fig.show()

#Se guarda la figura
plt.savefig('20230915.png')