from gtts import gTTS
from playsound import  playsound


def speechtext(text,la):
    mytext=text
    language=la
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save("welcome1.mp3")
    playsound("welcome1.mp3")

    def __del__(self):
        print("call destructor")
