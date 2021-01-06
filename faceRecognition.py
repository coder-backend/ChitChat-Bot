import face_recognition
import os
import cv2
import pickle
import numpy as np
from ChatBot import *
import time
KNOWN_FACE_DIR = "knownFaces"
TOLERANCE =0.55


print("loading Known faces")

known_faces = []
known_names=  []

for name in os.listdir(KNOWN_FACE_DIR):
    image = face_recognition.load_image_file(f"{KNOWN_FACE_DIR}/{name}")
    encoding = face_recognition.face_encodings(image)[0]

    known_faces.append(encoding)
    known_names.append(os.path.splitext(name)[0])
    
pickle_out = open("encoding.pickle", "wb")
pickle.dump(known_faces, pickle_out)
pickle_out.close()

pickle_name = open("names.pickle","wb")
pickle.dump(known_names, pickle_name)
pickle_name.close()
