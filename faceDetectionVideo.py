#is there a better way to detect faces? (more cascades?)
import cv2 as cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')

cap = cv.VideoCapture(0) #pass in the index of the video device you want to use

#loop that captures each video frame and sees if their is a face in it
while True:
    _, frame = cap.read() #the underscore notes an insignificant variable since we are not reading from a file
    frame = cv.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA) #scaling down the window so the program doesn't slow down with multiple cascades
    fact_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=3)

    for (x, y, w, h) in fact_rects:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'): #compatible with all OS
        break


cap.release()
cv.destroyAllWindows()