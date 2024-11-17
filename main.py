import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


# pip install pocketsphinx
recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "75d94d09eb3f48e48e75173459d1551f"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text=text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def aiprocess(command):
    client = OpenAI(
    api_key="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"
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named  Jarvis skilled in general tasks like google and alexa. Give short responses"},
            {"role": "user", "content": command},
        ]
    )

    return completion.choices[0].message

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open stackoverflow" in c.lower():
        speak("Opening StackOverflow")
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in c.lower():
        speak("Opening Github")
        webbrowser.open("https://github.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in c.lower():
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open reddit" in c.lower():
        speak("Opening Reddit")
        webbrowser.open("https://www.reddit.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split("play")[1].strip()
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # parse the JSON response
            data = r.json()
            
            # extract the articles from the response
            articles = data.get("articles", [])
            # print the titles of the articles
            for article in articles:
                speak(article["title"])
    else:
        # let openai handle the command
        output = aiprocess(c)
        speak(output.content)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognising...")
        try: 
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("yeah")
                # listen for the command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error: {0}".format(e))