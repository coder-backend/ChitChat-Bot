
import datetime


import speech_recognition as sr

from nltk.chat.util import Chat, reflections
from gtts import gTTS 
import playsound
import wikipedia
from wiki import *
import os

from wikiNepali import *

#############################English###############################################################
pairs =[
        ["(hello|namaskar|namaste|hey|hi|hola)",["hey there","namaste","hi there"]],
        ["(.*) your name?",["I am Ginger, What's yours?"]],
        ["I am (.*)",["hello %1, Welcome to Naulo!!"]],
        ["(.*) created you",["I was created by Paaila Technology"]],
        ["how is the weather in (.*)?",["the weather in %1 is amazing like always"]], 
        ['my name is (.*)', ['hi %1, welcome to Naulo']],
        ['(.*) was (.*)',['%1 is indeed tasty, Thank you for your complement']],
        ['(.*) was bad in (.*)',["We are really sorry for that we will improve next time!!"]],
        ["(.*) help (.*)",["I can help you"]],
        ["What is (.*) Restaurant",["Naulo restaurant is the first fully digitized robotic restaurant in South Asia."]],
        ["What is the mission of (.*)",["Attain the best service experience in the food industry with a touch of AI and robotics."]],
        ["What is the goal of (.*)",["To give the best customer experience with the touch of technology and AI"]],
        ["What is your name robot",["My name is Ginger. I was made in Nepal by Paaila Technology."]],
        ["Who is your mother",["My mother is my creator Paaila Technology who built me."]],
        ["What is the concept of (.*)",["Naulo is uniquely positioned with the restaurant industry by enhancing consumers experiences, through digitization and automation."]],
        ["What (.*) the technology used by (.*)",["Naulo uses the state art of technology developed by its parent company Paaila Technology robotics and AI."]],
        ["(What is the function or use of digital tables used at (.*)|What (.*) function of digital tables used at (.*))",["Naulo has positioned a highly interactive digital screen in its menu where customers can choose their food, place an order seamlessly without any human intervention."]],
        ["(What do you do Ginger (.*)|What do you do (.*))",["I serve food to customers in the restaurant."]],
        ["What types of food is served at (.*)",["We serve different cuisines: Nepalese, Indian, Chinese, Japanese, Italian, Pan Asian, Continental and American cuisines."]],
        ["(What is the signature food of (.*)|suggest me|suggest me (.*))",["Sushi to start with, Cheese burst pizza, Rich indian curries, Biryanis, Pan asian curries, Momos, Dimsum, we have different signature food offerings in our menu for different taste palette."]],
        ["What are the different brands owned by (.*)",["Naulo Bakes, Naulo Pan Asian, Naulo Pizzeria and Naulo Restaurant."]],
        ["What is sushi",["A Japanese dish consisting of small balls or rolls of vinegar-flavoured cold rice served with a garnish of vegetables, egg, or raw seafood"]],
        ["What are the types of sushi",["There are different types of sushi: Gunkan maki, Temaki, Nigiri, Hosomaki ,Uramaki"]]
]
# # This module is imported so that we can 
# # play the converted audio 


chat = Chat(pairs, reflections)
def quiting(lang,userName):
    speak("Main",lang)
    languageChoose(userName)


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
        now = datetime.datetime.now()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ask Me:")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said:- " + text)
                if(text=="next"):
                    a=False
                    quiting("hi",userName)
            except sr.UnknownValueError:
                print("BOT:- I didn't get that")
                speak("I didn't get that","hi")
                if(text=="next"):
                    quiting("en",userName)
                record_audio(userName)
            if text!="next":
                try:
                    result = chat.respond(text)
                    print("Bot: "+result)
                    speak(result,"hi")
                    if(text=="next"):
                        quiting("hi",userName)
                except:
                        wikiResultSpeak,resultLang = wikiSearch(text)
                        print("BOT: "+wikiResultSpeak)
                        speak(wikiResultSpeak, resultLang)
                        if(text=="next"):
                            quiting("hi",userName)
                        record_audio(userName)
                
            else:
                quiting("en",userName)
                a=False
###################################End##################################################################

#################################Nepali#################################################################

nepaliDictionary =[
    ["(नमस्कार|नमस्ते|हेल्लो|Hello|namaste|namaskar)",["नमस्ते, हजुरलाई पाइला टेक्नोलोजीमा स्वागत छ।"]],
    ["(.*) नाम के हो",["म परि, अनि हजुर को नि?"]],
    ["म (.*)",["हेल्लो %1 नौलो म हजुरलाइ स्वागत छ ।"]],
    ["मेरो नाम (.*) (.*)",["हेल्लो %1 नौलो म हजुरलाइ स्वागत छ ।"]],
    ["((.*) कस्ले बनाएको हो|(.*) निर्माताको हो)",["म पाइला टेक्नोलोजीद्वारा बनाइएको एउटा रोबोट हूँ।","मलाई पाइला टेक्नोलोजीले निर्माण गरेको हो।"]],
    ]
        # ["how is the weather in (.*)?",["the weather in %1 is amazing like always"]], 
        # ['my name is (.*)', ['hi %1, welcome to Naulo']],
        # ['(.*) was (.*)',['%1 is indeed tasty, Thank you for your complement']],
        # ['(.*) was bad in (.*)',["We are really sorry for that we will improve next time!!"]],
        # ["(.*) help (.*)",["I can help you"]],


# # This module is imported so that we can 
# # play the converted audio 


chatNepali = Chat(nepaliDictionary, reflections)


def record_audio_Nepali(userName):
    a=True
    text=''
    while a:
        now = datetime.datetime.now()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Ask Me:")
            audio = r.listen(source)
            try:
                print("Recognizing...")
                text = r.recognize_google(audio, language='ne-NP')
                print("You said:- " + text)
                if(text=="menu" or text =="मेनू" or text=="मेन्यु"):
                    a=False
                    quiting("ne",userName)
            except sr.UnknownValueError:
                print("BOT:- I didn't get that")
                speak("मैले बुझिन","ne")
                if(text=="menu"):
                    quiting("ne",userName)
                record_audio_Nepali(userName)
            if(text!="menu" or text !="मेनू" or text!="मेन्यु"):
                try:
                    print("Responding...")
                    result = chatNepali.respond(text)
                    print("Bot: "+result)
                    speak(result,"ne")
                    if(text=="बन्द"):
                        quiting("ne",userName)
                except:
                        wikiResultSpeak, resultLang = wikiNepali(text)
                        
                        print("BOT: "+wikiResultSpeak)
                        speak(wikiResultSpeak,resultLang)
                        if(text=="menu" or text =="मेनू" or text=="मेन्यु" ):
                            quiting("ne",userName)
                        record_audio_Nepali(userName)
                
            else:
                quiting("ne",userName)
                a=False

#############################################End##############################################################




def languageChoose(userName):
    lang=''
    condi =True
    while condi:
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
                if(lang=="done"):
                    condi =False
                    speak("See You next Time","en")
                    break
                languageChoose(userName)
    return
#languageChoose(userName)