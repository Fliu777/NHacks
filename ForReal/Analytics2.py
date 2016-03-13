"""Examples illustrating the use of plt.subplots().

This function creates a figure and a grid of subplots with a single call, while
providing reasonable control over how the individual plots are created.  For
very refined tuning of subplot creation, you can still use add_subplot()
directly on a new figure.
"""

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime
import matplotlib
import random
import time
from matplotlib.dates import DateFormatter
import matplotlib.image as mpimg


#Arduino
import serial
ser = serial.Serial('COM6', 9600)


touch1,touch2,touch3, accXO,accYO,accZO=map(int,[ser.readline() for _ in range(6)])
tol=10
def curTime():
    return int(round(time.time() * 1000))
last=[0]*10
threshold=500


def check_touch(curTouch, idx):
    global last
    global threshold
    if curTouch == 1:
        print 'TOUCH',idx+1,'IN USE'
        last[idx]=curTime()
	return True
    elif curTime()-last[idx]>threshold:
        print 'TOUCH',idx+1,'NOT IN USE'
	return False
    else:
        print 'TOUCH',idx+1,'NOT IN USE, TIMER'
	return True
        


#Plot
lastUpdate=datetime.datetime.today()

base = datetime.datetime.today()

dates=[datetime.datetime.today()]

plt.close('all')

minutes     = mpl.dates.MinuteLocator()
hours    = mpl.dates.HourLocator()


img=mpimg.imread("map3.png")

lum_img=img[:,:,0]


f, (ax1, ax2, ax3,ax4) = plt.subplots(4, sharex=True, sharey=True,facecolor="white")
ax1=plt.subplot2grid((4,2),(0,0),colspan=1)

#LEGEND
red_patch = mpatches.Patch(color='red', label='Squat Racks')
ora_patch = mpatches.Patch(color='orange', label='Treadmills')
blue_patch = mpatches.Patch(color='blue', label='Bench')
gray_patch = mpatches.Patch(color='gray', label='Free Weights')
plt.legend(handles=[red_patch, ora_patch, blue_patch, gray_patch], loc=1) 
    
ax2=plt.subplot2grid((4,2),(1,0),colspan=1)
ax3=plt.subplot2grid((4,2),(2,0),colspan=1)
ax4=plt.subplot2grid((4,2),(3,0),colspan=1)
ax5=plt.subplot2grid((4,2),(0,1),rowspan=4)

ax5.imshow(lum_img,cmap=plt.cm.gray)


f.tight_layout()
f.subplots_adjust(hspace=0,wspace=0)
generatedValues=[[10] for _ in range(5)]

plt.ion()
plt.show(block=False)

maxPoints=5


diffs=[None]*5
trigger=[False]*5
#Loop

ax4.set_ylim([0,100])
ax3.set_ylim([0,100])
ax2.set_ylim([0,100])
ax1.set_ylim([0,100])
colours=['red','blue','green','orange']

colours=['red','blue','green','orange']
import pylab #Imports matplotlib and a host of other useful modules

radii=[50]*5
ccol=['r','r','r','r','r']

opa=0.5


locations=[(305,600),(595,306),(272,1320),(910,1820), (903, 1325)]
colourQueue=[]


counter=0

while True:
    now=datetime.datetime.today()
    #print now
    diff=now-lastUpdate
    """

"""
    if (diff.seconds>2):
	diff=datetime.datetime.today()
    else:
	continue
    if len(dates)>maxPoints:
	dates=dates[-maxPoints:]
	for idx,val in enumerate(generatedValues):
	    generatedValues[idx]=generatedValues[idx][-maxPoints:]
	    #print len(dates),len(generatedValues[0])
    
    for i in xrange(5):
	if diffs[i] and trigger[i]==False:
	    trigger[i]=True
	    newV=generatedValues[i][-1]+20
	    if i==2:
		newV=generatedValues[1][-1]+20
		generatedValues[1][-1]=(newV)
		generatedValues[2].append(generatedValues[2][-1])
	    else:
		if newV>100:newV=100
		if newV<0:newV=0
		generatedValues[i].append(newV)
	    for j in colourQueue:
		j.remove()
	    colourQueue=[]
	    for j in xrange(5):
		colourQueue.append( pylab.Circle(locations[j], radius=radii[j],  alpha=opa,fc=ccol[j], ec='none'))
		ax5.add_patch(colourQueue[-1])
		
	elif not diffs[i] and trigger[i]==True:
	    newV=generatedValues[i][-1]-20
	    if i==2:
		newV=generatedValues[1][-1]-20
		generatedValues[1][-1]=(newV)
		generatedValues[2].append(generatedValues[2][-1])
	
	    else:
		if newV>100:newV=100
		if newV<0:newV=0
		generatedValues[i].append(newV)
	    trigger[i]=False


	    for j in colourQueue:
		j.remove()
	    colourQueue=[]
	    for j in xrange(5):
		colourQueue.append( pylab.Circle(locations[j], radius=radii[j],  alpha=opa,fc=ccol[j], ec='none'))
		ax5.add_patch(colourQueue[-1])
	else:
	    generatedValues[i].append(generatedValues[i][-1])
	    
	    
    dates.append(now)
    #for idx,val in enumerate(generatedValues):
	#newV=generatedValues[idx][-1]+random.randint(-15,15)
	#if newV<0:
	    #newV=5
	#if newV>100:
	    #newV=random.randint(80,95)
	#generatedValues[idx].append(newV)

    #print dates, generatedValues[0]
    ax1.step(dates,generatedValues[0],linewidth=5, color='red')
    ax1.set_title('Equipment Consumption % March 13, 2016')
    ax2.step(dates,generatedValues[1],linewidth=5, color='orange')
    #ax2.plot_date(dates, y)
    ax3.step(dates,generatedValues[2],linewidth=5, color='blue')
    ax4.step(dates,generatedValues[3],linewidth=5, color='gray')
    # Fine-tune figure; make subplots close to each other and hide x ticks for
    # all but bottom plot.
    #f.subplots_adjust(hspace=0)
    
    #ax4.xaxis.set_major_locator(hours)
    #ax4.xaxis.set_minor_locator(minutes)
    
    #Sets X-axis timer
    majorFormatter = mpl.dates.DateFormatter('%H:%M:%S')
    ax1.xaxis.set_major_formatter(majorFormatter)
    ax2.xaxis.set_major_formatter(majorFormatter)
    ax3.xaxis.set_major_formatter(majorFormatter)
    ax4.xaxis.set_major_formatter(majorFormatter)
       
    
    #ax1.set_xlim([dates[0],dates[-1]])
    #ax2.set_xlim([dates[0],dates[-1]])
    #ax3.set_xlim([dates[0],dates[-1]])
    #ax4.set_xlim([dates[0],dates[-1]])
    
    #Removes 0 Ticks
    ax1.yaxis.get_major_ticks()[0].label1.set_visible(False)
    ax2.yaxis.get_major_ticks()[0].label1.set_visible(False)
    ax3.yaxis.get_major_ticks()[0].label1.set_visible(False)
    
    #Removes Map Axis Labels
    ax5.yaxis.set_visible(False)
    ax5.xaxis.set_visible(False)
    
    #Removes Top 3 chart x-axis
    plt.setp([a.get_xticklabels() for a in f.axes[:-2]], visible=False)
    
    
       


    touch1,touch2,touch3, accX,accY,accZ=map(int,[ser.readline() for _ in range(6)])

    diffs[0]=check_touch(touch1,0)
    diffs[1]=check_touch(touch2,1)
    diffs[2]=check_touch(touch3,2)    

    past=diffs[3]
    #ACCEL SENSOR 12C
    if abs(accX-accXO)>tol:
    	print 'ACCEL IN USE'
    	accXO=accX
    	last[4]=curTime()
	diffs[3]=True
	
    elif abs(accY-accYO)>tol:
    	print 'ACCEL IN USE'
    	accYO=accY
    	last[4]=curTime()
	diffs[3]=True
	
    elif abs(accZ-accZO)>tol:
    	print 'ACCEL IN USE'
    	accZO=accZ
    	last[4]=curTime()
    	diffs[3]=True
	
    elif curTime()-last[4]>threshold:
	print 'ACCEL NOT IN USE'
    	diffs[3]=False
    else:
    	print 'ACCEL IN USE, TIMER'
	print '------------'
    	diffs[3]=True
    
    if diffs[3]!=past:
    
	for j in colourQueue:
	    j.remove()
	colourQueue=[]
	for j in xrange(5):
	    colourQueue.append( pylab.Circle(locations[j], radius=radii[j],  alpha=opa,fc=ccol[j], ec='none'))
	    ax5.add_patch(colourQueue[-1])
    
    for i in xrange(5):
	if diffs[i]:
	    ccol[i]='g'
	    radii[i]*=1.03
	else:
	    ccol[i]='r'
    plt.draw()    
    plt.pause(0.1)
    #time.sleep(0.05)
