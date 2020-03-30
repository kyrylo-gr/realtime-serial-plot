# -*- coding: utf-8 -*-

import serial
import numpy as np
from matplotlib import pyplot as plt
import time

ser = serial.Serial('COM8',115200) #/dev/ttyACM0', 115200)

plt.ion() 

colors = ['b','r','c','g','m','y','k']
def pltupdate(fig,ax,dats,tp="plot"):
    if ax.lines:
        for i, line in enumerate(ax.lines):
            if i>=len(dats): break
            if type(dats[i])!=int or dats[i]!=0:
                if type(dats[i])==tuple:
                    line.set_xdata(dats[i][0])
                    line.set_ydata(dats[i][1])
                else:
                    line.set_ydata(dats[i])

        for j in range(i+1,len(dats)):
            if type(dats[j])!=int or dats[j]!=0:
                color = colors[j%len(colors)] #'b' if j>=len(colors) else colors[j]
                if type(dats[j])==tuple:
                    if tp=="loglog":
                        ax.loglog(dats[j][0],dats[j][1], color)
                    elif tp=="plot":
                        ax.plot(dats[j][0],dats[j][1], color)
                else:
                    if tp=="loglog":
                        ax.loglog(dats[j], color)
                    elif tp=="plot":
                        ax.plot(dats[j], color)
            else:
                print("there are some plots missing ({}), but it'll be skiped".format(j))
    else:
        for i, dat in enumerate(dats):
            if type(dat)!=int or dat!=0:
                color = colors[i%len(colors)] #'b' if i>=len(colors) else colors[i]
                if type(dat)==tuple:
                    if tp=="loglog":
                        ax.loglog(dat[0],dat[1], color)
                    elif tp=="plot":
                        #print(dat[1])
                        ax.plot(dat[0],dat[1], color)
                else:
                    if tp=="loglog":
                        ax.loglog(dat, color)
                    elif tp=="plot":
                        ax.plot(dat, color)
            else:
                print("there are some plots missing ({}), but it'll be skiped".format(i)) 
    fig.canvas.draw()
    
    



dt = 50/1000
time_range = 5


nt = int(time_range/dt)


fig2,ax2 = plt.subplots(1,1)
plt.ylim(-0.1,5.1)
plt.xlim(0,time_range)
plt.ylabel("Potential",fontsize='14', fontstyle='italic')
plt.xlabel("time, s", fontsize='14', fontstyle='italic')
fig2.set_size_inches((9,6))


ser.flushInput() 
ser.reset_input_buffer()
run = True


for i in range(5):
    ser.reset_input_buffer()
    dat = ser.readline().decode(encoding='UTF-8',errors='strict')
    data = dat.split(' ')
    
toplot2 = [([j*dt for j in range(nt)], np.zeros(nt)) for i in range(len(data))]

pltupdate(fig2,ax2,toplot2)


start_time = time.time()
i=0
while run:
    #ser.reset_input_buffer()
    dat = ser.readline().decode().replace('\r\n','')#encoding='UTF-8',errors='strict'

    #print("data = {} of {}, {}".format(i, nt, data))
    #print("time = {:.3f} <> {:.3f}".format(i*dt,time.time()-start_time))
    
    try:        
        data = dat.split(' ')
        for j in range(len(data)):
            toplot2[j][1][i] = (float(data[j])*5.0/1024)
        pltupdate(fig2,ax2,toplot2)
        i=(i+1)%nt
    
    except: 
        pass
    plt.pause(.000001) 


fig2.show()
ser.close()