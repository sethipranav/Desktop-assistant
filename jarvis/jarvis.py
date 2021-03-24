#from typing import Mapping
import json
import pyttsx3
# import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voice=engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty('voices',voice[1].id)

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("pranavmanishsethi@gmail.com","#yourpasswordhere")  #email has not been sent until a correct password is put. 
    server.sendmail("pranavmanishsethi@gmail.com",to,content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():         #whatever u speak this function return it as a string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please...")
        return "none"
    return query
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("GOod Afternoon!")
    else: 
        speak("Good evening!")

    speak("I am jarvis, how may i help you?")

if __name__=="__main__":
   #speak("pranav is a good boy")
   wishme()
   if 1:
        query=takecommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open big boss 14' in query:
            webbrowser.open("big-boss-vote.in")
        # elif 'stop' in query:
        #     break
        elif 'play music' in query:
            music_dir='E:\\Songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) #song[random.randint(0,len(songs)-1)]
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
        elif 'open code' in query:
            codepath="C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email to pranav' in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to="pranav1382.cse18@chitkara.edu.in"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend, i am not able to send this email")