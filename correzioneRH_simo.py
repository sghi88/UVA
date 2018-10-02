# -*- coding: utf-8 -*-
"""
Created on Tue Oct 02 13:28:22 2018

@author: Joseph
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import datetime as dt
import time
import matplotlib.dates as mdates

def read_CSV3(filename, fakelines):
	data = []
	with open(filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		i = 1
		for row in spamreader:
			if i > fakelines:
				newline = row
				newline = list(map(float, newline))
				data.append(newline)
			i = i + 1
	return data

def read_METEO(filename, fakelines):
	data = []
	with open(filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		i = 1
		for row in spamreader:
			if i > fakelines:
				if row == []:
					break
				if ";-;" in row[0]:
					continue
				newline = row[0].split(";")
				data.append(newline)
			i = i + 1
	data = np.array(data)
	times = data[:,1]
	data = data[:,1:].astype(float)
	data[:,0] = [time.mktime(dt.datetime.strptime(x, '%Y%m%d%H%M').timetuple()) for x in times]		
	return data

def reduce_data(data, r):
	data = np.array(data)
	data_red = []
	for k in range(len(data)):
		if k%r == 0:
			newline = data[k]
		elif k%r == r-1:
			newline = newline + data[k]
			data_red.append(newline)
			newline[-3:] = newline[-3:]/r   #media
		else:
			newline = newline + data[k]
	return data_red

dati_CSV = np.array(read_CSV3("OPC2_002.CSV",16)
)



dati_meteo = np.array(read_METEO("order_62441_data.txt", 3))

initial_time = 1528742640 # 11.06.2018 18:44
time = np.arange(initial_time, initial_time+1.4*len(dati_CSV)-0.1,1.4)
time = time[:, None]

dati_CSV = np.append(time, dati_CSV, axis=1)

new_HR = np.zeros([len(dati_CSV), 1])
range_meteo = len(dati_CSV)/429

for i in range(range_meteo):
	for j in range(429):
		new_HR[i*429 + j,0] = dati_meteo[i,6] + (dati_meteo[i+1,6]-dati_meteo[i,6])*j/429.

dati_CSV = np.append(dati_CSV, new_HR, axis=1)
dati_CSV = dati_CSV[:len(dati_CSV)-429,:]

# Il codice sotto è la versione estesa di quello che faccio dopo in una linea
for i in range(len(dati_CSV)):
	C = (1. + (0.4/1.65)/(-1. + 1./(dati_CSV[i, -1]/100)))
	dati_CSV[i, -4:-1] = dati_CSV[i, -4:-1]/C

#dati_CSV[:, -4:-1] = dati_CSV[:, -4:-1]/(1. + (0.4/1.65)/(-1. + 1./np.repeat(dati_CSV[:, -1],3).reshape((len(dati_CSV), 3))))
#ma al posto di sostituire i dati, aggiungo 3 colonne alla fine. quindi avremo: -7 -6 -5 sono i non corretti. -4 HR e poi abbiamo i corretti:  -3 -2 -1

#429  a 0 metto il primo valore HR a 429 il secondo a 878 il terzo e così via

dati_CSV = np.append(dati_CSV, dati_CSV[:, -4:-1]/(1. + (0.4/1.65)/(-1. + 1./np.repeat(dati_CSV[:, -1],3).reshape((len(dati_CSV), 3)))), axis=1)

fig = plt.figure(figsize=(7, 20), dpi=100)
ax1 = fig.add_axes([0.1, 0.85, 0.8, 0.11])
ax2 = fig.add_axes([0.1, 0.74, 0.8, 0.11])


ax1.set_ylabel('HR[%]')
ax2.set_ylabel('PM1[ug/m3]')

time = [dt.datetime.fromtimestamp(ts) for ts in dati_CSV[:,0]]
ax1.plot(time, dati_CSV[:,-4])
ax2.plot(time, dati_CSV[:,-7],alpha=0.5)
ax2.plot(time, dati_CSV[:,-3],alpha=0.5)
plt.ylim(0,200)

plt.xticks(rotation = 25)
ax2.set_xlabel('time')
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
#plt.savefig("bin0_8.pdf")
