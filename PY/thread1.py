import threading
from datetime import datetime
from threading import Thread
import pyttsx3


def time():
    current_date = datetime.now()
    print('现在时间为:'+str(current_date)[0:-10]+'\n')
    return str(current_date)[0:-10]


def speak(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


if __name__ == "__main__":

    # word = str('hello')
    # print(type(word))
    # # threading.Thread(target=time, args=()).start()
    # threading.Thread(target=speak, args=(time()+str(type(word)),)).start()
