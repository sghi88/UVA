# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:18:00 2018

@author: pini
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#import datetime as dt
#import time
#import matplotlib.dates as mdates

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

tempo1 = np.array(range(0, len(data1)))
tempo2 = np.array(range(0, len(data2)))
tempo3 = np.array(range(0, len(data3)))
tempo11 = np.array(range(0, len(data11)))
tempo22 = np.array(range(0, len(data22)))
tempo33 = np.array(range(0, len(data33)))
#now = 1537891511
#timestamps1 = now + np.array(y1)*1.4
#dates1 = [dt.datetime.fromtimestamp(ts) for ts in timestamps1]



####PLOT OPCN2###################
fig = plt.figure(figsize=(9, 20), dpi=100)
ax1 = fig.add_axes([0.1, 0.85, 0.8, 0.11])
ax2 = fig.add_axes([0.1, 0.74, 0.8, 0.11])
ax3 = fig.add_axes([0.1, 0.63, 0.8, 0.11])
ax4 = fig.add_axes([0.1, 0.52, 0.8, 0.11])
ax5 = fig.add_axes([0.1, 0.41, 0.8, 0.11])
ax6 = fig.add_axes([0.1, 0.30, 0.8, 0.11])
ax7 = fig.add_axes([0.1, 0.19, 0.8, 0.11])
ax8 = fig.add_axes([0.1, 0.08, 0.8, 0.11])

ax1.plot(tempo1, data1[:,0],alpha=0.2)
ax2.plot(tempo1, data1[:,1],'o', color='blue',alpha=0.5)
ax3.plot(tempo1, data1[:,2],'o', color='blue',alpha=0.5)
ax4.plot(tempo1, data1[:,3],'o', color='blue',alpha=0.5)
ax5.plot(tempo1, data1[:,4],'o', color='blue',alpha=0.5)
ax6.plot(tempo1, data1[:,5],'o', color='blue',alpha=0.5)
ax7.plot(tempo1, data1[:,6],'o', color='blue',alpha=0.5)
ax8.plot(tempo1, data1[:,7],'o', color='blue',alpha=0.5)

ax1.plot(tempo2, data2[:,0],'o', color='green',alpha=0.5)
ax2.plot(tempo2, data2[:,1],'o', color='green',alpha=0.5)
ax3.plot(tempo2, data2[:,2],'o', color='green',alpha=0.5)
ax4.plot(tempo2, data2[:,3],'o', color='green',alpha=0.5)
ax5.plot(tempo2, data2[:,4],'o', color='green',alpha=0.5)
ax6.plot(tempo2, data2[:,5],'o', color='green',alpha=0.5)
ax7.plot(tempo2, data2[:,6],'o', color='green',alpha=0.5)
ax8.plot(tempo2, data2[:,7],'o', color='green',alpha=0.5)

ax1.plot(tempo3, data3[:,0],'o', color='red',alpha=0.5)
ax2.plot(tempo3, data3[:,1],'o', color='red',alpha=0.5)
ax3.plot(tempo3, data3[:,2],'o', color='red',alpha=0.5)
ax4.plot(tempo3, data3[:,3],'o', color='red',alpha=0.5)
ax5.plot(tempo3, data3[:,4],'o', color='red',alpha=0.5)
ax6.plot(tempo3, data3[:,5],'o', color='red',alpha=0.5)
ax7.plot(tempo3, data3[:,6],'o', color='red',alpha=0.5)
ax8.plot(tempo3, data3[:,7],'o', color='red',alpha=0.5)


ax1.set_ylabel('bin 0 [Counts/s]')
ax2.set_ylabel('bin 1 [Counts/s]' )
ax3.set_ylabel('bin 2 [Counts/s]')
ax4.set_ylabel('bin 3 [Counts/s]')
ax5.set_ylabel('bin 4 [Counts/s]')
ax6.set_ylabel('bin 5 [Counts/s]')
ax7.set_ylabel('bin 6 [Counts/s]')
ax8.set_ylabel('bin 7 [Counts/s]')

plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax5.get_xticklabels(), visible=False)
plt.setp(ax6.get_xticklabels(), visible=False)
plt.setp(ax7.get_xticklabels(), visible=False)

plt.savefig("OPCN2_bin0-7.pdf")


fig2 = plt.figure(figsize=(9, 20), dpi=100)
ax9 = fig2.add_axes([0.1, 0.85, 0.8, 0.11])
ax10 = fig2.add_axes([0.1, 0.74, 0.8, 0.11])
ax11 = fig2.add_axes([0.1, 0.63, 0.8, 0.11])
ax12 = fig2.add_axes([0.1, 0.52, 0.8, 0.11])
ax13 = fig2.add_axes([0.1, 0.41, 0.8, 0.11])
ax14 = fig2.add_axes([0.1, 0.30, 0.8, 0.11])
ax15 = fig2.add_axes([0.1, 0.19, 0.8, 0.11])
ax16 = fig2.add_axes([0.1, 0.08, 0.8, 0.11])

ax9.plot(tempo1, data1[:,8],'o', color='blue',alpha=0.5)
ax10.plot(tempo1, data1[:,9],'o', color='blue',alpha=0.5)
ax11.plot(tempo1, data1[:,10],'o', color='blue',alpha=0.5)
ax12.plot(tempo1, data1[:,11],'o', color='blue',alpha=0.5)
ax13.plot(tempo1, data1[:,12],'o', color='blue',alpha=0.5)
ax14.plot(tempo1, data1[:,13],'o', color='blue',alpha=0.5)
ax15.plot(tempo1, data1[:,14],'o', color='blue',alpha=0.5)
ax16.plot(tempo1, data1[:,15],'o', color='blue',alpha=0.5)

ax9.plot(tempo2, data2[:,8],'o', color='green',alpha=0.5)
ax10.plot(tempo2, data2[:,9],'o', color='green',alpha=0.5)
ax11.plot(tempo2, data2[:,10],'o', color='green',alpha=0.5)
ax12.plot(tempo2, data2[:,11],'o', color='green',alpha=0.5)
ax13.plot(tempo2, data2[:,12],'o', color='green',alpha=0.5)
ax14.plot(tempo2, data2[:,13],'o', color='green',alpha=0.5)
ax15.plot(tempo2, data2[:,14],'o', color='green',alpha=0.5)
ax16.plot(tempo2, data2[:,15],'o', color='green',alpha=0.5)

ax9.plot(tempo3, data3[:,8],'o', color='red',alpha=0.5)
ax10.plot(tempo3, data3[:,9],'o', color='red',alpha=0.5)
ax11.plot(tempo3, data3[:,10],'o', color='red',alpha=0.5)
ax12.plot(tempo3, data3[:,11],'o', color='red',alpha=0.5)
ax13.plot(tempo3, data3[:,12],'o', color='red',alpha=0.5)
ax14.plot(tempo3, data3[:,13],'o', color='red',alpha=0.5)
ax15.plot(tempo3, data3[:,14],'o', color='red',alpha=0.5)
ax16.plot(tempo3, data3[:,15],'o', color='red',alpha=0.5)



ax9.set_ylabel('bin 8 [Counts/s]')
ax10.set_ylabel('bin 9 [Counts/s]')
ax11.set_ylabel('bin 10 [Counts/s]')
ax12.set_ylabel('bin 11 [Counts/s]')
ax13.set_ylabel('bin 12 [Counts/s]')
ax14.set_ylabel('bin 13 [Counts/s]')
ax15.set_ylabel('bin 14 [Counts/s]')
ax16.set_ylabel('bin 15 [Counts/s]')

plt.setp(ax9.get_xticklabels(), visible=False)
plt.setp(ax10.get_xticklabels(), visible=False)
plt.setp(ax11.get_xticklabels(), visible=False)
plt.setp(ax12.get_xticklabels(), visible=False)
plt.setp(ax13.get_xticklabels(), visible=False)
plt.setp(ax14.get_xticklabels(), visible=False)
plt.setp(ax15.get_xticklabels(), visible=False)


plt.savefig("OPCN2_bin8-15um.pdf")

##############PLOT OPC-N3##############

fig3 = plt.figure(figsize=(9, 20), dpi=100)
bx1 = fig3.add_axes([0.1, 0.85, 0.8, 0.11])
bx2 = fig3.add_axes([0.1, 0.74, 0.8, 0.11])
bx3 = fig3.add_axes([0.1, 0.63, 0.8, 0.11])
bx4 = fig3.add_axes([0.1, 0.52, 0.8, 0.11])
bx5 = fig3.add_axes([0.1, 0.41, 0.8, 0.11])
bx6 = fig3.add_axes([0.1, 0.30, 0.8, 0.11])
bx7 = fig3.add_axes([0.1, 0.19, 0.8, 0.11])
bx8 = fig3.add_axes([0.1, 0.08, 0.8, 0.11])

bx1.plot(tempo11, data11[:,0],'o', color='blue',alpha=0.5)
bx2.plot(tempo11, data11[:,1],'o', color='blue',alpha=0.5)
bx3.plot(tempo11, data11[:,2],'o', color='blue',alpha=0.5)
bx4.plot(tempo11, data11[:,3],'o', color='blue',alpha=0.5)
bx5.plot(tempo11, data11[:,4],'o', color='blue',alpha=0.5)
bx6.plot(tempo11, data11[:,5],'o', color='blue',alpha=0.5)
bx7.plot(tempo11, data11[:,6],'o', color='blue',alpha=0.5)
bx8.plot(tempo11, data11[:,7],'o', color='blue',alpha=0.5)

bx1.plot(tempo22, data22[:,0],'o', color='green',alpha=0.5)
bx2.plot(tempo22, data22[:,1],'o', color='green',alpha=0.5)
bx3.plot(tempo22, data22[:,2],'o', color='green',alpha=0.5)
bx4.plot(tempo22, data22[:,3],'o', color='green',alpha=0.5)
bx5.plot(tempo22, data22[:,4],'o', color='green',alpha=0.5)
bx6.plot(tempo22, data22[:,5],'o', color='green',alpha=0.5)
bx7.plot(tempo22, data22[:,6],'o', color='green',alpha=0.5)
bx8.plot(tempo22, data22[:,7],'o', color='green',alpha=0.5)

bx1.plot(tempo33, data33[:,0],'o', color='red',alpha=0.5)
bx2.plot(tempo33, data33[:,1],'o', color='red',alpha=0.5)
bx3.plot(tempo33, data33[:,2],'o', color='red',alpha=0.5)
bx4.plot(tempo33, data33[:,3],'o', color='red',alpha=0.5)
bx5.plot(tempo33, data33[:,4],'o', color='red',alpha=0.5)
bx6.plot(tempo33, data33[:,5],'o', color='red',alpha=0.5)
bx7.plot(tempo33, data33[:,6],'o', color='red',alpha=0.5)
bx8.plot(tempo33, data33[:,7],'o', color='red',alpha=0.5)


bx1.set_ylabel('bin 0 [Counts/s]')
bx2.set_ylabel('bin 1 [Counts/s]' )
bx3.set_ylabel('bin 2 [Counts/s]')
bx4.set_ylabel('bin 3 [Counts/s]')
bx5.set_ylabel('bin 4 [Counts/s]')
bx6.set_ylabel('bin 5 [Counts/s]')
bx7.set_ylabel('bin 6 [Counts/s]')
bx8.set_ylabel('bin 7 [Counts/s]')

plt.setp(bx1.get_xticklabels(), visible=False)
plt.setp(bx2.get_xticklabels(), visible=False)
plt.setp(bx3.get_xticklabels(), visible=False)
plt.setp(bx4.get_xticklabels(), visible=False)
plt.setp(bx5.get_xticklabels(), visible=False)
plt.setp(bx6.get_xticklabels(), visible=False)
plt.setp(bx7.get_xticklabels(), visible=False)

plt.savefig("OPCN3_bin0-7.pdf")


fig4 = plt.figure(figsize=(9, 20), dpi=100)
bx9 = fig4.add_axes([0.1, 0.85, 0.8, 0.11])
bx10 = fig4.add_axes([0.1, 0.74, 0.8, 0.11])
bx11 = fig4.add_axes([0.1, 0.63, 0.8, 0.11])
bx12 = fig4.add_axes([0.1, 0.52, 0.8, 0.11])
bx13 = fig4.add_axes([0.1, 0.41, 0.8, 0.11])
bx14 = fig4.add_axes([0.1, 0.30, 0.8, 0.11])
bx15 = fig4.add_axes([0.1, 0.19, 0.8, 0.11])
bx16 = fig4.add_axes([0.1, 0.08, 0.8, 0.11])

bx9.plot(tempo11, data11[:,8],'o', color='blue',alpha=0.5)
bx10.plot(tempo11, data11[:,9],'o', color='blue',alpha=0.5)
bx11.plot(tempo11, data11[:,10],'o', color='blue',alpha=0.5)
bx12.plot(tempo11, data11[:,11],'o', color='blue',alpha=0.5)
bx13.plot(tempo11, data11[:,12],'o', color='blue',alpha=0.5)
bx14.plot(tempo11, data11[:,13],'o', color='blue',alpha=0.5)
bx15.plot(tempo11, data11[:,14],'o', color='blue',alpha=0.5)
bx16.plot(tempo11, data11[:,15],'o', color='blue',alpha=0.5)

bx9.plot(tempo22, data22[:,8],'o', color='green',alpha=0.5)
bx10.plot(tempo22, data22[:,9],'o', color='green',alpha=0.5)
bx11.plot(tempo22, data22[:,10],'o', color='green',alpha=0.5)
bx12.plot(tempo22, data22[:,11],'o', color='green',alpha=0.5)
bx13.plot(tempo22, data22[:,12],'o', color='green',alpha=0.5)
bx14.plot(tempo22, data22[:,13],'o', color='green',alpha=0.5)
bx15.plot(tempo22, data22[:,14],'o', color='green',alpha=0.5)
bx16.plot(tempo22, data22[:,15],'o', color='green',alpha=0.5)

bx9.plot(tempo33, data33[:,8],'o', color='red',alpha=0.5)
bx10.plot(tempo33, data33[:,9],'o', color='red',alpha=0.5)
bx11.plot(tempo33, data33[:,10],'o', color='red',alpha=0.5)
bx12.plot(tempo33, data33[:,11],'o', color='red',alpha=0.5)
bx13.plot(tempo33, data33[:,12],'o', color='red',alpha=0.5)
bx14.plot(tempo33, data33[:,13],'o', color='red',alpha=0.5)
bx15.plot(tempo33, data33[:,14],'o', color='red',alpha=0.5)
bx16.plot(tempo33, data33[:,15],'o', color='red',alpha=0.5)



bx9.set_ylabel('bin 8 [Counts/s]')
bx10.set_ylabel('bin 9 [Counts/s]')
bx11.set_ylabel('bin 10 [Counts/s]')
bx12.set_ylabel('bin 11 [Counts/s]')
bx13.set_ylabel('bin 12 [Counts/s]')
bx14.set_ylabel('bin 13 [Counts/s]')
bx15.set_ylabel('bin 14 [Counts/s]')
bx16.set_ylabel('bin 15 [Counts/s]')

plt.setp(bx9.get_xticklabels(), visible=False)
plt.setp(bx10.get_xticklabels(), visible=False)
plt.setp(bx11.get_xticklabels(), visible=False)
plt.setp(bx12.get_xticklabels(), visible=False)
plt.setp(bx13.get_xticklabels(), visible=False)
plt.setp(bx14.get_xticklabels(), visible=False)
plt.setp(bx15.get_xticklabels(), visible=False)

plt.savefig("OPCN3_bin8-15.pdf")

fig5 = plt.figure(figsize=(9, 20), dpi=100)
bx17 = fig5.add_axes([0.1, 0.85, 0.8, 0.11])
bx18 = fig5.add_axes([0.1, 0.74, 0.8, 0.11])
bx19 = fig5.add_axes([0.1, 0.63, 0.8, 0.11])
bx20 = fig5.add_axes([0.1, 0.52, 0.8, 0.11])
bx21 = fig5.add_axes([0.1, 0.41, 0.8, 0.11])
bx22 = fig5.add_axes([0.1, 0.30, 0.8, 0.11])
bx23 = fig5.add_axes([0.1, 0.19, 0.8, 0.11])
bx24 = fig5.add_axes([0.1, 0.08, 0.8, 0.11])

bx17.plot(tempo11, data11[:,16],'o', color='blue',alpha=0.5)
bx18.plot(tempo11, data11[:,17],'o', color='blue',alpha=0.5)
bx19.plot(tempo11, data11[:,18],'o', color='blue',alpha=0.5)
bx20.plot(tempo11, data11[:,19],'o', color='blue',alpha=0.5)
bx21.plot(tempo11, data11[:,20],'o', color='blue',alpha=0.5)
bx22.plot(tempo11, data11[:,21],'o', color='blue',alpha=0.5)
bx23.plot(tempo11, data11[:,22],'o', color='blue',alpha=0.5)
bx24.plot(tempo11, data11[:,23],'o', color='blue',alpha=0.5)

bx17.plot(tempo22, data22[:,16],'o', color='green',alpha=0.5)
bx18.plot(tempo22, data22[:,17],'o', color='green',alpha=0.5)
bx19.plot(tempo22, data22[:,18],'o', color='green',alpha=0.5)
bx20.plot(tempo22, data22[:,19],'o', color='green',alpha=0.5)
bx21.plot(tempo22, data22[:,20],'o', color='green',alpha=0.5)
bx22.plot(tempo22, data22[:,21],'o', color='green',alpha=0.5)
bx23.plot(tempo22, data22[:,22],'o', color='green',alpha=0.5)
bx24.plot(tempo22, data22[:,23],'o', color='green',alpha=0.5)

bx17.plot(tempo33, data33[:,16],'o', color='red',alpha=0.5)
bx18.plot(tempo33, data33[:,17],'o', color='red',alpha=0.5)
bx19.plot(tempo33, data33[:,18],'o', color='red',alpha=0.5)
bx20.plot(tempo33, data33[:,19],'o', color='red',alpha=0.5)
bx21.plot(tempo33, data33[:,20],'o', color='red',alpha=0.5)
bx22.plot(tempo33, data33[:,21],'o', color='red',alpha=0.5)
bx23.plot(tempo33, data33[:,22],'o', color='red',alpha=0.5)
bx24.plot(tempo33, data33[:,23],'o', color='red',alpha=0.5)


bx17.set_ylabel('bin 16 [Counts/s]')
bx18.set_ylabel('bin 17 [Counts/s]')
bx19.set_ylabel('bin 18 [Counts/s]')
bx20.set_ylabel('bin 19 [Counts/s]')
bx21.set_ylabel('bin 20 [Counts/s]')
bx22.set_ylabel('bin 21 [Counts/s]')
bx23.set_ylabel('bin 22 [Counts/s]')
bx24.set_ylabel('bin 23 [Counts/s]')


plt.setp(bx17.get_xticklabels(), visible=False)
plt.setp(bx18.get_xticklabels(), visible=False)
plt.setp(bx19.get_xticklabels(), visible=False)
plt.setp(bx20.get_xticklabels(), visible=False)
plt.setp(bx21.get_xticklabels(), visible=False)
plt.setp(bx22.get_xticklabels(), visible=False)
plt.setp(bx23.get_xticklabels(), visible=False)

plt.savefig("OPCN3_bin16-23.pdf")
plt.show()
