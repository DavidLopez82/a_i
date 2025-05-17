import RPi.GPIO as GPIO
from tools import parameters


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

parameters = parameters.Parameters()

GPIO.setup(parameters.v_intractor_pin, GPIO.OUT)
GPIO.setup(parameters.v_extractor_pin, GPIO.OUT)
GPIO.output(parameters.v_intractor_pin, GPIO.HIGH)
GPIO.output(parameters.v_extractor_pin, GPIO.HIGH)


def reset_v_intractor():
    GPIO.output(parameters.v_intractor_pin, GPIO.HIGH)
    parameters.v_intractor_status = False
    parameters.set_fan_i("False")


def set_v_intractor():
    GPIO.output(parameters.v_intractor_pin, GPIO.LOW)
    parameters.v_intractor_status = True
    parameters.set_fan_i("True")


def getStatus_v_intractor():
    return parameters.v_intractor_status


def reset_v_extractor():
    GPIO.output(parameters.v_extractor_pin, GPIO.HIGH)
    parameters.v_extractor_status = False
    parameters.set_fan_e("False")


def set_v_extractor():
    GPIO.output(parameters.v_extractor_pin, GPIO.LOW)
    parameters.v_extractor_status = True
    parameters.set_fan_e("True")


def getStatus_v_extractor():
    return parameters.v_extractor_status


def show_status():
    print("V intractor status: %s - V extractor status: %s" % (parameters.v_intractor_status,
                                                               parameters.v_extractor_status))
