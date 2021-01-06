import face_recognition
import os
import cv2
import pickle
from ChatBot import *
import time
import numpy as np
import speech_recognition as sr


from gtts import gTTS 
import playsound

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')



def speakface(speakText, lang):
    myobj = gTTS(text=speakText, lang=lang, slow=False)
    audio_file ="welcome.mp3"
    myobj.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

finalName="Unknown"
pickle_encoding = open("encoding.pickle","rb")
known_faces =pickle.load(pickle_encoding)

pickle_name = open("names.pickle","rb")
known_names = pickle.load(pickle_name)
print(known_names)

MODEL = "cnn"
TOLERANCE =0.3
face_encodings, face_locations, face_names, process_this_frame = [],[], [], True

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    
    small_frame=cv2.resize(frame, (0,0),fx=0.25,fy=0.25)
    rgb_small_frame =small_frame[:,:,::-1] #BGR--> RGB
    
    if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame, model=MODEL)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names=[]
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_faces, face_encoding)
                name ="Unknown"
                face_distances = face_recognition.face_distance(known_faces, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name= known_names[best_match_index]
                    finalName = name
                    print(finalName)
                speakface("Hey You want to ask anything?","en")
                userDecision = input("Want to go in? ")
                if userDecision=="yes" and finalName!="Unknown":
                    languageChoose(finalName)
                else:
                    pass
    process_this_frame =not process_this_frame
    #cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()





