
import datetime
import speech_recognition as sr
from gtts import gTTS 
import playsound
import os
from chatBotEnglish import *
from chatBotNepali import *



def languageChoose(userName):
    lang=''
    condi =True
    while condi:
        if lang=="done":
            condi=False
            break
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Welcome to Naulo "+ userName)
            speak("Welcome to Naulo"+userName,"hi")
            print("Choose a Language")
            speak("Choose a Language","hi")
            
            audio = r.listen(source)
            try:
                print("Recognizing...")
                lang = r.recognize_google(audio)
                if(lang=="done"):
                    condi =False
                    speak("See You next Time","en")
                    break
                print("You said:- " + lang)
                if(lang=="English"):
                    record_audio(userName)
                if(lang=="Nepali"):
                    record_audio_Nepali(userName)
            except sr.UnknownValueError:
                print("BOT:- Choose again")
                speak("Choose again","en")
    return
#languageChoose(userName)