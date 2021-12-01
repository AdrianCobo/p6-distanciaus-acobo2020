
#Libraries
import RPi.GPIO as GPIO
import time
import sys
import threading

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

ledVerde=12
zumbador=16
ledAmarillo=20
ledRojo=21

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

def comportamiento_leds():

    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            if(dist > 30):
                pwm.ChangeDutyCycle(100)
                pwm2.ChangeDutyCycle(0)
                pwm3.ChangeDutyCycle(0)
                pwm4.ChangeDutyCycle(0)
            elif(dist <= 30 and dist > 10):
                pwm.ChangeDutyCycle(0)
                pwm2.ChangeDutyCycle(100)
                pwm3.ChangeDutyCycle(0)
                pwm4.ChangeDutyCycle(50)
            else:
                pwm.ChangeDutyCycle(0)
                pwm2.ChangeDutyCycle(0)
                pwm3.ChangeDutyCycle(100)
                pwm4.ChangeDutyCycle(100)
            time.sleep(0.5)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        sys.exit(0)

if __name__ == '__main__':

    GPIO.setup (ledVerde, GPIO.OUT)
    GPIO.setup (ledAmarillo, GPIO.OUT)
    GPIO.setup (ledRojo, GPIO.OUT)
    GPIO.setup (zumbador, GPIO.OUT)
    pwm = GPIO.PWM(ledVerde,100)
    pwm.start (0)
    pwm2 = GPIO.PWM(ledAmarillo,100)
    pwm2.start (0)
    pwm3 = GPIO.PWM(ledRojo,100)
    pwm3.start (0)
    pwm4 = GPIO.PWM(zumbador,100)
    pwm4.start (0)

    hilo1 = threading.Thread(target=comportamiento_leds)
    hilo1.start()