from speechtext import *
from zonedata import *
# from controlCar import *

def call_in_functionEn(sound):
    if sound == "data":
        print("show Cactus data")
        return datazone()
    elif sound == "forward":
        # forward_motor()
        print("moving forward")
        # speechtext("กำลังไปข้างหน้า",'th')
        return speechtext("moving forward english function",'en')
    elif sound == "stop":
        # stop_motor()
        print("stop")
        # speechtext("กำลังหยุดรถ",'th')
        return speechtext("stop moving english function",'en')
    else:
        print("out")