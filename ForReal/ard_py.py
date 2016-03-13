import serial
import subprocess
child=subprocess.Popen(['python','Analytics.py'],stdin=subprocess.PIPE)
ser = serial.Serial('COM6', 9600)

import time

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
        child.communicate("dawg")
        print 'TOUCH',idx+1,'IN USE'
        last[idx]=curTime()
    elif curTime()-last[idx]>threshold:
        print 'TOUCH',idx+1,'NOT IN USE'
    else:
        print 'TOUCH',idx+1,'NOT IN USE, TIMER'
        
while True:
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
