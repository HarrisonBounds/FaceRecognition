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
#path = "C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\cv2\\data"

#Loading classifiers and assigining them to variables
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml') #cv.data.haarcascades is the path
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")
#Use addiditonal classifiers to identify profiles, smiles, glasses, etc.

#changing directories to the images folder and assigning the contents to a "contents" variable
os.chdir("images")
contents = sorted(os.listdir())

for image in contents:
    print(f"\nFace detected...{datetime.now()}")
    engine.say("Test")
    engine.runAndWait() #halts the programs execution and waits for the audio to finish
    time.sleep(3)

    img_gray = cv.imread(image, cv.IMREAD_GRAYSCALE) #converts the image to grayscale
    h, w = img_gray.shape
    #control - show the image before its face detection and wait for 2000ms
    cv.imshow(f"Face detected {image}", img_gray)
    cv.waitKey(2000)
    cv.destroyAllWindows()

    face_list = [] #empty list to hold the faces detected
    face_list.append(face_cascade.detectMultiScale(image=img_gray, scaleFactor=1.1, minNeighbors=5))

    print("Searching for eyes...")

    for rect in face_list:
        for (x, y, w, h) in rect:
            cv.rectangle(img_gray, (x,y), (x+w, y+h), (255, 255, 255), 2)
            cv.imshow('Detected Face', img_gray)
            cv.waitKey(2000)
            cv.destroyAllWindows()
            #loop through the coordinates with the face rectangle to find eyes
            rect_eyes = img_gray[y:y + h, x:x + w]
            #call the eye cascade classifier to determine if the subarray is an eye
            eyes = eye_cascade.detectMultiScale(image=rect_eyes, scaleFactor=1.05, minNeighbors=2) #since we are searching a much smaller area, we can use a smaller minNeighbors

        #Retrieve coordinates for the eyes found and draw circles around them
        for (xe, ye, we, he) in eyes:
            print("Eyes detected")
            center = (int(xe + 0.5 * we), int(ye + 0.5 * he))
            radius = int((we + he) / 3)
            cv.circle(rect_eyes, center, radius, 255, 2)
            

            cv.imshow('Detected Face', img_gray)
            cv.waitKey(2000)
            cv.destroyAllWindows()

            #Since we only need to indentift one eye, we can break out of the loop if this is successful
            break






