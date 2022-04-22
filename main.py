import plan
from tools.parameters import *
import etapa

# parameter = Parameters()
# e = etapa.Etapa(parameter.c_dias_ec, parameter.tmin_l_on_ec, parameter.tmax_l_on_ec, parameter.tmin_l_off_ec,
#                 parameter.tmax_l_off_ec, parameter.hmin_ec, parameter.hmax_ec, parameter.l_on_ec,
#                 parameter.h_delta_ec)
#
# print("######################################################################")
# e.start()
plan_test = plan.Plan()
plan_test.start_plan()
