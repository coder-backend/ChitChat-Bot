import speech_recognition as sr
from nltk.chat.util import Chat, reflections
from gtts import gTTS 
import playsound
import wikipedia
import os
from wikiNepali import *
from mysqlDataFetch import *
from googletrans import Translator
nepaliDictionary =[
    ["(नमस्कार|नमस्ते|हेल्लो|Hello|namaste|namaskar)",["नमस्ते, हजुरलाई पाइला टेक्नोलोजीमा स्वागत छ।"]],
    ]

chatNepali = Chat(nepaliDictionary, reflections)
translator = Translator()


def quitingNepali(lang,userName):
    speakNepali("Main",lang)


def speakNepali(speakText, lang):
    myobj = gTTS(text=speakText, lang=lang, slow=False)
    audio_file ="welcome.mp3"
    myobj.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def record_audio_Nepali(userName):
    a=True
    text=''
    while a:
        if(text=="menu" or text =="मेनू" or text=="मेन्यु"):
            a=False
            quitingNepali("ne",userName)
            break
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
                    quitingNepali("ne",userName)
                    break
                else:
                    try:
                        print("Responding...")
                        result = chatNepali.respond(text)
                        print("Bot: "+result)
                        speakNepali(result,"ne")
                    except:
                        translated=translator.translate(text ,src="ne" , dest ='en')
                        result = chatAnswer(translated.text)
                        if result is None:
                            wikiResultSpeak, resultLang = wikiNepali(translated.text)  
                            print("BOT: "+wikiResultSpeak)
                            speakNepali(wikiResultSpeak,resultLang)
                        else:
                            nepalitranslator = translator.translate(result, dest="ne")
                            print("BOT: "+nepalitranslator.text)
                            speakNepali(nepalitranslator.text,"ne")
            except sr.UnknownValueError:
                print("BOT:- I didn't get that")
                speakNepali("मैले बुझिन","ne")
    return 
#############################################End##############################################################
