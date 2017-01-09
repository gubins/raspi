import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

## Triem quin pins faran d'entrada i de sortida
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

## Comencem a programar

def blink(cicles,velocitat):
    print "Execucio iniciada: "+str(cicles)+" cicles, a una freqncia de "
    iteracio=0
    print cicles
    while iteracio < str(cicles):
        GPIO.output(17, True)
        GPIO.output(27, False)
        time.sleep(velocitat)
        GPIO.output(17, False)
        GPIO.output(27, True)
        time.sleep(velocitat)
        print iteracio
        iteracio= iteracio + 2
    print "Execucio finalitzada"
    GPIO.cleanup()

cicles = input("Quants cicles?")
freq = input("quina freq?")
velocitat= 1/int(freq)
blink(cicles,velocitat)
