import datetime
import Adafruit_DHT
from configparser import ConfigParser


class Parameters:
    DHT1_Sensor = Adafruit_DHT.DHT11
    __instance = None

    def __new__(cls):
        if Parameters.__instance is None:
            Parameters.__instance = object.__new__(cls)
        return Parameters.__instance

    def __init__(self):

        self.time_delta_report = None
        self.parser = ConfigParser()
        self.temperatura = None
        self.humedad = None
        self.v_intractor_status = None
        self.v_extractor_status = None
        self.luces_status = None
        self.l_on_off = None
        self.dht1_pin = None
        self.v_intractor_pin = None
        self.v_extractor_pin = None
        self.luces_pin = None
        self.auxiliar_2 = 24  # conectado a reles no/nc libres
        self.c_dias_ec = None
        self.c_dias_ev = None
        self.c_dias_ef = None
        self.l_on_ec = None
        self.h_delta_ec = None
        self.l_on_ev = None
        self.h_delta_ev = None
        self.l_on_ef = None
        self.h_delta_ef = None
        self.hmax_ec = None
        self.hmin_ec = None
        self.hmax_ev = None
        self.hmin_ev = None
        self.hmax_ef = None
        self.hmin_ef = None
        self.tmax_l_on_ec = None
        self.tmin_l_on_ec = None
        self.tmax_l_on_ev = None
        self.tmin_l_on_ev = None
        self.tmax_l_on_ef = None
        self.tmin_l_on_ef = None
        self.tmax_l_off_ec = None
        self.tmin_l_off_ec = None
        self.tmax_l_off_ev = None
        self.tmin_l_off_ev = None
        self.tmax_l_off_ef = None
        self.tmin_l_off_ef = None
        self.etapa_f_running = None
        self.etapa_v_running = None
        self.etapa_c_running = None
        self.etapa_f_active = None
        self.etapa_c_active = None
        self.etapa_v_active = None
        self.fecha_inicio_plan = None

        self.read_values()
        self.load_values()

    def set_fecha_inicio_plan(self, fecha_inicio_plan):
        self.parser.set('parametros de cultivo', 'fecha_inicio_plan', str(fecha_inicio_plan))
        self.save_and_update_values()

    def clear_fecha_inicio_plan(self):
        self.parser.set('parametros de cultivo', 'fecha_inicio_plan', 'None')
        self.save_and_update_values()

    def set_fan_i(self, v_fan_i_stat):
        self.parser.set('status', 'v_intractor_status', v_fan_i_stat)
        self.save_and_update_values()

    def set_fan_e(self, v_fan_e_stat):
        self.parser.set('status', 'v_extractor_status', v_fan_e_stat)
        self.save_and_update_values()

    def set_temperatura(self, temperatura):
        if temperatura is not None:
            self.parser.set('status', 'temperatura', temperatura)
            self.save_and_update_values()

    def set_humedad(self, humedad):
        if humedad is not None:
            self.parser.set('status', 'humedad', humedad)
            self.save_and_update_values()

    def set_luces_status(self, l_status):
        self.parser.set('status', 'luces_status', l_status)
        self.save_and_update_values()


    def save_and_update_values(self):
        self.write_values()
        self.read_values()
        self.load_values()

    def load_values(self):
#        try:
        self.temperatura = self.parser.getfloat('status', 'temperatura')
        self.humedad = self.parser.getfloat('status', 'humedad')
        self.v_intractor_status = self.parser.get('status', 'v_intractor_status')
        self.v_extractor_status = self.parser.get('status', 'v_extractor_status')
        self.luces_status = self.parser.getboolean('status', 'luces_status')
        self.l_on_off = self.parser.getboolean('status', 'l_on_off')
        self.time_delta_report = self.parser.getint('status', 'time_report_delta')
        self.dht1_pin = self.parser.getint('io', 'dht1_pin')
        self.v_intractor_pin = self.parser.getint('io', 'v_intractor_pin')
        self.v_extractor_pin = self.parser.getint('io', 'v_extractor_pin')
        self.luces_pin = self.parser.getint('io', 'luces_pin')
        self.auxiliar_2 = 24  # conectado a reles no/nc libres
        self.c_dias_ec = self.parser.get('parametros de cultivo', 'c_dias_ec')
        self.c_dias_ev = self.parser.get('parametros de cultivo', 'c_dias_ev')
        self.c_dias_ef = self.parser.get('parametros de cultivo', 'c_dias_ef')
        self.l_on_ec = datetime.time(self.parser.getint('parametros de cultivo', 'l_on_ec'))
        self.h_delta_ec = self.parser.getint('parametros de cultivo', 'h_delta_ec')
        self.l_on_ev = datetime.time(self.parser.getint('parametros de cultivo', 'l_on_ev'))
        self.h_delta_ev = self.parser.getint('parametros de cultivo', 'h_delta_ev')
        self.l_on_ef = datetime.time(self.parser.getint('parametros de cultivo', 'l_on_fv'))
        self.h_delta_ef = self.parser.getint('parametros de cultivo', 'h_delta_fv')
        self.hmax_ec = self.parser.getfloat('parametros de cultivo', 'hmax_ec')
        self.hmin_ec = self.parser.getfloat('parametros de cultivo', 'hmin_ec')
        self.hmax_ev = self.parser.getfloat('parametros de cultivo', 'hmax_ev')
        self.hmin_ev = self.parser.getfloat('parametros de cultivo', 'hmin_ev')
        self.hmax_ef = self.parser.getfloat('parametros de cultivo', 'hmax_ef')
        self.hmin_ef = self.parser.getfloat('parametros de cultivo', 'hmin_ef')
        self.tmax_l_on_ec = self.parser.getfloat('parametros de cultivo', 'tmax_l_on_ec')
        self.tmin_l_on_ec = self.parser.getfloat('parametros de cultivo', 'tmin_l_on_ec')
        self.tmax_l_on_ev = self.parser.getfloat('parametros de cultivo', 'tmax_l_on_ev')
        self.tmin_l_on_ev = self.parser.getfloat('parametros de cultivo', 'tmin_l_on_ev')
        self.tmax_l_on_ef = self.parser.getfloat('parametros de cultivo', 'tmax_l_on_ef')
        self.tmin_l_on_ef = self.parser.getfloat('parametros de cultivo', 'tmin_l_on_ef')
        self.tmax_l_off_ec = self.parser.getfloat('parametros de cultivo', 'tmax_l_off_ec')
        self.tmin_l_off_ec = self.parser.getfloat('parametros de cultivo', 'tmin_l_off_ec')
        self.tmax_l_off_ev = self.parser.getfloat('parametros de cultivo', 'tmax_l_off_ev')
        self.tmin_l_off_ev = self.parser.getfloat('parametros de cultivo', 'tmin_l_off_ev')
        self.tmax_l_off_ef = self.parser.getfloat('parametros de cultivo', 'tmax_l_off_ef')
        self.tmin_l_off_ef = self.parser.getfloat('parametros de cultivo', 'tmin_l_off_ef')
        self.etapa_f_running = self.parser.getboolean('parametros de cultivo', 'etapa_f_running')
        self.etapa_v_running = self.parser.getboolean('parametros de cultivo', 'etapa_v_running')
        self.etapa_c_running = self.parser.getboolean('parametros de cultivo', 'etapa_c_running')
        self.etapa_f_active = self.parser.getboolean('parametros de cultivo', 'etapa_f_active')
        self.etapa_v_active = self.parser.getboolean('parametros de cultivo', 'etapa_v_active')
        self.etapa_c_active = self.parser.getboolean('parametros de cultivo', 'etapa_c_active')
        self.fecha_inicio_plan = self.parser.get('parametros de cultivo', 'fecha_inicio_plan')
 #       except:
 #           print ("Error en el archivo parametros\n Cheque los parametros de configuración\n")
            

    def read_values(self):
        self.parser.read('source/parameters.ini')


    def write_values(self):
        with open("source/parameters.ini", "w+") as f:
            self.parser.write(f)




