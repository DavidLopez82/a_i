from etapa import *
from tools.parameters import *


class Plan:

    parameter = Parameters()

    def __init__(self):
        self.etapa_c = None
        self.etapa_v = None
        self.etapa_f = None
        self.date_inicio_ec = datetime.datetime.now()
        self.date_fin_ec = datetime.datetime.now()
        self.date_inicio_ev = datetime.datetime.now()
        self.date_fin_ev = datetime.datetime.now()
        self.date_inicio_ef = datetime.datetime.now()
        self.date_fin_ef = datetime.datetime.now()
        self.ini_time_plan()
        self.init_objects()

    def init_objects(self):
        print ("Se inician los objetos etapa....")
        self.etapa_c = Etapa(self.date_inicio_ec, self.date_fin_ec, self.parameter.tmin_l_on_ec, self.parameter.tmax_l_on_ec,
                        self.parameter.tmin_l_off_ec, self.parameter.tmax_l_off_ec, self.parameter.hmin_ec,
                        self.parameter.hmax_ec, self.parameter.l_on_ec, self.parameter.h_delta_ec, self.parameter.time_report_delta)
        self.etapa_v = Etapa(self.date_inicio_ev, self.date_fin_ev, self.parameter.tmin_l_on_ev, self.parameter.tmax_l_on_ev,
                        self.parameter.tmin_l_off_ev, self.parameter.tmax_l_off_ev, self.parameter.hmin_ev,
                        self.parameter.hmax_ev, self.parameter.l_on_ev, self.parameter.h_delta_ev, self.parameter.time_report_delta)
        self.etapa_f = Etapa(self.date_inicio_ef, self.date_fin_ef, self.parameter.tmin_l_on_ef, self.parameter.tmax_l_on_ef,
                        self.parameter.tmin_l_off_ef, self.parameter.tmax_l_off_ef, self.parameter.hmin_ef,
                        self.parameter.hmax_ef, self.parameter.l_on_ef, self.parameter.h_delta_ef, self.parameter.time_report_delta)

    def ini_time_plan(self):
        print("Se inician las variables dates...")
        self.date_inicio_ec = datetime.datetime.now()
        self.date_fin_ec = datetime.datetime.now()
        self.date_inicio_ev = datetime.datetime.now()
        self.date_fin_ev = datetime.datetime.now()
        self.date_inicio_ef = datetime.datetime.now()
        self.date_fin_ef = datetime.datetime.now()
        if self.parameter.etapa_c_active and self.parameter.etapa_v_active and self.parameter.etapa_f_active:
            if self.parameter.fecha_inicio_plan == "":
                self.date_inicio_ec = datetime.datetime.now()
            else:
                self.date_inicio_ec = datetime.datetime.fromisoformat(self.parameter.fecha_inicio_plan[0:10])
            self.parameter.set_fecha_inicio_plan(self.date_fin_ec)
            self.date_fin_ec = self.date_inicio_ec + timedelta(days=int(self.parameter.c_dias_ec))
            self.date_inicio_ev = self.date_fin_ec
            self.date_fin_ev = self.date_inicio_ev + timedelta(days=int(self.parameter.c_dias_ev))
            self.date_inicio_ef = self.date_fin_ev
            self.date_fin_ef = self.date_inicio_ef + timedelta(days=int(self.parameter.c_dias_ef))
        elif not self.parameter.etapa_c_active and self.parameter.etapa_v_active and self.parameter.etapa_f_active:
            if self.parameter.fecha_inicio_plan == "":
                self.date_inicio_ev = datetime.datetime.now()
            else:
                self.date_inicio_ev = datetime(self.parameter.fecha_inicio_plan)
            self.parameter.set_fecha_inicio_plan(self.date_fin_e)
            self.date_inicio_ev = datetime.datetime.now()
            self.date_fin_ev = self.date_inicio_ev + timedelta(days=int(self.parameter.c_dias_ev))
            self.date_inicio_ef = self.date_fin_ef
            self.date_fin_ef = self.date_inicio_ef + timedelta(days=int(self.parameter.c_dias_ef))
        elif not self.parameter.etapa_c_active and not self.parameter.etapa_v_active and self.parameter.etapa_f_active:
            if self.parameter.fecha_inicio_plan == "":
                self.date_inicio_ef = datetime.datetime.now()
            else:
                self.date_inicio_ef = datetime(self.parameter.fecha_inicio_plan)
            self.parameter.set_fecha_inicio_plan(self.date_fin_e)
            self.date_inicio_ef = datetime.datetime.now()
            self.date_fin_ef = self.date_inicio_ef + timedelta(days=int(self.parameter.c_dias_ef))

    def start_plan(self):
        print("Se inicia plan...")
        if self.parameter.etapa_c_active and self.date_fin_ec > datetime.datetime.now():
            if self.etapa_v.status == etapa_status.not_init or etapa_status.finish and \
                    self.etapa_f.status == etapa_status.not_init or etapa_status.finish:
                self.etapa_c.start()
        elif self.parameter.etapa_v_active and self.date_fin_ev > datetime.datetime.now():
            if self.etapa_c.status == etapa_status.not_init or etapa_status.finish and \
                    self.etapa_f.status == etapa_status.not_init or etapa_status.finish:
                self.etapa_v.start()
        elif self.parameter.etapa_f_active and self.date_fin_ef > datetime.datetime.now():
            if self.etapa_c.status == etapa_status.not_init or etapa_status.finish and \
                    self.etapa_v.status == etapa_status.not_init or etapa_status.finish:
                self.etapa_f.start()
        print("Se termina plan...")
