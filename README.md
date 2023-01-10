# openCV with Python Series

OpenCV-Python is an opensource library of Python bindings designed to solve computer vision problems such as image analysis, video analysis, image processing, manipulation and so on.

OpenCV-Python makes use of Numpy, which is a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array structures are converted to and from Numpy arrays. This also makes it easier to integrate with other libraries that use Numpy such as SciPy and Matplotlib.

OpenCV introduces a new set of tutorials which will guide you through various functions available in OpenCV-Python. This guide is mainly focused on OpenCV 2.x version.

in this series i will show you how to load images, draw things on images, analysis, face dectation and recongnition, object detection and recognitiong, track object moving around in an image or a video and so on.


## 01. OpenCV With Python - Introduction & Images
in this introduction and images, we will load an image, display the image, resize the image, rotate the image and save the rotated image.

To start you import the opencv library, after which you load the image by entering the image path, the image name and the mode to load the image. by default cv2 load image in blue green red pattent instead of red blue green.

we have three options to load the image,we can load it in GRAYSCALE, regular color image and without considering transparency