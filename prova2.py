#!/usr/bin/python
import RPi.GPIO as GPIO
import subprocess as sp
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(17, False)
GPIO.output(27, False)

tmp=sp.call('clear', shell=True)

def my_callback(channel):
    print('premut 22 '+str(GPIO.input(22)))
    
GPIO.add_event_detect(22, GPIO.FALLING, callback=my_callback)

while (time.time()<time.time()+3000):
    #print str(time.time())
    
    #if GPIO.event_detected(22):
    #    print("premut 22")
    time.sleep(10)
    tmp=sp.call('clear', shell=True)

GPIO.cleanup()
