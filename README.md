# openCV with Python Series

OpenCV-Python is an opensource library of Python bindings designed to solve computer vision problems such as image analysis, video analysis, image processing, manipulation and so on.

OpenCV-Python makes use of Numpy, which is a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array structures are converted to and from Numpy arrays. This also makes it easier to integrate with other libraries that use Numpy such as SciPy and Matplotlib.

OpenCV introduces a new set of tutorials which will guide you through various functions available in OpenCV-Python. This guide is mainly focused on OpenCV 2.x version.

in this series i will show you how to load images, draw things on images, analysis, face dectation and recongnition, object detection and recognitiong, track object moving around in an image or a video and so on.


## 01. OpenCV With Python - Introduction & Images

In this introduction and images, we will load an image, display the image, resize the image, rotate the image and save the rotated image.

To start you import the opencv library, after which you load the image by entering the image path, the image name and the mode to load the image. by default cv2 load image in blue green red pattent instead of red blue green.

we have three options to load the image:

'-1' cv2.IMREAD_COLOR: loads a color image. any transparency will be neglected. it is the default flag
 
'0' cv2.IMREAD_GRAYSCALE: loads images in a grayscale mode
 
'1' cv2.IMREAD_UNCHANGED: loads image as such including alpha channel 

After we've succefully loaded this image, next we will display the image with the approprate command, add label and the name of the image we want to show, before loading the image we need to create a way to close the window. To do this, we create waitkey for infinite time and distroy the window after.

We can also rotate the image either clockwise or anti-clockwise direction. To rotate in a clockwise direction we enter this line of code 'img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)'

As we can see from the vizulized image, the image is large, we can resize it to make it visible in all it's form, to do that we will run this line of code to reduiced the size "img = cv2.resize(img, (0,0), fx= 0.6, fy= 0.6)" enter the 'img' feature and the reduction scale for both axis


## 02. OpenCV With Python - Image Fundamentals and Manipulation

In this part we will dive into how image is represented in the computer, how we communicate with the computer and how the computer reads it. If we print out the image the output will show pixel values, we can see how the image is interprinted by the computer, we see a numpy array that's how the computer can relate and how we communicate with the computer. in openCV we use numpy because they are closely related, when we load an image it extract the pixels from the image and load them as numpy array thats why if we check the type function we will get 'numpy.ndarray'.

To get more understanding about our image, we can check the shape of the image, it will show us the number of rolls, colums and channels of the image respectively. The channel here represent the color space of the image, the value that represent each pixels which is Blue, Green and Red in openCV instead of the standard Red, Green and Blue respectively. The value for the pixels ranges between 0 to 255, the value appointed will determine the color this is important because when we manipulate the image all we are doing is modifing the numbers in the ndarray.

The next step in our manipulation process is to cut part of the image and move it to another part of the image, we do this by taking part of the array we want and paste it on the other part of the array we want it to be using numpy array slice. To do this, we copy from row 400 to 700 then within row 400 and 700 we want to copy from 400 to 600. What this will do is copy from our image row 400 to 700 and not including 700 and it will copy all of row 400 to 600 within 400 to 700 after we will paste it into part of the array, we choose the position and make sure it is equall in shape and dimension that we have copy


## 03. Cameras and Video Capture

update soon