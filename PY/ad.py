import win32com.client as win
import pyttsx3
speak = win.Dispatch("SAPI.SpVoice")
speak.Speak("come on")
speak.Speak('现在时间为:'+str(current_date)[0:-10])
