import pyttsx3
from datetime import datetime
current_date = datetime.now( )

print('现在时间为:'+str(current_date)[0:-10]+'\n')

engine = pyttsx3.init()
engine.say('现在时间为:'+str(current_date)[0:-10])
engine.runAndWait()

import win32com.client as win

speak = win.Dispatch("SAPI.SpVoice")
speak.Speak("come on")
speak.Speak('现在时间为:'+str(current_date)[0:-10])
