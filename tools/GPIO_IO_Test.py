import RPi.GPIO as GPIO
import time
import Adafruit_DHT


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

print(" ")
print("SETEO DE GPIO")
print(" ")

GPIO.setup(3, GPIO.OUT) #SDA1 PIN 3
GPIO.setup(5, GPIO.OUT) #SLC1 PIN 5
GPIO.setup(10, GPIO.OUT) #RX0 PIN 10
GPIO.setup(8, GPIO.OUT) #TX0 PIN 8
GPIO.setup(18, GPIO.IN) #MOSI PIN 19

print(" ")
print("RESET DE SALIDAS")
print(" ")

GPIO.output(3, GPIO.HIGH)
GPIO.output(5, GPIO.HIGH)
GPIO.output(10, GPIO.HIGH)
GPIO.output(8, GPIO.HIGH)

print("TEST DE RELES")
print(" ")
print("RELE1 ON")

GPIO.output(3, GPIO.LOW)
time.sleep(1)
print("RELE1 OFF")
GPIO.output(3, GPIO.HIGH)
time.sleep(1)
print("RELE2 ON")
GPIO.output(5, GPIO.LOW)
time.sleep(1)
print("RELE2 OFF")
GPIO.output(5, GPIO.HIGH)
time.sleep(1)
print("RELE3 ON")
GPIO.output(10, GPIO.LOW)
time.sleep(1)
print("RELE3 OFF")
GPIO.output(10, GPIO.HIGH)
time.sleep(1)
print("RELE4 ON")
GPIO.output(8, GPIO.LOW)
time.sleep(1)
print("RELE4 OFF")
GPIO.output(8, GPIO.HIGH)

print(" ")
print("SETEANDO SENSOR DE HUMEDAD Y TEMPERATURA DHT11")
print(" ")

DHT1_Sensor = Adafruit_DHT.DHT11
PIN_Sensor = 18

print("RECUPERANDO DATOS DEL SENSOR")
print(" ")

i = 0
while (i <= 5):
    h, t = Adafruit_DHT.read(DHT1_Sensor, PIN_Sensor)
    if t is not None or not "None" and h is not None or not "None":
        print("Sensor is ok, updating values...")
        print("Temp: {0} C  -|-  Hum: {1} %".format(h, t))
        time.sleep(3)
        i = i + 1
    else:
        print("Una poronga tu sensor, no anda")
        print(" ")
        i = 6