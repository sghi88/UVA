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

def read_CSV(filename, fakelines):
	data = []
	with open(filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		i = 1
		for row in spamreader:
			if i > fakelines:
				newline = row[0].split(",")
				newline = list(map(float, newline))
				data.append(newline)
			i = i + 1
	return data


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

fig1,ax1 = plt.subplots() 
plt.plot(time, data[:,2], time, data[:,3], time, data[:,4], time, data[:,5], time, data[:,6], time, data[:7])
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
plt.xticks(rotation = 25)
