import os
import time
from datetime import datetime
import pyttsx3 #text to speech library
import cv2 as cv

#Initialize a pyttsx3 object and assign it the variable "engine"
engine = pyttsx3.init()
engine.setProperty("rate", 145) #rate of the words (WPM)
engine.setProperty("volume", 1.0) #1 is the max volume

#path to pretrained haar casacade classifiers
path = "C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\cv2\\data"

#Loading classifiers and assigining them to variables
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")
#Use addiditonal classifiers to identify profiles, smiles, glasses, etc.

#changing directories to the images folder and assigning the contents to a "contents" variable
os.chdir("images")
contents = sorted(os.listdir())

for image in contents:
    print(f"\nFace detected...{datetime.now()}")
    engine.say("test")
    engine.runAndWait() #halts the programs execution and waits for the audio to finish
    time.sleep(3)

    img_gray = cv.imread(image, cv.IMREAD_GRAYSCALE) #converts the image to grayscale
    h, w = img_gray.shape
    #control - show the image before its face detection and wait for 2000ms
    cv.imshow(f"Face detected {image}", img_gray)
    cv.waitKey(2000)

    face_list = [] #empty list to hold the faces detected
    face_list.append(face_cascade.detectMultiScale(image=img_gray, scaleFactor=1.1, minNeighbors=1))




