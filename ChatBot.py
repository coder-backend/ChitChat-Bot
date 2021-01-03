
import datetime


import speech_recognition as sr

from nltk.chat.util import Chat, reflections
from gtts import gTTS 
import playsound
import wikipedia
from wiki import *

pairs =[
        ["(hello|namaskar|namaste|hey|hi|hola)",["hey there","namaste","hi there"]],
        ["(.*) your name?",["I am Pari, What's yours?"]],
        ["I am (.*)",["hello %1, Welcome to Naulo!!"]],
        ["(.*) created you",["I was created by Paaila Technology"]],
        
        ["how is the weather in (.*)?",["the weather in %1 is amazing like always"]], 
        ['my name is (.*)', ['hi %1, welcome to Naulo']],
        ['(.*) was (.*)',['%1 is indeed tasty, Thank you for your complement']],
        ['(.*) was bad in (.*)',["We are really sorry for that we will improve next time!!"]],
        ["(.*) help (.*)",["I can help you"]],

]
# # This module is imported so that we can 
# # play the converted audio 
import os 

chat = Chat(pairs, reflections)
def quiting():
    myobj = gTTS(text="Thank You", lang="hi", slow=False)
    audio_file ="welcome.mp3"
    myobj.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
    exit()

def record_audio():
    a=True
    text=''
    while a:
        now = datetime.datetime.now()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ask Me:")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said:- " + text)
                if(text==quit):
                    a=False
                    quiting()
            except sr.UnknownValueError:
                print("I didn't get that")
                myobj = gTTS(text="I didn't get that", lang="hi", slow=False)
                audio_file ="welcome.mp3"
                myobj.save(audio_file)
                playsound.playsound(audio_file)
                os.remove(audio_file)
                if(text==quit):
                    exit()
                record_audio()
        if text!="quit":
            try:
                result = chat.respond(text)
                print("Bot: "+result)
                myobj = gTTS(text=result, lang="hi", slow=False)
                audio_file ="welcome.mp3"
                myobj.save(audio_file)
                playsound.playsound(audio_file)
                os.remove(audio_file)
                if(text==quit):
                    exit()
            except:
                    wikiResultSpeak = wikiSearch(text)
                    myobj = gTTS(text=wikiResultSpeak, lang="hi", slow=False)
                    audio_file ="welcome.mp3"
                    myobj.save(audio_file)
                    print("BOT: "+wikiResultSpeak)
                    playsound.playsound(audio_file)
                    os.remove(audio_file)
                    if(text==quit):
                        exit()
                    record_audio()
                
        else:
            quiting()
            a=False

record_audio()
    