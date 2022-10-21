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
path = "C:\Users\Owner\AppData\Local\Programs\Python\Python39\lib\site-packages\cv2\data"

#Loading classifiers and assigining them to variables
face_cascade = cv.CascadeClassifier(path + "haarcasacde_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier(path + "haarcascade_eye.xml")
#Use addiditonal classifiers to identify profiles, smiles, glasses, etc.

#changing directories to the images folder and assigning the contents to a "contents" variable
os.chdir("images")
contents = sorted(os.listdir())





