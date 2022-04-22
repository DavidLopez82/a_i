from tools import parameters
from periph import fans

parameter = parameters.Parameters()


def check(tmin, tmax, hmin, hmax):

    if tmin <= parameter.temperatura <= tmax:
        print(
            "L/On TMin {0}°C < Ts {1}°C and TMax {2:0.0f}°C > Ts {1:0.0f}°C".format(tmin, parameter.temperatura, tmax))
        fans.reset_v_intractor()
        fans.reset_v_extractor()
    #     break
    # Temperatura por debajo del mínimo
    elif tmin >= parameter.temperatura:
        print("L/On TMin {0}°C > Ts {1:0.0f}°C ".format(tmin, float(parameter.temperatura)))
        fans.reset_v_intractor()
        fans.reset_v_extractor()
    #      break
    # Temperatura por encima del máximo
    elif tmax <= parameter.temperatura:
        print("L/On TMax {0}°C < Ts {1}°C ".format(tmax, parameter.temperatura))
        fans.set_v_intractor()
        fans.set_v_extractor()
