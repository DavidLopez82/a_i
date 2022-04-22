import Adafruit_DHT
from tools import parameters

parameters = parameters.Parameters()


class DHT_Sensor:

    def __init__(self):
        pass

    def get_parameters(self):
        h, t = Adafruit_DHT.read_retry(parameters.DHT1_Sensor, parameters.dht1_pin)
        if parameters.humedad is not None and parameters.temperatura is not None:
            print("Sensor is ok, updating values...")
            parameters.set_humedad(str(h))
            parameters.set_temperatura(str(t))

        else:
            print("Failed to retrieve data from humidity sensor")

        return parameters.humedad, parameters.temperatura

    def show(self):
        print("Temperatura={0}°C  Humedad relativa={1}%".format(parameters.temperatura,
                                                                parameters.humedad))
