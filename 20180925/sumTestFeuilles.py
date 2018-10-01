# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:07:59 2018

@author: Pini
"""

import csv
import numpy as np
import matplotlib.pyplot as plt


def read_CSV(filename, fakelines):
	data = []
	with open(filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')  # apre il file riga per riga
		i = 1
		for row in spamreader:
			if i > fakelines:
				newline = row[0].split(",")  #prende ogni riga e separa i suoi elementi dove c'é la virgola
				newline = list(map(float, newline))
				data.append(newline)
			i = i + 1
	return data


data1 = np.array(read_CSV('OPC2_039.CSV', 16))
data2 =np.array(read_CSV('OPC2_040.CSV', 16))
data3 =np.array(read_CSV('OPC2_041.CSV', 16))
data11 = np.array(read_CSV('OPC2_004.CSV', 16))
data22 =np.array(read_CSV('OPC2_005.CSV', 16))
data33 =np.array(read_CSV('OPC2_006.CSV', 16))

data1_sum = data1.sum(axis=0)/len(data1)
data2_sum = data2.sum(axis=0)/len(data2)
data3_sum = data2.sum(axis=0)/len(data3)

data11_sum = data11.sum(axis=0)/len(data11)
data22_sum = data22.sum(axis=0)/len(data22)
data33_sum = data33.sum(axis=0)/len(data33)


binN2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
binN3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]



binN2 = [1, 1.5, 3, 3.3, 4, 4.1, 4.3, 5, 6, 8, 10, 14, 14.5, 16, 17, 18]
binN2.insert(0,0)

fig, ax = plt.subplots()

for i in range(16):
	line1 = ax.hlines(y=data1_sum[i], xmin=binN2[i], xmax=binN2[i+1], linewidth=1.5, color='grey', label='data1')
ax.set_yscale('log')
for i in range(16):
	line2 = ax.hlines(y=data3_sum[i], xmin=binN2[i], xmax=binN2[i+1], linewidth=1.5, color='purple', label='data3')
ax.set_yscale('log')
for i in range(16):
	line3 = ax.hlines(y=data2_sum[i], xmin=binN2[i], xmax=binN2[i+1], linewidth=1.5, color='orange', label='data2')
ax.set_yscale('log')

ax.legend(handles=[line1,line2,line3], loc=1)

plt.show()
###########

########################################
#binN2 = [1, 1.5, 3, 3.3, 4, 4.1, 4.3, 5, 6, 8, 10, 14, 14.5, 16, 17, 18]
#binN2.insert(0,0)

#fig, ax = plt.subplots()

#for i in range(16):
#	line = ax.hlines(y=data3_sum[i]-data1_sum[i], xmin=binN2[i], xmax=binN2[i+1], linewidth=1.5, color='purple', label='Vittorio ha il pisello piccolo')

##ax.set_yscale('log')
#ax.legend(handles=[line], loc=4)
#plt.title("Lunghezza del pene di Vittorio in funzione dell'eta'")
#ax.set_ylabel("Lunghezza pene di Vittorio")
#ax.set_xlabel("eta'")

#plt.show()
########################################




#fig1 = plt.figure(figsize=(9, 20), dpi=100)
#ax1 = fig1.add_axes([0.1, 0.85, 0.8, 0.11])

#ax1.plot(binN2,data3_sum[:16]-data1_sum[:16],'o', color='green',alpha=0.5)
#ax1.plot(binN2,data2_sum[:16]-data1_sum[:16],'o', color='red',alpha=0.5)

#ax1.set_xlabel('size_bin')
#ax1.set_ylabel('[Counts/30min]')
#plt.title('OPC-N2')
#plt.savefig("N2.pdf")


#fig2 = plt.figure(figsize=(9, 20), dpi=100)
#ax2 = fig2.add_axes([0.1, 0.85, 0.8, 0.11])
#ax2.plot(binN3,data33_sum[:23]-data11_sum[:23],'o', color='green',alpha=0.5)
#ax2.plot(binN3,data22_sum[:23]-data11_sum[:23],'o', color='red',alpha=0.5)
#ax2.set_ylabel('[Counts/30min]')
#ax2.set_xlabel('size_bin')
#plt.title('OPC-N3')
#plt.savefig("N3.pdf")

#fig3 = plt.figure(figsize=(9, 20), dpi=100)
#ax3 = fig3.add_axes([0.1, 0.85, 0.8, 0.11])
#ax3.plot(binN2,data3_sum[:16]-data2_sum[:16],'o', color='black',alpha=0.5, label='cc')
#ax3.plot(binN3,data33_sum[:23]-data22_sum[:23],'o', color='grey',alpha=0.5)
#ax3.set_ylabel('[Counts/30min]')
#ax3.set_xlabel('size_bin')
#plt.legend
#plt.title('OPC-N3&N2')
#plt.savefig("N3&N2.pdf")

#plt.show()


