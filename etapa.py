from datetime import datetime, timedelta
import crtl_clima
from periph import fans, luces
import foto_p
from periph import DHT_Sensor
from tools.etapa_status import etapa_status
from tools.foto_p_status import foto_p_status
from reporte import write_report


class Etapa:

    def __init__(self, fecha_inicio, fecha_fin, tmin_l_on, tmax_l_on, tmin_l_off, tmax_l_off, hmin, hmax, time_l_on,
                 time_delta_l, time_delta_report):
        self.stop_flag = None
        self.pause_flag = None
        self.first_report_flag = True
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.hora_l_on = datetime.now()
        self.hora_l_off = datetime.now()
        self.time_report = datetime.now()
        self.tmin_l_on = tmin_l_on
        self.tmax_l_on = tmax_l_on
        self.tmin_l_off = tmin_l_off
        self.tmax_l_off = tmax_l_off
        self.hmin = hmin
        self.hmax = hmax
        self.time_l_on = time_l_on
        self.time_delta_l = time_delta_l
        self.sensor = DHT_Sensor()
        self.status = etapa_status.not_init
        self.time_delta_report = time_delta_report
        self.date_delta_report = self.time_report + timedelta(minutes=self.time_delta_report)

    def start(self):
        print("Se inicia etapa {0}".format(self.__class__.__name__))
        self.calc_dates_times()
        while (self.fecha_inicio <= datetime.now() <= self.fecha_fin) or self.stop_flag:
            if not self.pause_flag:
                self.status = etapa_status.running
                self.sensor.get_parameters()
                self.sensor.show()
                self.check_t_y_h()
                self.luces_timming()
                fans.show_status()
                luces.show_status_luces()
                self.check_time_report()
                self.show_periodo_etapa()
                self.show_foto_periodo()
                #            foto_p.show_times_fp()

    def pause(self):
        self.pause_flag = True

    def stop(self):
        self.stop_flag = True

    def luces_timming(self):
        status = foto_p_status
        status = foto_p.check(self.hora_l_on, self.hora_l_off)

        if foto_p_status.finish == status:
            self.calc_new_foto_p()
            print("Foto periodo = Terminado")
        elif foto_p_status.running == status:
            # Nada
            print("Foto periodo = En curso")
        elif foto_p_status.waiting == status:
            # Nada
            print("Foto periodo = En espera")

    def check_t_y_h(self):
        crtl_clima.check(self.tmin_l_on, self.tmax_l_on, self.hmin, self.hmax)

    def calc_dates_times(self):
        self.time_report = a = datetime.today()
        self.hora_l_on = a.replace(hour=int(self.time_l_on.hour), minute=0, second=0)
        self.hora_l_off = self.hora_l_on + timedelta(hours=self.time_delta_l)
        if self.hora_l_off <= datetime.now():
            self.hora_l_on = self.hora_l_on + timedelta(days=1)
            self.hora_l_off = self.hora_l_on + timedelta(hours=self.time_delta_l)

    def calc_new_foto_p(self):
        self.hora_l_on = self.hora_l_on + timedelta(hours=24)
        self.hora_l_off = self.hora_l_on + timedelta(hours=self.time_delta_l)

    def check_time_report(self):
        if self.time_report <= datetime.now():  # or self.first_report_flag:
            write_report()
            self.time_report = datetime.now() + timedelta(minutes=self.time_delta_report)
            #            self.first_report_flag = False
        else:
            print("Next report: {}".format(self.time_report.strftime("%b %d %Y %H:%M:%S")))

    def show_periodo_etapa(self):
        print("Fi: {0} Ff: {1}".format(self.fecha_inicio.strftime("%b %d %Y %H:%M:%S"),
                                       self.fecha_fin.strftime("%b %d %Y %H:%M:%S")))

    def show_foto_periodo(self):
        print("FPhi: {0} FPhf: {1}".format(self.hora_l_on.strftime("%b %d %Y %H:%M:%S"),
                                           self.hora_l_off.strftime("%b %d %Y %H:%M:%S")))
