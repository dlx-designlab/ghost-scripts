# Image Processing
Explore of realtime pre-processing for image detection by neuron cells.
Details in G-Drive's "Ghost/Kenta Progress"

# Setup
It needs
* opencv (cv2)
* numpy
* matplotlib

# filter-test.py
This code loads an image of a duck and performs edge detection using various algorithms such as Sobel filter, Laplacian filter, and Canny filter on the grayscale version of the image. It then applies a bilateral filter to the image and performs edge detection using the same algorithms. The processed images are displayed using OpenCV.
Smoothing before edge detection is common technique to reduce effect of noises.

# realtime-processing.py
This code uses OpenCV to capture video from a camera and perform image processing to display the processed video. The code uses Canny filter and Sobel filter to detect edges in the image, and filters the image using two different kernels. It also allows changing processing parameters based on keyboard input.
