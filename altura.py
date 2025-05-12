#Se importan las librerías necesarias
import sys
import pandas as pd
import numpy as np
import pylab as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import datetime as dt

#Se abre el archivo de los datos
data = pd.read_csv("/content/opticos_Cielometro.dat", sep= ",", engine='python',skiprows=4, names=["datetime","N","Z1","Z2","Z3","Z4","C1","C2","C3","C4","C5","H1","H2","H3","H4","H5","V1","V2"])

#Se vuelven los NAN en nan numéricos.
data['Z1'] = np.array(data['Z1'].replace(["NAN"], np.nan))
data['Z2'] = np.array(data['Z2'].replace(["NAN"], np.nan))
data['Z3'] = np.array(data['Z3'].replace(["NAN"], np.nan))
data['Z4'] = np.array(data['Z4'].replace(["NAN"], np.nan))

data['C1'] = np.array(data['C1'].replace(["NAN"], np.nan))
data['C2'] = np.array(data['C2'].replace(["NAN"], np.nan))
data['C3'] = np.array(data['C3'].replace(["NAN"], np.nan))
data['C4'] = np.array(data['C4'].replace(["NAN"], np.nan))
data['C5'] = np.array(data['C5'].replace(["NAN"], np.nan))

data['H1'] = np.array(data['H1'].replace(["NAN"], np.nan))
data['H2'] = np.array(data['H2'].replace(["NAN"], np.nan))
data['H3'] = np.array(data['H3'].replace(["NAN"], np.nan))
data['H4'] = np.array(data['H4'].replace(["NAN"], np.nan))
data['H5'] = np.array(data['H5'].replace(["NAN"], np.nan))

#Se le da formato a la fecha
data['datetime'] = pd.to_datetime(data['datetime'], format="%Y-%m-%d %H:%M:%S")

#Se convierte en índice el datetime
data = data.set_index('datetime')

#Convierte data en numéricos e ignora los errores
data = data.apply(pd.to_numeric, errors='ignore')

# Elige un día específico para graficar
fecha_especifica = '2023-11-11'

# Convierte la fecha a un objeto datetime
fecha_especifica = pd.to_datetime(fecha_especifica)

# Verifica si la fecha está dentro del rango de fechas del DataFrame
if fecha_especifica.date() in data.index.date:
    # Filtra los datos para el día específico
    datos_del_dia = data[data.index.date == fecha_especifica.date()]

#Se grafica la cobertura nubosa

#Se crea la figura
fig, ax = plt.subplots(1,figsize=(10,5),dpi=100)
ax.scatter(datos_del_dia.index, datos_del_dia['H1'], s=20*datos_del_dia['C1'], alpha=0.3, label = "Primera capa")
ax.scatter(datos_del_dia.index, datos_del_dia['H2'], s=20*datos_del_dia['C2'], alpha=0.3, label = "Segunda capa")
ax.scatter(datos_del_dia.index, datos_del_dia['H3'], s=20*datos_del_dia['C3'], alpha=0.3, label = "Tercera capa")
ax.scatter(datos_del_dia.index, datos_del_dia['H4'], s=20*datos_del_dia['C4'], alpha=0.3, label = "Cuarta capa")
ax.scatter(datos_del_dia.index, datos_del_dia['H5'], s=20*datos_del_dia['C5'], alpha=0.3, label = "Quinta capa")

#Se pone la leyenda
plt.legend(loc="best", facecolor="w", fontsize=10)

#Se le da formato a la fecha
fig.autofmt_xdate()
xfmt = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)

#Se nombran los ejes
plt.xlabel('Hora')
plt.ylabel('Altura (m)')

#Muestra la figura
plt.show()

#Se grafica la altura de las bases de las nubes

#Se guarda la figura
plt.savefig("cobertura.png")

#Se crea la figura
fig, ax = plt.subplots(1,figsize=(10,5),dpi=100)
ax.scatter(datos_del_dia.index,datos_del_dia['Z1'], linestyle = 'dotted', label = "Primera base")
ax.scatter(datos_del_dia.index,datos_del_dia['Z2'], linestyle = 'dotted', label = "Segunda base")
ax.scatter(datos_del_dia.index,datos_del_dia['Z3'], linestyle = 'dotted', label = "Tercera base")
ax.scatter(datos_del_dia.index,datos_del_dia['Z4'], linestyle = 'dotted', label = "Cuarta base")

plt.legend(loc="best", facecolor="w", fontsize=10)

#Se le da formato a la fecha
fig.autofmt_xdate()
xfmt = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)

plt.xlabel('Hora')
plt.ylabel('Altura (m)')

#Muestra la figura
plt.show()
plt.savefig("altura.png")