import os
import cv2 as cv
import numpy as np

face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

train_path = './trainer'
image_paths = [os.path.join(train_path, f) for f in os.listdir(train_path)] #golds directory and file name for each file in the folder

images, labels = [], []

for image in image_paths:
    train_image = cv.imread(image, cv.IMREAD_GRAYSCALE)

    #extract label, name, and frame num from the training image
    label = int(os.path.split(image)[-1].split('.')[1])
    name = os.path.split(image)[-1].split('.')[0]
    frame_num = os.path.split(image)[-1].split('.')[2]
    
    #returns a numpy array
    faces = face_detector.detectMultiScale(train_image)

    for (x, y, w, h) in faces: #loop through the numpy array
        images.append(train_image[y:y+h, x:x+w])
        labels.append(label)
        print(f"\nPreparing training images for {name}.{label}.{frame_num}")

        cv.imshow("Training Image", train_image[y:y+h, x:x+w])
        cv.waitKey(50)

cv.destroyAllWindows()

#actual trianing of the face using LBPH and writing it to a YAML file
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.train(images, np.array(labels))
recognizer.write('lbph_trainer.yml')
print("\nTraining Complete")

