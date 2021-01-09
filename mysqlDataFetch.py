import mysql.connector
from nltk.tokenize import word_tokenize 
from SimilarSentences import SimilarSentences
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='9840382936',
    database ="chatdata"
)
my_cursor = mydb.cursor()


def chatAnswer(text):
    model = SimilarSentences('model.zip',"predict")
    simple = model.predict(text, 1, "simple")
    simple = simple.replace("[","")
    simple = simple.replace("]","")
    simple = simple.replace('"',"")

    print(simple)
    print(type(simple))
    my_cursor.execute("SELECT answers FROM talkative WHERE questions=%s",(simple,))
    result =my_cursor.fetchall()
    return result[0][0]