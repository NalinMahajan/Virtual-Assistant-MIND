import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import globalvariables as gv
import webbrowser
from selenium import webdriver
import sys
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak('Good Morning')
    elif(hour>=12 and hour < 18):
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am Mind!,How may I help you Neil')

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en_in')
        print(f"User said:{query}\n")
    except Exception as e:
        return "None"
    return query
def takecommand_2():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\nSay it Now")
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en_in')
        print(f"User said:{query}\n")
    except Exception as w:
        speak("Didn't get it")
        return "None"
    return query
def takecommand_3():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\n")
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en_in')
    except Exception as w:
        return "None"
    return query
def my_name():
    speak(f"Your name is{gv.myname}!.What can I do for you Sir.")
def changename():
    speak("Share me your ID number")
    query=takecommand_2().lower()
    if query== gv.myid :
        speak("Your ID is Correct!.Go for your new name")
        speak('Please call your New Name')
        query=takecommand_2().lower()
        gv.myname=f"{query}"
        speak(f"Your new name is{gv.myname}.What can I do for you...\n")
    else:
        speak("Your Given ID number is wrong.You can't access that setting")
def wake_up():
    speak("I'm Mind! I'm ready for my work")
    takecommand().lower()
def sleep():
    while True:
        query=takecommand_3().lower()
        if 'wake up' in query:
            wake_up()
def offline():
    speak("Thankyou for using me. I am going offline")
    sys.exit()


if __name__ == "__main__" :
    wishme()
    while True:

        query=takecommand().lower()
        if 'hey mind' in query:
            speak("I'm Mind!,What can I do for you Sir")
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace("wikipedia","")
            try:
                results=wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as w:
                speak("I didn't get anything on Wikipedia")
        if 'change my name' in query:
            changename()
        if'what is my name' in query:
            my_name()
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'open chrome' in query:
            chromedriver = "C:\\Users\\hp\\Desktop\\chromedriver"
            driver=webdriver.Chrome(executable_path="C:\\Users\\hp\\Desktop\\chromedriver")
            driver.get("https://www.google.com")
            query=takecommand_2().lower()
            if "maximize" in query:
              driver.maximize_window()
            elif " minimise" or "minimize" in query:
                driver.minimize_window()
            else:
                pass
        if 'wake up' in query:
            wake_up()
        if 'sleep mode' in query:
            sleep()
        if 'go offline' in query:
            offline()

            
            