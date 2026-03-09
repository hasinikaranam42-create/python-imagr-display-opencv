Day 2 – Motion Detection using OpenCV

Overview

Today I learned how to detect motion using Python and OpenCV.
The program captures video from the webcam and detects moving objects by comparing frames.

Concepts Learned

- Capturing video using OpenCV
- Converting images to grayscale
- Applying Gaussian Blur to reduce noise
- Frame differencing for motion detection
- Thresholding to highlight movement
- Detecting contours
- Drawing bounding boxes around moving objects

Program Logic

1. Start webcam using OpenCV.
2. Capture the first frame and store it as the reference frame.
3. Convert frames to grayscale.
4. Apply Gaussian blur to remove noise.
5. Compare the current frame with the first frame.
6. Detect differences between frames.
7. Identify moving objects using contours.
8. Draw rectangles around detected motion.

Technologies Used

- Python
- OpenCV
- imutils

Learning Outcome

This project helped me understand the basic workflow of motion detection in computer vision.
