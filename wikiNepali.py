# print("what")
import wikipedia
from googletrans import Translator

def removeWords(text):
    stopwords =['i','me','my','myself','we','our','ours','ourselves','you',"you're","you've","you'll","you'd",'your','yours','yourself','yourselves',
    'he','him','his','himself','she',"she's",'her','hers','herself','it',"it's",'its','itself','they','them',
    'their','theirs','themselves','what','which','who','whom','this','that',"that'll",'these','those','am','is','are','was',
    'were','be',
    'been',
    'being',
    'have',
    'has',
    'had',
    'having',
    'do',
    'does',
    'did',
    'doing',
    'a',
    'an',
    'the',
    'and',
    'but',
    'if',
    'or',
    'because',
    'as',
    'until',
    'while',
    'of',
    'at',
    'by',
    'for',
    'with',
    'about',
    'against',
    'between',
    'into',
    'through',
    'during',
    'before',
    'after',
    'above',
    'below',
    'to',
    'from',
    'up',
    'down',
    'in',
    'out',
    'on',
    'off',
    'over',
    'under',
    'again',
    'further',
    'then',
    'once',
    'here',
    'there',
    'when',
    'where',
    'why',
    'how',
    'all',
    'any',
    'both',
    'each',
    'few',
    'more',
    'most',
    'other',
    'some',
    'such',
    'no',
    'nor',
    'not',
    'only',
    'own',
    'same',
    'so',
    'than',
    'too',
    'very',
    's',
    't',
    'can',
    'will',
    'just',
    'don',
    "don't",
    'should',
    "should've",
    'now',
    'd',
    'll',
    'm',
    'o',
    're',
    've',
    'y',
    'ain',
    'aren',
    "aren't",
    'couldn',
    "couldn't",
    'didn',
    "didn't",
    'doesn',
    "doesn't",
    'hadn',
    "hadn't",
    'hasn',
    "hasn't",
    'haven',
    "haven't",
    'isn',
    "isn't",
    'ma',
    'mightn',
    "mightn't",
    'mustn',
    "mustn't",
    'needn',
    "needn't",
    'shan',
    "shan't",
    'shouldn',
    "shouldn't",
    'wasn',
    "wasn't",
    'weren',
    "weren't",
    'won',
    "won't",
    'wouldn',
    "wouldn't"]
    text= text.lower()
    text=list(text.split(" "))
    finalText =[]

    for i in text:
        if i not in stopwords:
            finalText.append(i)
            
    txt_clean = " ".join(finalText)
    return txt_clean


def wikiNepali(text):
    translator = Translator()

    try:
        translated = translator.translate(text, src='ne', dest='en')
        txt_clean = removeWords(translated.text)
        try:
            search = wikipedia.search(txt_clean, results=1)
            wikipedia.set_lang("ne")
            wikiResult =wikipedia.summary(str(search))
            wikiResult =wikiResult.split("।")
            wikiFinalResult = wikiResult[0]+"। "+wikiResult[-2]
            return wikiFinalResult, "ne"
        except:
            wikipedia.set_lang("en")
            search = wikipedia.search(txt_clean, results=1)
            wikiResult =wikipedia.summary(str(search))
            wikiResult =wikiResult.split(".")
            wikiFinalResult = wikiResult[0]+". "+wikiResult[-2]
            return wikiFinalResult, "en"

    except:
        return "माफ गर्नुहोस्, मैले केहि पनि पाइ न","ne"
