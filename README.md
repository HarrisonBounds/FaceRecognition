# FaceRecognition
Builds and improves on face detection code - Now comes with the ability to recognize trained faces

Face detection is possible because humans share similar facial features. These similarities in features are called Haar features (basically the attributes of a digital image). We have man Haar templates that we train or images with to get the best effectiveness rate at identifying faces. 

This "face classifier" algorithm uses the sliding window technique, comparing each of the pixels in the window to the Haar template. For each face detected, the algorithm returns the coordinate where it located the face.