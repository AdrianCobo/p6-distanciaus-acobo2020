# P6-DistanciaUS

## (CC-BY-NC-SA) Adrián Cobo Merino

El objetivo de este esta práctica es tener la primera toma de contacto con el sensor de distancia.

### Ejercicio1

En el ejercicio 1 hacemos un programa que apagará o encenderá unos leds en función de la distancia que mida el senor. Se encenderá un led 
rojo si hay un objeto muy cerca del sensor, el amarillo si hay una distancia razonable, y uno verde si el objeto esta bastante lejos.

```python
    dist = distance()
    print ("Measured Distance = %.1f cm" % dist)
    if(dist > 30):
       pwm.ChangeDutyCycle(100)
       pwm2.ChangeDutyCycle(0)
       pwm3.ChangeDutyCycle(0)
    elif(dist <= 30 and dist > 10):
       pwm.ChangeDutyCycle(0)
       pwm2.ChangeDutyCycle(100)
       pwm3.ChangeDutyCycle(0)
    else:
       pwm.ChangeDutyCycle(0)
       pwm2.ChangeDutyCycle(0)
       pwm3.ChangeDutyCycle(100)
```

### Ejercicio2

En el ejercicio 2 hacemos un programa que controlara 3 leds con el mismo comportamiento que en el ejercicio 1, pero además controlara un
zumbador que no pitará si hay bastante distancia al objeto, pitará un poco si está a una distancia moderada, y pitará mucho si el objeto
esta muy cerca 

```python
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
```
**Aclaración:**
En los trozos de programas que hemos puesto, pwm corresponde al led verde,pwm2 corresponde al led amarillo,pwm3 corresponde al led rojo y
pwm4 corresponde al zumbador.

**A destacar:**

Es interesante ver como se puede controlar el brillo de un led usando el mismo metodo que se usa para controlar un zumbador

```python
   
   pwm.ChangeDutyCycle(100)//encendemos el led verde
   pwm4.ChangeDutyCycle(0)//hacemos que no pite el zumbador
   pwm.ChangeDutyCycle(0)//apagamos el led verde
   pwm4.ChangeDutyCycle(100)//hacemos que pite al maximo el zumbador
```

**El esquema de conexión se puede intuir de**

```python
   
   #GPIO Mode (BOARD / BCM)
   GPIO.setmode(GPIO.BCM)

   #set GPIO Pins
   GPIO_TRIGGER = 18
   GPIO_ECHO = 24

   ledVerde=12
   zumbador=16
   ledAmarillo=20
   ledRojo=21
```

Si quieres ver un video de demostracion del ej1, pulsa [aqui](https://drive.google.com/file/d/1LNC3v44mUW_4co6VeOfFKkEQ0VkQVgdz/view?usp=sharing).

Si quieres ver un video de demostracion del ej2, pulsa [aqui](https://drive.google.com/file/d/13HE9hiigJC6TBC2GDbPAyeLynDoZgk1s/view?usp=sharing).

Para la parte del funcionamiento del sensor, me he ayudado del codigo de [esta pagina](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)

Para cualquier duda: <a.cobo.2020@alumos.urjc.es>
