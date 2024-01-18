import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import spotify
from spotify.oauth import get_required_scopes
from AppOpener import open
import os

engine = pyttsx3.init('sapi5')  #sapi5 is an API used for taking voice input
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id) #it helps to know what voices i have in pc

def speak(audio):  #function for audio output
    engine.say(audio)
    engine.runAndWait()

def wishMe():  #function for wishing me according to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")   #it will wish good morning

    elif hour>=12 and hour<18:
        speak("Good Afternoon")  #it will wish good afternoon

    else:
        speak("Good Evening")    #it will wish good evening

    speak("I am Jarvis sir,Please tell me how may I help you!")

def takeCommand():  #It takes microphone input from the user and returns string output
    r = sr.Recognizer()  #it helps to recognise audio
    with sr.Microphone() as source:
        print("Listening...")  #it prints listen while listening an audio
        r.pause_threshold = 1  #minimum seconds of speaking audio before we consider thee speaking audio a phrase
        audio = r.listen(source)

    try:
        print("Recognizing...")  #it prints recognize when recognizing an audio
        query = r.recognize_google(audio, language='en-in')  #it helps to recognize in english-india language
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")  #if the audio recognition is unclear it will print this
        return "None"
    return query

def sendEmail(to,content):   #function of send email
    server = smtplib.SMTP('smtp.gmail.com', 587)   #you should allow less secure app for sending email
    server.ehlo()
    server.starttls()
    server.login('paulsubhadeep014@gmail.com', 'subhadeep123')
    server.sendmail('paulsubhadeep014@gmail.com',to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        #logic for executing task based on query
        if 'wikipedia' in query:  #for any query in wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) #details of the query in 2 sentences
            speak("According to wikipedia")
            print(results)    #prints the result of the quwry
            speak(results)    #speaks the result of the query

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open chrome' in query:
            open("chrome")

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            open("spotify")

        elif 'open whatsapp' in query:
            open("Whatsapp")

        #     elif 'play music' in query:
        #      open(spotify)
        #      os.startfile(spotify.playlist)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}\n")

        elif 'email to subhadeep' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "subhadeeppaul111@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend subhadeep bhai,I am not able to send this email")

