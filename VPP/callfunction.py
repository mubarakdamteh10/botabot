from speechtext import *
from zonedata import *
from controlCar import *

def call_in_function(sound):
    if sound == "ดูข้อมูล":
        print("show Cactus data")
        return datazone()
    elif sound == "เดินหน้า":
        forward_motor()
        print("moving forward")
        speechtext("กำลังไปข้างหน้า",'th')
        return speechtext("moving forward",'en')
    elif sound == "หยุดรถ":
        stop_motor()
        print("stop moving")
        speechtext("กำลังหยุดรถ",'th')
        return speechtext("stop moving",'en')
    else:
        print("out")