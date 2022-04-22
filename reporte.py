import datetime

from tools import parameters

parameter = parameters.Parameters()

def write_report():

    with open('rep/reporte.csv', 'a') as f:
        fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        hora = datetime.datetime.now().strftime("%H:%M:%S")
        temperatura = parameter.temperatura
        humedad = parameter.humedad
        luces = parameter.luces_status
        fan_i = parameter.v_intractor_status
        fan_e = parameter.v_extractor_status
        f.write("{0}; {1}; {2}; {3}; {4}; {5}; {6}\n".format(fecha, hora, temperatura, humedad, luces, fan_i, fan_e))

write_report()