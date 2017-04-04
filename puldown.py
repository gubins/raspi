#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
'''
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(22, GPIO.BOTH)
def my_callback(22):
        GPIO.output(17, GPIO.input(22))
GPIO.add_event_callback(22, my_callback)
'''

GPIO.setup(22,GPIO.IN)
if GPIO.input(22):
    print('Input was HIGH')
else:
    print('Input was LOW')
#To wait for a button press by polling in a loop:
while GPIO.input(22) == GPIO.LOW:
    time.sleep(0.01) 