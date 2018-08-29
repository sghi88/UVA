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
#				print row[0]
				newline = row
				newline.pop(1)
				newline.pop(13)
				newline = list(map(float, newline))
				data.append(newline)
			i = i + 1
	return data

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

data = np.array(read_CSV3("S0_0149.CSV",1))
time = [dt.datetime.fromtimestamp(ts) for ts in data[:,1]]

R = [0.46,0.66,0.89,1.15,1.45,1.85,2.55,3.5,4.5,5.75,7.25,9,11,13,15,16.5]
fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()

fig.show()
fig.canvas.draw()

for i in range(len(data)):
	ax.clear()
	plt.title(time[i])
	plt.loglog(R, data[i,8:24])
	plt.ylim(ymax = max(data[:,8]), ymin = 0.1)
	fig.canvas.draw()


#fig = plt.figure(figsize=(7, 20), dpi=100)
#ax1 = fig.add_axes([0.1, 0.85, 0.8, 0.11])
#ax2 = fig.add_axes([0.1, 0.74, 0.8, 0.11])
#ax3 = fig.add_axes([0.1, 0.63, 0.8, 0.11])
#ax4 = fig.add_axes([0.1, 0.52, 0.8, 0.11])
#ax5 = fig.add_axes([0.1, 0.41, 0.8, 0.11])
#ax6 = fig.add_axes([0.1, 0.30, 0.8, 0.11])
#ax7 = fig.add_axes([0.1, 0.19, 0.8, 0.11])
#ax8 = fig.add_axes([0.1, 0.08, 0.8, 0.11])
#ax1.plot(time, data[:,8])
#ax1.set_ylabel('size bin 0')
#ax2.plot(time, data[:,9])
#ax2.set_ylabel('size bin 1')
#ax3.plot(time, data[:,10])
#ax3.set_ylabel('size bin 2')
#ax4.plot(time, data[:,11])
#ax4.set_ylabel('size bin 3')
#ax5.plot(time, data[:,12])
#ax5.set_ylabel('size bin 4')
#ax6.plot(time, data[:,13])
#ax6.set_ylabel('size bin 5')
#ax7.plot(time, data[:,14])
#ax7.set_ylabel('size bin 6')
#ax8.plot(time, data[:,15])
#ax8.set_xlabel('time')
#ax8.set_ylabel('size bin 7')
#plt.xticks(rotation = 25)
#ax8.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
##plt.savefig("plot2.pdf")

#fig2 = plt.figure(figsize=(7, 20), dpi=100)
#ax9 = fig2.add_axes([0.1, 0.85, 0.8, 0.11])
#ax9.set_ylabel('size bin 8')
#ax10 = fig2.add_axes([0.1, 0.74, 0.8, 0.11])
#ax10.set_ylabel('size bin 9')
#ax11 = fig2.add_axes([0.1, 0.63, 0.8, 0.11])
#ax11.set_ylabel('size bin 10')
#ax12 = fig2.add_axes([0.1, 0.52, 0.8, 0.11])
#ax12.set_ylabel('size bin 11')
#ax13 = fig2.add_axes([0.1, 0.41, 0.8, 0.11])
#ax13.set_ylabel('size bin 12')
#ax14 = fig2.add_axes([0.1, 0.30, 0.8, 0.11])
#ax14.set_ylabel('size bin 13')
#ax15 = fig2.add_axes([0.1, 0.19, 0.8, 0.11])
#ax15.set_ylabel('size bin 14')
#ax16 = fig2.add_axes([0.1, 0.08, 0.8, 0.11])
#ax16.set_ylabel('size bin 15')
#ax9.plot(time, data[:,16])
#ax10.plot(time, data[:,17])
#ax11.plot(time, data[:,18])
#ax12.plot(time, data[:,19])
#ax13.plot(time, data[:,20])
#ax14.plot(time, data[:,21])
#ax15.plot(time, data[:,22])
#ax16.plot(time, data[:,23])
#ax16.set_xlabel('time')
#ax16.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
#plt.xticks(rotation = 25)
#plt.savefig("plot3.pdf")

#plt.show()

#data = read_CSV2("test_sonde/sonde.CSV",1)
#data = np.array(read_CSV("Test_alphasense0620.CSV",16))
#data_red = np.array(reduce_data(data, 1600)) # r che ti da 38 righe
#R = [1, 2, 3, 4, 5, 7, 9, 11, 12, 13, 16, 18, 19, 20, 21, 22]

#fig = plt.figure()
#ax = fig.add_subplot(111)
#plt.ion()

#fig.show()
#fig.canvas.draw()

#for i in range(len(data_red)):
#	ax.clear()
#	plt.loglog(R, data_red[i,0:16])
#	plt.ylim(ymax = 100000, ymin = 1)
#	fig.canvas.draw()

#data1 = np.array(read_CSV("Test_alphasense0620.CSV",16))
#data2 = np.array(read_CSV2("Test_Logger0620.CSV",1))

#time2 =  [dt.datetime.fromtimestamp(ts) for ts in data2[:, 19]]

#now = data2[0,19]
#r = 2
#data_red = np.array(reduce_data(data1, r))
#data_red = data_red[:6437,:]
#tempo = len(data_red)
#y = range(0, tempo)
#timestamps = now + np.array(y)*1.398*r
#time1 = [dt.datetime.fromtimestamp(ts) for ts in timestamps]

#fig1,ax1 = plt.subplots() 
#ax1.plot(time1, data_red[:,0])
#ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
#plt.xticks(rotation = 25)
#plt.ylim(ymax = 100, ymin = 0)
#fig2,ax2 = plt.subplots() 
#plt.plot(time2[2:], data2[2:,0])
#ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
#plt.xticks(rotation = 25)

# Esempio di plot con read_METEO

#data = read_METEO("order_59882_data.txt", 3)
#time = [dt.datetime.fromtimestamp(ts) for ts in data[:,0]]

#fig,ax = plt.subplots() 
#ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
#plt.xticks(rotation = 25)
#ax.plot(time, data[:,input("Che colonna vuoi plottare? ")])
#plt.show()



#data = read_CSV('OPC2_000.CSV', 16)+read_CSV('OPC2_001.CSV', 16)+read_CSV('OPC2_002.CSV', 16)
#r = 900
#data_red = np.array(reduce_data(data, r))


#tempo = len(data_red)
#y = range(0, tempo)

#now = 1528223400
#now = time.mktime(time.localtime())
#timestamps = now + np.array(y)*1.4*r #600 sec = 15 min
#dates = [dt.datetime.fromtimestamp(ts) for ts in timestamps]

#####PLOT 1###################
#data_red_sel = data_red[:, np.arange(10)]
#x = range(1, len(data_red_sel[0])+1)

#Z = data_red_sel
#hf = plt.figure()
#ha = hf.add_subplot(111, projection='3d')

#X, Y = np.meshgrid(x, y)
#ha.plot_surface(X, Y, Z)

#ha.set_xlabel('bin')
#ha.set_ylabel('time')
#ha.set_zlabel('counts/s')
##plt.savefig("plot1.pdf")
#####PLOT 1###################

#####PLOT 2###################
#fig = plt.figure(figsize=(7, 20), dpi=100)
#ax1 = fig.add_axes([0.1, 0.85, 0.8, 0.11])
#ax2 = fig.add_axes([0.1, 0.74, 0.8, 0.11])
#ax3 = fig.add_axes([0.1, 0.63, 0.8, 0.11])
#ax4 = fig.add_axes([0.1, 0.52, 0.8, 0.11])
#ax5 = fig.add_axes([0.1, 0.41, 0.8, 0.11])
#ax6 = fig.add_axes([0.1, 0.30, 0.8, 0.11])
#ax7 = fig.add_axes([0.1, 0.19, 0.8, 0.11])
#ax8 = fig.add_axes([0.1, 0.08, 0.8, 0.11])
#ax1.plot(dates, data_red[:,0])
#ax1.set_ylabel('size bin 0')
#ax2.plot(dates, data_red[:,1])
#ax2.set_ylabel('size bin 1')
#ax3.plot(dates, data_red[:,2])
#ax3.set_ylabel('size bin 2')
#ax4.plot(dates, data_red[:,3])
#ax4.set_ylabel('size bin 3')
#ax5.plot(dates, data_red[:,4])
#ax5.set_ylabel('size bin 4')
#ax6.plot(dates, data_red[:,5])
#ax6.set_ylabel('size bin 5')
#ax7.plot(dates, data_red[:,6])
#ax7.set_ylabel('size bin 6')
#ax8.plot(dates, data_red[:,7])
#ax8.set_xlabel('time')
#ax8.set_ylabel('size bin 7')
#plt.xticks(rotation = 25)
#ax8.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d \n %H:%M"))
#plt.savefig("plot2.pdf")
#####PLOT 2###################

#####PLOT 3###################
#fig2 = plt.figure(figsize=(7, 20), dpi=100)
#ax9 = fig2.add_axes([0.1, 0.85, 0.8, 0.11])
#ax9.set_ylabel('size bin 8')
#ax10 = fig2.add_axes([0.1, 0.74, 0.8, 0.11])
#ax10.set_ylabel('size bin 9')
#ax11 = fig2.add_axes([0.1, 0.63, 0.8, 0.11])
#ax11.set_ylabel('size bin 10')
#ax12 = fig2.add_axes([0.1, 0.52, 0.8, 0.11])
#ax12.set_ylabel('size bin 11')
#ax13 = fig2.add_axes([0.1, 0.41, 0.8, 0.11])
#ax13.set_ylabel('size bin 12')
#ax14 = fig2.add_axes([0.1, 0.30, 0.8, 0.11])
#ax14.set_ylabel('size bin 13')
#ax15 = fig2.add_axes([0.1, 0.19, 0.8, 0.11])
#ax15.set_ylabel('size bin 14')
#ax16 = fig2.add_axes([0.1, 0.08, 0.8, 0.11])
#ax16.set_ylabel('size bin 15')
#ax9.plot(dates, data_red[:,8])
#ax10.plot(dates, data_red[:,9])
#ax11.plot(dates, data_red[:,10])
#ax12.plot(dates, data_red[:,11])
#ax13.plot(dates, data_red[:,12])
#ax14.plot(dates, data_red[:,13])
#ax15.plot(dates, data_red[:,14])
#ax16.plot(dates, data_red[:,15])
#ax16.set_xlabel('time')
#plt.xticks(rotation = 25)
#plt.savefig("plot3.pdf")
#####PLOT 4###################
#fig3 = plt.figure(figsize=(7, 12), dpi=100)
#ax1 = fig3.add_axes([0.1, 0.66, 0.8, 0.28])
#ax2 = fig3.add_axes([0.1, 0.38, 0.8, 0.28])
#ax3 = fig3.add_axes([0.1, 0.1, 0.8, 0.28])
#ax1.plot(dates, data_red[:,-3])
#ax2.plot(dates, data_red[:,-2])
#ax3.plot(dates, data_red[:,-1])
#ax3.set_xlabel('time')
#ax1.set_ylabel('PM1 [ug/m3])')
#ax2.set_ylabel('PM2.5 [ug/m3]')
#ax3.set_ylabel('PM10 [ug/m3]')
#plt.xticks(rotation = 25)
#plt.savefig("plot4.pdf")
#####PLOT 4###################

#####PLOT 5###################
#fig4 = plt.figure()
#plt.semilogy(dates, data_red[:,0])
#plt.semilogy(dates, data_red[:,3])
#plt.semilogy(dates, data_red[:,6])
#plt.semilogy(dates, data_red[:,9])
#plt.semilogy(dates, data_red[:,12])
#plt.semilogy(dates, data_red[:,15])
#plt.axvline(x=dt.datetime.fromtimestamp(now+200*60))
#plt.xlabel('time')
#plt.ylabel('sizebin')
#plt.legend(["bin1", "bin4", "bin7", "bin10", "bin13", "bin16"])
#plt.xticks(rotation = 25)
#plt.savefig("plot5.pdf")
#####PLOT 5###################

#plt.show()


