from datetime import datetime
import win32com.client as win
import pyttsx3
speak = win.Dispatch("SAPI.SpVoice")
speak.Speak("come on")
current_date = datetime.now()
speak.Speak('现在时间为:'+str(current_date)[0:-10])


def speak(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


def time():
    current_date = datetime.now()
    print('现在时间为:'+str(current_date)[0:-10]+'\n')
