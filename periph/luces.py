import RPi.GPIO as GPIO
from tools import parameters

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
parameters = parameters.Parameters()

GPIO.setup(parameters.luces_pin, GPIO.OUT)
GPIO.output(parameters.luces_pin, GPIO.HIGH)


def set_luces():
    GPIO.output(parameters.luces_pin, GPIO.LOW)
    parameters.luces_status = True
    parameters.set_luces_status("True")


def reset_luces():
    GPIO.output(parameters.luces_pin, GPIO.HIGH)
    parameters.luces_status = False
    parameters.set_luces_status("False")


def get_status_luces():
    return parameters.luces_status


def show_status_luces():
    print("Estado de luces: {0}".format(parameters.luces_status))
