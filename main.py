import time
import serial
import serial.tools.list_ports
# configure the serial port

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math

try:
    ser = serial.Serial(
        port='COM7', # Change as needed
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.EIGHTBITS
    )
    ser.isOpen()
except:
    portlist=list(serial.tools.list_ports.comports())
    print ('Available serial ports:')
    for item in portlist:
       print (item[0])
    exit()
# while 1 :
#     strin = ser.readline()
#     print (strin.decode('utf-8'))

xsize = 120


def data_gen():
    t = data_gen.t
    game_start = False
    while True:
        t += 1
        #val = 100.0 * math.sin(t * 2.0 * 3.1415 / 100.0)
        strin = ser.readline()
        converted = (strin.decode('utf-8'))
        val = float(converted)
        print("temp:", val)
        if val > 25:
            #print("over26")
            if game_start == False:
                plt.title("Temperature GAME")
            game_start = True
        if val > 26 and game_start:
            #print("over27")
            plt.title("Temperature OVER")
            xlinetop = []
            ylinetop = []
            for i in range(0, 400):
                xlinetop.append(i + 1)
                ylinetop.append(val)
            # plot line
            plt.plot(xlinetop, ylinetop)
        if val < 25 and game_start:
            #print("under25")
            plt.title("Temperature UNDER")
            game_start = False
            xlinebot = []
            ylinebot = []
            for i in range(0, 400):
                xlinebot.append(i + 1)
                ylinebot.append(val)
            # plot line
            plt.plot(xlinebot, ylinebot)

        #print("gameflag:", game_start)


        yield t, val


def run(data):
    # update the data
    t, y = data
    if t > -1:
        xdata.append(t)
        ydata.append(y)
        if t > xsize:  # Scroll to the left.
            ax.set_xlim(t - xsize, t)
        line.set_data(xdata, ydata)
    return line,


def on_close_figure(event):
    sys.exit(0)


data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)
line, = ax.plot([], [], lw=3)
ax.set_ylim(18, 28)
ax.set_xlim(0, xsize)
ax.grid()
xdata, ydata = [], []

# create data
xline1 = []
yline1 = []
for i in range(0, 400):
    xline1.append(i)
    yline1.append(26)
# plot line
plt.plot(xline1, yline1)

# create data
xline2 = []
yline2 = []
for i in range(0,400):
    xline2.append(i)
    yline2.append(25)

# plot line
plt.plot(xline2, yline2)

plt.ylabel("Temperature (Celsius)")
plt.xlabel("Time (seconds)")
plt.title("Temperature GAME")

# Important: Although blit=True makes graphing faster, we need blit=False to prevent
# spurious lines to appear when resizing the stripchart.
ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=500, repeat=False)
plt.show()