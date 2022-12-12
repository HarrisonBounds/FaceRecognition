import cv2 as cv
import os

#face detection
face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Could not open video device")

cap.set(3, 640) #frame width
cap.set(4, 480) #frame height

name = input("\nEnter your name: ")
userID = input("Enter ID: ")
print("\nCapturing face, look at the camera now!")

#capture the training images
#if the path is not in the training directory, make a directory called trainer and cd into it
if not os.path.isdir("trainer"):
    os.mkdir("trainer")
os.chdir("trainer")

frame_count = 0 #capture and save video only if face is detected

while True:
    #Capture frame by frame for a total of 30 frames

    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # convert frame to grayscale

    face_rects = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5) #detect faces in an image

    for (x, y, w, h) in face_rects:
        frame_count += 1
        cv.imwrite(str(name) + '.' + str(userID) + '.' + str(frame_count) + '.jpg', gray[y:y+h, x:x+w]) #saves image to the training folder (only the portion with the face)
        cv.rectangle(frame, (x, y), (w+w, y+h), (0, 255, 0), 2)
        cv.imshow('image', frame)
        cv.waitKey(400)
    if frame_count >= 30:
        break

print("\nImage collection completed")
cap.release()
cv.destroyAllWindows()