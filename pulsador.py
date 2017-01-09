#!/usr/bin/python
import MySQLdb 
import subprocess as sp
import RPi.GPIO as GPIO
import time
import datetime

#Preparem la base de dades
db=MySQLdb.connect("localhost","raspi","r4sp1","raspi")
cursor=db.cursor()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

tmp=sp.call('clear',shell=True)
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0
ts=inici=time.time()
st = datetime.datetime.fromtimestamp(inici).strftime('%Y-%m-%d %H:%M:%S')
print ("Iniciat a les "+st)
while (time.time()< ts+5):  #El proces acabara 5 segons despres de la ultima pulsacio
#take a reading
	input = GPIO.input(22)
#if the last reading was low and this one high, print
	if ((not prev_input) and input): #
                ts=time.time()
		sql="INSERT INTO pulsador (instant) VALUES (" + str(ts) + ")"
#		print(sql)
		print(input)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		print("Button pressed at "+str(st))
		GPIO.output(17, True)
		time.sleep(0.1)
		GPIO.output(17, False)
#update previous input
	prev_input = input
#slight pause to debounce
	time.sleep(0.005)
GPIO.cleanup()
final=time.time()
st = datetime.datetime.fromtimestamp(final).strftime('%Y-%m-%d %H:%M:%S')
db.close()
print ("Finalitzat a les "+st)
