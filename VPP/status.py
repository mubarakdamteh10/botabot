from speechtext import *
from random import *

def light_status():
    status = [True,False]
    light_value = sample(status,1)
    return(light_value)

def water_status():
    status = [True,False]
    water_value = sample(status,1)
    return(water_value)

def display_value():
    print("light = ",light_status())
    print("water = ",water_status())



