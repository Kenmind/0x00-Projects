from typing import IO
import pyttsx3
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'english+f2')
engine.setProperty('rate', 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
speak("What is your name")
while (0 < 1):
    speak("I am never tired of speaking")
    speak("so I wont stop")