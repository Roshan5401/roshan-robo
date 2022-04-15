import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init('sapi5')#sapi5 used to take the voice in the laptop by microsoft
voices=engine.getProperty('voices')#this is to get the voice
engine.setProperty('voice',voices[0].id)#setting voice 0 for male 1 for female

def speak(audio):#this fuction just takes string input and reads it out
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<12:
        speak("Good afternoon sir")
    else:
        speak("Good Evening sir")

    speak("this is roshan how may i help you")

def takeCommand():
    """ take microphone input from the user and return string output"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio =r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        query=query.lower()
        #logic for performing task
        if 'wikipedia' in query:
            speak(f"Searching {query}...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(f"According to wikipedia {result}")
            speak("According to wikipedia")
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='D:\\songs'
            songs=os.listdir(music_dir)
            a=random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[a]))
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
        elif 'open code' in query:
            path="C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(path)
        elif 'roshan' in query:
            speak("yes sir how may i help you")
        elif 'shutdown' in query:
            exit()
        elif 'exit' in query:
            exit()
        elif 'kaise ho' in query:
            speak("mai badhiya hu sir")
        elif 'hello' in query:
            speak('hello sir how are you')
        elif 'good' in query:
            speak('nice to hear it sir')
        elif 'fine' in query:
            speak('nice to hear it sir')
        elif 'bad' in query:
            speak('why so sir')
