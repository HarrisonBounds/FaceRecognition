import os 
from datetime import datetime
import cv2 as cv

#dictinoary to link names to id numbers
names = {1: "Harrison"}

face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('lbph_trainer.yml')

test_path = './tester'
image_paths = [os.path.join(test_path, f) for f in os.listdir(test_path)]


for image in image_paths:
    predict_image = cv.imread(image, cv.IMREAD_GRAYSCALE)

    faces = face_detector.detectMultiScale(predict_image, scaleFactor=1.05, minNeighbors=5)

    for (x, y, w, h) in faces:
        print(f"\nAccess requested at {datetime.now()}")

        face = cv.resize(predict_image[y:y+h, x:x+w], (100, 100))
        predicted_id, dist = recognizer.predict(face)

        if predicted_id == 1 and dist <= 95:
            name = names[predicted_id]
            print("{} identifies as {} with distance = {}".format(image, name, round(dist, 1)))
            print(f"\nAccess granted to {name} at {datetime.now()}", file=open('access_log.txt', 'a'))
        else:
            name = 'unknown'
            print(f"{image} is {name}")

        cv.rectangle(predict_image, (x, y), (x+w, y+h), 255, 2)
        cv.putText(predict_image, name, (x+1, y+h-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, 255, 1)
        cv.imshow('ID', predict_image)
        cv.waitKey(2000)
        cv.destroyAllWindows()