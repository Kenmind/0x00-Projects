import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import time
import os
import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes # pip install pyjokes

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f2')
newVoiceRate = 140
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I hours %M minutes %S seconds")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak("day number")
    speak(date)
    speak("of month number")
    speak(month)
    speak("of the year")
    speak(year)

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 4 and hour <= 11:
        speak("Good morning")
    elif hour >= 12 and hour < 17:
        speak("Good afternoon")
    elif hour >= 17 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")

    speak("Lee at your service.")
    speak("How can I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration = 1)
#        r.pause_threshold = 2
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-uk')
        print(query)

    except Exception as e:
        print(e)
        speak("would you Say that again please...")
    
        return "None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login("simsibe0@gmail.com", "********")
    server.sendmail("simsibe0@gmail.com", to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensor_battery.percent
    speak("The battery is at")
    speak(battery.percent )

def screenshot():
    speak("Please tell me the name of the screenshotfile.")
    name = input("File Name:")
    speak("Please wait while I'm taking the screenshot")
 #   time.sleep(4)
    img = pyautogui.screenshot()
    img.save(f'{name}.png')
    speak("The screenshot has been taken! Now I am ready for the next command please")

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("going offline, please take care of yourself")
            speak("good bye")
            quit()
        elif "wikipedia" in query:
            speak("Searching..")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentence = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send message")

        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown - 1")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir = "F:\musics\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        
        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You told me to remember " + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        
        elif "know" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Screenshot taken")

        elif "cpu" in query:
            cpu()
        
        elif "joke" in query:
            jokes()

        elif "created" in query:
            speak("I was created, I was developed")
        
        elif "family" in query:
            speak("yes. I am the first born in my family and I am patiently waiting for my siblings")
        
        elif "made" in query:
            speak("I was developed by kennedy kalaluka, the mastermind")
            speak("and that makes me smart")

        elif "developed" in query:
            speak("I was developed by Kennedy KALALUKA, the Mastermind")
            speak("And that makes me smart")
        
        elif "Kennedy" in query:
            speak("My developer")
            speak("I love him so much")
        
        elif "you" in query:
            speak("I am Lee, your virtual assistant")
            speak("I am well and good. How are you")
        
        elif "fine" in query:
            speak("That is great to here")

        elif "okay" in query:
            speak("That is great to hear")
        
        elif "sick" in query:
            speak("Too bad dear, maybe you should have some rest or go see a doctor. get well soon")
        
        elif "feel weak" in query:
            speak("Too bad dear")
            speak("maybe you should have some rest or see a doctor")
            speak("get well soon")
