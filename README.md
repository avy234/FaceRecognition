# Face Recognition

### [YouTube Demonstration](https://youtu.be/ZwrU6ek0up4)

## Description

Real-time face recognition system using Python, OpenCV, and DeepFace.
The program captures video from the webcam and compares each detected face to a predefined reference image. If the face matches, a message is displayed on the video feed in real-time.

Use case: Ideal for personal authentication systems, attendance tracking, or simple facial verification tasks.

### ⚠️Limitation:
- This system can be fooled by static images. If someone obtains a clear photo of the authorized face and presents it to the webcam, the algorithm may incorrectly verify it as a match.
- This makes it insecure for high-stakes authentication where spoofing attacks are a concern. For robust security, consider using liveness detection or multi-factor authentication.

---

## Languages and Utilities Used

- **Python **
- **OpenCV** (for real-time video capture and drawing)
- Threading (for asynchronous face recognition without freezing the video)
- DeepFace (for deep learning-based face verification)

---

## Environments Used

- **Windows 10**
- **VSCode**
- **Python 3.10.11**

---

## Program Walk-through

<p align="center">
Codes: <br/>
<img src="https://i.imgur.com/R4cXUba.png" height="80%" width="80%" alt="Unorganized Files"/>
<br /><br />
  <br/>
<img src="https://i.imgur.com/42iAaCE.png" height="80%" width="80%" alt="Unorganized Files in Folder"/>
<br /><br />
</p>

---

## Output
<p align="center">
Face not looking at the camera: <br/>
<img src="https://i.imgur.com/gF40Bjz.png" height="80%" width="80%" alt="Code1"/>
<br /><br />
Face looking at the camera: <br/>
<img src="https://i.imgur.com/sye0Mz5.png" height="80%" width="80%" alt="Code2"/>
<br /><br />
Face covered: <br/>
<img src="https://i.imgur.com/vdNEe0H.png" height="80%" width="80%" alt="Code3n"/>
</p>

## To Run the Project

1. Make sure you have a webcam.
2. Install the required libraries:

    ```bash
    pip install opencv-python deepface
    ```

3. Place your reference image in the same directory as the script and name it:

    ```text
    reference.jpg
    ```

4. Run the script:

    ```bash
    python face_recognition.py
    ```

5. Press `d` in the window to quit the application.


