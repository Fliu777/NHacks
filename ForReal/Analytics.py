"""Examples illustrating the use of plt.subplots().

This function creates a figure and a grid of subplots with a single call, while
providing reasonable control over how the individual plots are created.  For
very refined tuning of subplot creation, you can still use add_subplot()
directly on a new figure.
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib
import random
import time
#Arduino
import serial
ser = serial.Serial('COM6', 9600)


touch1,touch2,touch3, accXO,accYO,accZO=map(int,[ser.readline() for _ in range(6)])
tol=20
def curTime():
    return int(round(time.time() * 1000))
last=[0]*10
threshold=5000


def check_touch(curTouch, idx):
    global last
    global threshold
    if curTouch == 1:
        print 'TOUCH',idx+1,'IN USE'
        last[idx]=curTime()
    elif curTime()-last[idx]>threshold:
        print 'TOUCH',idx+1,'NOT IN USE'
    else:
        print 'TOUCH',idx+1,'NOT IN USE, TIMER'
        


#Plot
lastUpdate=datetime.datetime.today()

base = datetime.datetime.today()
dates=[datetime.datetime.today()]

plt.close('all')

f, (ax1, ax2, ax3,ax4) = plt.subplots(4, sharex=True, sharey=True,facecolor="red")

generatedValues=[[1] for _ in range(4)]

plt.ion()
plt.show(block=False)

maxPoints=10



#Loop
while True:
	now=datetime.datetime.today()
	#print now
	diff=now-lastUpdate


	if (diff.seconds>2):
		diff=datetime.datetime.today()
	else:
		continue
	if len(dates)>maxPoints:
		dates=dates[-maxPoints:]
		for idx,val in enumerate(generatedValues):
			generatedValues[idx]=generatedValues[idx][-maxPoints:]
	print len(dates),len(generatedValues[0])

	dates.append(now)
	for idx,val in enumerate(generatedValues):
		newV=generatedValues[idx][-1]+random.randint(-15,15)
		if newV<0:
			newV=5
		if newV>100:
			newV=random.randint(80,95)
		generatedValues[idx].append(newV)

	#print dates, generatedValues[0]
	ax1.step(dates,generatedValues[0])
	ax1.set_title('Machine Consumption')
	ax2.step(dates,generatedValues[1])
	#ax2.plot_date(dates, y)
	ax3.step(dates,generatedValues[2])
	ax4.step(dates,generatedValues[3])
	# Fine-tune figure; make subplots close to each other and hide x ticks for
	# all but bottom plot.
	#f.subplots_adjust(hspace=0)

	ax4.set_xlim([dates[0],dates[-1]]);

	plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

	plt.draw()
	touch1,touch2,touch3, accX,accY,accZ=map(int,[ser.readline() for _ in range(6)])

    check_touch(touch1,0)
    check_touch(touch2,1)
    check_touch(touch3,2)    

    #ACCEL SENSOR 12C
    if abs(accX-accXO)>tol:
    	print 'ACCEL IN USE'
    	accXO=accX
    	last[4]=curTime()
    elif abs(accY-accYO)>tol:
    	print 'ACCEL IN USE'
    	accYO=accY
    	last[4]=curTime()

    elif abs(accZ-accZO)>tol:
    	print 'ACCEL IN USE'
    	accZO=accZ
    	last[4]=curTime()
	elif curTime()-last[4]>threshold:
    	print 'ACCEL NOT IN USE'
    else:
    	print 'ACCEL IN USE, TIMER'
	print '------------'

	plt.pause(0.1)
	#time.sleep(0.05)
