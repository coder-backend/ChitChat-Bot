
import datetime


import speech_recognition as sr

from nltk.chat.util import Chat, reflections
from gtts import gTTS 
import playsound
import wikipedia
from wiki import *
import os

#from wikiNepali import *
from mysqlDataFetch import *
pairs =[
        ["(hello|namaskar|namaste|hey|hi|hola)",["hey there","namaste","hi there"]],
        ["how is the weather in (.*)?",["the weather in %1 is amazing like always"]], 
        ["(.*) help (.*)",["I can help you"]],
]


chat = Chat(pairs, reflections)
def quiting(lang,userName):
    speak("Main",lang)


def speak(speakText, lang):
    myobj = gTTS(text=speakText, lang=lang, slow=False)
    audio_file ="welcome.mp3"
    myobj.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def record_audio(userName):
    a=True
    text=''
    while a:
        if(text=="next"):
            a=False
            quiting("hi",userName)
            break
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ask Me:")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                if(text=="next"):
                    a=False
                    quiting("hi",userName)
                    break
                print("You said:- " + text)
                if text!="next":
                    try:
                        result = chat.respond(text)
                        #result = chatAnswer(text)
                        print("Bot: "+result)
                        speak(result,"hi")

                    except:
                        result = chatAnswer(text)
                        if result is None:
                            wikiResultSpeak,resultLang = wikiSearch(text)
                            print("BOT: "+wikiResultSpeak)
                            speak(wikiResultSpeak, resultLang)
                        else:
                            print("Bot: "+result)
                            speak(result,"hi")

                else:
                    quiting("hi",userName)
                    a=False
                    break
            except sr.UnknownValueError:
                print("BOT:- I didn't get that")
                speak("I didn't get that","hi")

    return        