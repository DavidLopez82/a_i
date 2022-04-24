from datetime import datetime
from tools.foto_p_status import foto_p_status
from tools.parameters import *
from periph import luces

parameter = Parameters()

def check(h_l_on, h_l_off):
    hora_l_on = h_l_on
    hora_l_off = h_l_off
    hora_ = datetime.datetime.now()

    if hora_l_off >= hora_ >= hora_l_on:
        luces.set_luces()
        return foto_p_status.running
    elif not hora_l_off >= hora_ >= hora_l_on:
        luces.reset_luces()
    elif hora_ >= hora_l_off:
        luces.reset_luces()
        return foto_p_status.finish
    else:
        return foto_p_status.waiting


def show_times_fp():
    print("{0} >= {1} >= {2}".format(hora_l_off.strftime("%b %d %Y %H:%M:%S"),
                                     datetime.datetime.now().strftime("%b %d %Y %H:%M:%S"),
                                     hora_l_on.strftime("%b %d %Y %H:%M:%S")))
