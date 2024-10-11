# OpenCV Face Recognition System

This project uses OpenCV to implement a face recognition system that captures facial images, trains a recognizer, and performs face recognition from a webcam or saved images.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Capturing Facial Images](#1-capturing-facial-images)
  - [2. Training the Recognizer](#2-training-the-recognizer)
  - [3. Recognizing Faces](#3-recognizing-faces)
- [Directory Structure](#directory-structure)
- [Logging](#logging)
- [License](#license)

## Features

- **Face Detection:** Uses Haar Cascades for detecting faces.
- **Face Recognition:** Utilizes LBPH for recognizing faces from captured images.
- **Real-Time and Static Image Recognition:** Works with both live video feed and static images.
- **User Logging:** Logs access attempts with timestamps.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/opencv-face-recognition.git
   cd opencv-face-recognition
   ```

2. **Set Up a Virtual Environment (Optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *If requirements.txt is not provided, install manually:*

   ```bash
   pip install opencv-python opencv-contrib-python numpy
   ```

## Usage

The system comprises three main scripts:

1. **`capture_faces.py`**: Capture and save facial images for training.
2. **`train_model.py`**: Train the face recognizer using captured images.
3. **`recognize_faces.py`**: Recognize faces from images or webcam feed.

### 1. Capturing Facial Images

Use the wcapture_faces.pyw script to collect facial images for each user.

**Steps:**

1. **Run the Script:**

   ```bash
   python capture_faces.py
   ```

3. **Input User Information:**

   - **Name:** Enter the user's name.
   - **ID:** Enter a unique numerical ID for the user.

4. **Capture Process:**

   - The script will activate the webcam.
   - Look directly into the camera; the system will capture 30 images of your face.
   - Each captured face will be saved in the ./trainer directory in grayscale.

**Example Output:**

``
Enter your name: Harrison
Enter ID: 1

Capturing face, look at the camera now!
Image collection completed
``

### 2. Training the Recognizer

After capturing images, train the recognizer using the wtrain_model.pyw script.

**Steps:**

1. **Ensure Training Images are Available:**

   - Captured images should be in the ./trainer directory with filenames formatted as Name.ID.FrameNumber.jpg (e.g., Harrison.1.1.jpg).

2. **Run the Training Script:**

   ``` bash
   python train_model.py
   ```

3. **Training Process:**

   - The script reads all images from the ./trainer directory.
   - Detects faces and associates them with labels based on the provided IDs.
   - Trains the LBPH face recognizer.
   - Saves the trained model to lbph_trainer.yml.

**Example Output:**

``
Preparing training images for Harrison.1.1
...
Training Complete
``

### 3. Recognizing Faces

Use the wrecognize_faces.pyw script to recognize and identify faces from images in the ./tester directory.

**Steps:**

1. **Prepare Test Images:**

   - Place test images in the ./tester directory.

2. **Run the Recognition Script:**

   ``` bash
   python recognize_faces.py
   ```

3. **Recognition Process:**

   - The script reads images from the ./tester directory.
   - Detects faces and attempts to recognize them using the trained model.
   - If a face is recognized with sufficient confidence, access is granted and logged.
   - Displays the image with a rectangle around the face and the identified name.

**Example Output:**

``
Access requested at 2024-04-27 12:34:56.789012
Harrison.1.1.jpg identifies as Harrison with distance = 50.3
Access granted to Harrison at 2024-04-27 12:34:56.789012
unknown.jpg is unknown
``

**Access Log:**

Access attempts are logged in access_log.txt with timestamps.

## Directory Structure

``
opencv-face-recognition/
├── capture_faces.py
├── train_model.py
├── recognize_faces.py
├── lbph_trainer.yml
├── access_log.txt
├── trainer/
│   ├── Harrison.1.1.jpg
│   ├── Harrison.1.2.jpg
│   └── ...
└── tester/
    ├── test1.jpg
    ├── test2.jpg
    └── ...
``

- **trainer/**: Contains captured facial images for training.
- **tester/**: Contains images used for testing and recognition.
- **lbph_trainer.yml**: The trained LBPH model.
- **access_log.txt**: Logs of access attempts with timestamps.

## Logging

All successful access grants are logged in access_log.txt with the following format:

``
Access granted to Harrison at 2024-04-27 12:34:56.789012
``




