#imports

from datetime import datetime  # Importing the datetime module for handling date and time operations.
from winsound import PlaySound  # Importing PlaySound for playing sounds on a Windows system.
from pip import main  # Importing the main function from pip for handling Python package installations.
import pyttsx3  # Importing pyttsx3 for text-to-speech conversion.
import speech_recognition as sr  # Importing SpeechRecognition for speech recognition capabilities.
import pyaudio  # Importing pyaudio for handling audio input/output operations.
import wikipedia  # Importing the Wikipedia module for accessing Wikipedia content.
import time  # Importing the time module for time-related functions.
import webbrowser  # Importing webbrowser for opening web browsers programmatically.
import os  # Importing the os module for interacting with the operating system.



engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def repeatAfterMe(audio):
    pass


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.now().hour)
    if hour<12:
        speak('good morning sir')
    elif hour>=12 and hour<16: speak('good afternoon sir')
    else: speak('good evening sir')
    speak('I am jarvis, I am here for your assistance')


def takeCommand():
    '''takes voice input from user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1.3
        audio= r.listen(source, timeout=5, phrase_time_limit=10)
        # print("Time Over")  
        
    try:
        print('Recognizing...')
        query=r.recognize_google(audio)
        print(f"You: {query}")
    except Exception as e:
        #print(e)
        #print("Please say that again...")
        return "Sorry! i could'nt understand  you"
    return query

#main program starts here
if __name__=='__main__':
    wishMe()
    while True:
        query= takeCommand().lower()
        chrome_path= ' "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'

        if 'exit' in query: break
        

        elif 'wikipedia' in query:
            speak("searching wikipedia ..")

            query= query.replace("wikipedia",'').replace('look for', '').replace('search for','').replace('search','')
            time.sleep(0.5)
            results= wikipedia.summary(query, sentences= 3)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        
        elif ('what' in query and 'time' in query) or ('tell' in query and 'time' in query):
            strTime= datetime.now().strftime("%H:%M:%S")
            speak(f"It is {strTime[:2]} hours {strTime[2:5]} minutes and {strTime[5:7]} seconds")
            

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open('youtube.com')
            
            
        elif 'open stack overflow' in query or 'open stackoverflow' in query or 'go to stackoverflow' in query or ('open' in query and 'stackoverflow' in query) or ('open'in query and 'stack overflow' in query):
            webbrowser.get(chrome_path).open('stackoverflow.com')
            

        elif 'open code' in query or ('open' in query and 'code' in query):
            code_path = "C:\\Users\Yashu\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        




        break

    speak(" I am off. Have a nice day")
            