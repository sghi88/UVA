# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 22:40:16 2018

@author: Joseph
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import datetime as dt
import time
import matplotlib.dates as mdates


def read_CSV2(filename, fakelines):
	data = []
	with open(filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		i = 1
		for row in spamreader:
			if i > fakelines:
				#print row[0]
				newline = row
				
				newline.pop(1)  # data in formato stringa --> va tolta con .pop per avere np.array
				newline.pop(13)
				#print newline
				newline = list(map(float, newline))
				
                                    
				data.append(newline)
			i = i + 1
	return data
 

data = np.array(read_CSV2("sonde.CSV",1))
time = [dt.datetime.fromtimestamp(ts) for ts in data[:, 0]]


###############SONDE BS18D temperatura################################
media=(data[:,1]+data[:,2]+data[:,3]+data[:,4]+data[:,5]+data[:,6])/6

fig1,ax1 = plt.subplots() 
plt.plot(time, data[:,1], time, data[:,2], time, data[:,3], time, data[:,4], time, data[:,5], time, data[:,6])
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
plt.xticks(rotation = 25)

fig2,ax2 = plt.subplots() 
plt.plot(time, data[:,1]-media, time, data[:,2]-media, time, data[:,3]-media, time, data[:,4]-media, time, data[:,5]-media, time, data[:,6]-media)
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
plt.xticks(rotation = 25)

###########################SOndeDHT22 temperatura###################

fig4,ax4 = plt.subplots() 
plt.plot(time, data[:,8], time, data[:,10],time, media)
ax4.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
plt.xticks(rotation = 25)

fig5,ax5 = plt.subplots() 
plt.plot(time, data[:,8]-media, time, data[:,10]-media)
ax5.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
plt.xticks(rotation = 25)



###########################SOndeDHT22 umidità###################

fig6,ax6 = plt.subplots() 
plt.plot(time, data[:,7], time, data[:,9])
ax6.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
plt.xticks(rotation = 25)



###########################Soil Moisture###################

fig7,ax7 = plt.subplots() 
plt.plot(time, data[:,11], time, data[:,12])
ax7.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
plt.xticks(rotation = 25)


#############################LUX################################

dataLUXalpha2 = np.array(read_CSV2("sondaLUX_alpha2.CSV",1))
dataLUXalpha3 = np.array(read_CSV2("sondaLUX_alpha3.CSV",1))
timeLUX = [dt.datetime.fromtimestamp(ts) for ts in dataLUXapha2[:, 0]] 

fig8,ax8 = plt.subplots() 
plt.plot(timeLUX, dataLUXalpha2[:,23], timeLUX, dataLUXalpha3[:115898,23])
ax8.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
plt.xticks(rotation = 25)




