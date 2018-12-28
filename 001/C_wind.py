import math
from decimal import Decimal, ROUND_HALF_UP
deg, dis = map(int,input().split())

deg_list = ["N ", "NNE ", "NE ", "ENE ", "E ", "ESE ", "SE ", "SSE ", "S ", "SSW ", "SW ", "WSW ", "W ", "WNW ", "NW ", "NNW "]

_deg = math.floor(((deg/10) + 11.25) / 22.5)
if _deg >= len(deg_list):
    _deg = 0

_dis = float(dis)

if 0*60 <= _dis and _dis < 0.25*60:
    print("C " + "0")
elif 0.25*60 <= _dis and _dis < 1.55*60:
    print(deg_list[_deg] + "1" )
elif 1.55*60 <= _dis and _dis < 3.35*60:
    print(deg_list[_deg] + "2" )
elif 3.35*60 <= _dis and _dis < 5.45*60:
    print(deg_list[_deg] + "3" )
elif 5.45*60 <= _dis and _dis < 7.95*60:
    print(deg_list[_deg] + "4" )
elif 7.95*60 <= _dis and _dis < 10.75*60:
    print(deg_list[_deg] + "5" )
elif 10.75*60 <= _dis and _dis < 13.85*60:
    print(deg_list[_deg] + "6" )
elif 13.85*60 <= _dis and _dis < 17.15*60:
    print(deg_list[_deg] + "7" )
elif 17.15*60 <= _dis and _dis < 20.75*60:
    print(deg_list[_deg] + "8" )
elif 20.75*60 <= _dis and _dis < 24.45*60:
    print(deg_list[_deg] + "9" )
elif 24.45*60 <= _dis and _dis < 28.45*60:
    print(deg_list[_deg] + "10" )
elif 28.45*60 <= _dis and _dis < 32.65*60:
    print(deg_list[_deg] + "11" )
elif 32.65*60 <= _dis:
    print(deg_list[_deg] + "12" )