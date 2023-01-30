#import libraries
import numpy as np
import cv2

#load the video file
file = cv2.VideoCapture('assets/zuck.mp4')

#loop
while True:
	ret, frame = file.read()		
	
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) == ord('e'):
		break


file.release()
cv2.destroyAllWindows()