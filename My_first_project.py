import pyttsx3
import datetime as dt
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib
import subprocess as sb
import playsound as pss
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
# a=input("Enter your name")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme(name):
    # a=input("Enter your name")
    hour=int(dt.datetime.now().hour)
    if  hour>=0 and hour<12:
        speak(f"Good morning {name}, I am Zaraa, how may i help you")
    elif hour>12 and hour<18:
        speak(f"Good afternoon {name}, I am Zaraa, how may i help you")
    else:
        speak(f"Good evening {name},I am Zaraa how may i help you")
    # speak(f"I am Mikasa, how may i help you")
def takecommand():
    # '''It takes audio from user'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"Keshav said {query}\n")
    except Exception as e:
        print(e)
        print("Can't recognize , say that again please")
        return "None"
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('cashagrawal007@gmail.com','disha9983')
    server.sendmail('cashagrawal007@gmail.com',to,content)
    server.close()

if __name__=='__main__':
    # speak("Keshav")
    wishme("Keshav")
    if 1:
        q=str(takecommand())
        query=q.lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            speak(f"Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'open stack overflow' in query:
            speak(f"Opening stack overflow")
            webbrowser.open("stack overflow.com")
        elif 'open spotify' in query:
            speak(f"Opening spotify")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak(f"Playing music")
            music='C:\\Users\\admin\\Music'
            songs=os.listdir(music)
            print(songs)
            k=os.path.join(music,songs[0])
            pss.playsound(r'C:\Users\admin\Music\Slimshady.mp3')
        elif 'what time' in query:
            strtime=dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        elif 'open code' in query:
            os.startfile("C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",)

        elif 'send mail'  in query:
            try:
                to=input("Enter the email id ")
                speak("What should i mail?")
                content=takecommand()
                sendemail(to,content)
                speak("Your email is sent")
            except Exception as e:
                speak("Sorry I am not able to send email due to some weird reasons")
                print(e)
        elif 'hello how are you' in query:
            speak("Hi sir i am good and i hope you are fine too")
        else:
            speak("Sorry i am not that advanced right now")                
