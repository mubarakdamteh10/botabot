# import RPi.GPIO as GPIO          
from time import sleep

# set own pin
in1 = 3
in2 = 5
in3 = 11
in4 = 13
inL = 19
inR = 21
# ena = 7
# enb = 15
# enLR = 23
#temp1= 1 # VCC activate

# set pin 
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(in1,GPIO.OUT)
# GPIO.setup(in2,GPIO.OUT)
# GPIO.setup(in3,GPIO.OUT)
# GPIO.setup(in4,GPIO.OUT)
# GPIO.setup(inL,GPIO.OUT)
# GPIO.setup(inR,GPIO.OUT)
#GPIO.setup(ena,GPIO.OUT)
#GPIO.setup(enb,GPIO.OUT)
#GPIO.setup(enLR,GPIO.OUT)

# set default status pin
# GPIO.output(in1,GPIO.LOW)
# GPIO.output(in2,GPIO.LOW)
# GPIO.output(in3,GPIO.LOW)
# GPIO.output(in4,GPIO.LOW)
# GPIO.output(inL,GPIO.LOW)
# GPIO.output(inR,GPIO.LOW)

#p1 = GPIO.PWM(ena,1000)
#p2 = GPIO.PWM(enb,1000)
#p3 = GPIO.PWM(enLR,1000)
#
#set default frequency = 25 
#p1.start(25) 
#p2.start(25)
#p3.start(25)
#print("\n")
#print("The default speed & direction of motor is LOW & Forward.....")
#print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
#print("\n")    


def forward_motor():
    # GPIO.output(in1,GPIO.LOW)
    # GPIO.output(in2,GPIO.HIGH)
    print("front")
    # GPIO.output(in3,GPIO.HIGH)
    # GPIO.output(in4,GPIO.LOW)
    print("back")

# def backward_motor():
#     GPIO.output(in1,GPIO.HIGH)
#     GPIO.output(in2,GPIO.LOW)
#     print("front motor active")
#     GPIO.output(in3,GPIO.LOW)
#     GPIO.output(in4,GPIO.HIGH)
#     print("back")


def stop_motor():
    # GPIO.output(in1,GPIO.LOW)
    # GPIO.output(in2,GPIO.LOW)
    # GPIO.output(in3,GPIO.LOW)
    # GPIO.output(in4,GPIO.LOW)
    print("stop")

# def direction_right():
#     print("turn rigth")
#     GPIO.output(inL,GPIO.HIGH)
#     GPIO.output(inR,GPIO.LOW)
    
# def direction_left():  
#     print("turn left")
#     GPIO.output(inL,GPIO.LOW)
#     GPIO.output(inR,GPIO.HIGH)

# activate module
# forward_motor()
# stop_motor()
# backward_motor()
# direction_right()
# direction_left()