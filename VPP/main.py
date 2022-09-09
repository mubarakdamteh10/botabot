import pyaudio
import speech_recognition as sr
from callfunction import *
from callfunctionEn import *
from time import sleep
from threading import Thread
from controlCar import *


# print(sr.Microphone.list_microphone_names())
def voicestart():

    mic = sr.Microphone(1)
    recog = sr.Recognizer()

    speechtext("เริ่มการทำงาน",'th')
    with mic as source:
        while True:
            print("say something !")
            audio = recog.listen(source,timeout=5.0)
            try:
                voice = recog.recognize_google(audio,language='th')
                print(voice)
                print(call_in_function(voice))
                print("New Command th")
            except:
                continue
            print("out")

        def __del__(self):
            print("call destructor")

voicestart()