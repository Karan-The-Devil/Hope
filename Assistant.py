from logging import exception
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import random
engine = pyttsx3.init('sapi5')
pyttsx3.init()

voices = engine.getProperty('voices')
# print(voices[2].id)
# print(voices)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak(" i am hope, an artificial intiligence. how can i assist you?")

def takecommand():
    '''it takes microphone input from the user and return string inputs'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        speak("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        print("Just wait a second......")
        speak("Just wait a second......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while(True):
        query = takecommand().lower()
        # logic for executing tasks based on query

        if 'search' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
        
        elif "open stackoverflow" in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif "music" in query:
            music_dir = 'D:\\Songs1\\'
            songs = os.listdir(music_dir)
            # a = random.choice(songs)
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif "open vs code" in query:
            codePath = "C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open discord" in query:
            disPath = "C:\\Users\\pc\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe"
            os.startfile(disPath)
        
        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
        
        elif "open bluestacks" in query:
            bluePath = "C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe"
            os.startfile(bluePath)
        
        elif "open github" in query:
            webbrowser.open("https://github.com/")

        elif "open web browser" in query:
            opePath = "C:\\Users\\pc\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            os.startfile(opePath)
        
        elif "open torrent" in query:
            torPath = "C:\\Users\\pc\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
            os.startfile(torPath)

        elif "open zoom" in query:
            zoPath = "C:\\Users\\pc\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoPath)

        elif "open ig" in query:
            webbrowser.open("https://www.instagram.com")
        
        elif "exit" in query:
            speak("Good bye master!")
            break
