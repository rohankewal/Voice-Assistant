import speech_recognition as sr
import webbrowser
import time
import os
import random
import pyttsx3
from time import ctime

r = sr.Recognizer()

speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 173)


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak('Sorry, I did not get that')
        except sr.RequestError:
            alexis_speak('Sorry, my speech service is down')
        return voice_data


def alexis_speak(audio_string):
    print('Computer: ' + audio_string)
    speaker.say(audio_string)
    speaker.runAndWait()


def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is Alexis')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of ' + location)
    if 'what is the weather' in voice_data:
        area = record_audio('What area do you want to know the weather for?')
        zipcode = record_audio('what is the zipcode of the area?')
        url = 'https://www.weatherbug.com/weather-forecast/10-day-weather/' + area + '-' + zipcode
        webbrowser.get().open(url)
        alexis_speak('Here is the weather for ' + area)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
alexis_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
