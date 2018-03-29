import subprocess
import os
import random
import win32con
import win32gui
from time import ctime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def player():
    subprocess.call(['java','-jar','C:\\Users\\Sunil Aryal\\Desktop\\Our Media Player.jar'],shell=True) 

def play():
    handle = win32gui.FindWindow(None, '')
    win32gui.SetForegroundWindow(handle)
    win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


def maximize():
    Maximize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Maximize, win32con.SW_MAXIMIZE)


def minimize():
    Minimize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)


def listen():
    record = sr.Recognizer()
    with sr.Microphone() as sources:
        print("Please wait. Calibrating microphone...")
        # listen for 5 seconds and create the ambient noise energy level
        record.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
    a = record.listen(sources)
    data = ""

    try:
        data = record.recognize_google(a)

    except sr.UnknownValueError:
        msg = 'Sorry Sir not able to recognize your voice.'
        print(msg)
        speak(msg)

    except sr.RequestError as e:
        print("Recog Error; (0)".format(e))

    return data


def media():
    speak('ok sir')
    speak('starting required applications')
    speak('What do you want me to play for you.')
    any = listen()
    speak('ok sir playing' + any + 'for you')
    os.startfile('' + any + '.mp3')


def shutdown():
    speak('understood sir')
    speak('connecting command prompt')
    speak('shutting down your pc.')
    os.system('shutdown -s')


def gooffline():
    speak('ok sir')
    speak('closing system')
    speak('disconnecting from server')
    speak('going offline')
    quit()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def online():
    speak('ok sir')
    speak('starting all system applications')
    minimize()
    os.startfile('C:\Program Files\Rainmeter\Rainmeter.exe')
    # subprocess.call(['rainmeter'])
    # os.system('start Rainmeter')
    speak('installing all drivers')
    speak('every driver is installed')
    speak('all system have been started')
    speak('now i am online sir')


def recorder():
    print("Please wait. Calibrating microphone...")
    record.adjust_for_ambient_noise(source, duration=5)
    print("Say something!")
    speak('say something')
    a = record.listen(source)
    user = ""

    try:
        user = record.recognize_google(a)

    except sr.UnknownValueError:
        msg = 'Sorry Sir not able to recognize your voice.'
        print(msg)
        speak(msg)

    except sr.RequestError as e:
        print("Recog Error; (0)".format(e))

    return user


def mainfunction(user):
    print(user)
    if user == "ok system":
        online()

    elif user == "song":
        media()

    elif user == "down":
        gooffline()

    elif user == "shutdown":
        shutdown()

    elif user in ['hi', 'hey', 'good']:
        d = random.choice(['hey', 'hi', 'sup'])
        speak(d)
    elif user == 'what time is it':
        print(ctime())
        speak(ctime())
    elif user == 'calculator':
        speak('processing your command')
        os.system('start calc')
        speak("executed successfully")
    elif user == 'notepad':
        speak('processing your command')
        os.system('start notepad')
        speak("Executed successfully")
    elif user == 'minimise':
        minimize()
        speak("minimise successfully")
    elif user == 'maximize':
        maximize()
    elif user == 'shut':
        close()
    elif user == 'cat':
        speak("Opening Our Media Player:")
        player()
        


# time.sleep(1)
speak("Hi Sunil Aryal, what can I do for you?")

if __name__ == "__main__":
    record = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            user = recorder()
            mainfunction(user)
           
