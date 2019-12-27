'''
    Requeriments:
        * python -m pip install speechrecognition
        * python -m pip install pyaudio
        * python -m pip install gtts
        * python -m pip install playsound

    Install with ANACONDA
        * conda install -c conda-forge speechrecognition
        * conda install -c anaconda pyaudio
        --- NO FOUND TO gTTS and PlaySound
'''

import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import random

from time import ctime
import time
import webbrowser


r =  sr.Recognizer()

def voice_recognition(ask = False): 
    recognition_result = ''
    with sr.Microphone() as source:
        if ask: bojack_speak(ask) 
        else: bojack_speak('¿Can i Help u?')
        r.adjust_for_ambient_noise(source, duration=1)
        audio_data = r.listen(source)
        try:
            recognition_result = r.recognize_google(audio_data, language="es_CO")
        except sr.UnknownValueError:
            bojack_speak('I\'m sorry, I don\'t listen you!')
        except sr.RequestError():
            bojack_speak('I\'m taking a break! Try later')

    return recognition_result

def recognize_action(action_data):
    action_data = action_data.lower()
    if 'bye' in action_data:
        bojack_speak('See you later, it was a pleasure serving you')
        exit()
    if 'what time is it' in action_data: 
        bojack_speak(f'The current time is: {ctime()}')
    if 'search' in action_data:
        to_search = voice_recognition('¿What would you like to look for??')
        url = f'https://google.com/search?q={to_search}'
        webbrowser.get().open(url)
        bojack_speak(f'This is what I found for: {to_search}')
    if 'find location' in action_data:
        location = voice_recognition('¿What is the location?')
        url = f'https://google.nl/maps/place/{location}/&amp'
        webbrowser.get().open(url)
        bojack_speak(f'This is what I found for: {location}')

def bojack_speak(audio_string=""):
    tts = gTTS(text=audio_string, lang='en')
    audio_file = f'bojack_voice_{random.randint(1,10000)}.mp3' 
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

if __name__ == "__main__":
    time.sleep(1)
    bojack_speak('Initializing voice recognition...')
    bojack_speak('Welcome Jesús Villamarín')
    while True:
        action_data = voice_recognition()
        recognize_action(action_data)