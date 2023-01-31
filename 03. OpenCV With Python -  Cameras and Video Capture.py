# import libraries
import numpy as np
import cv2

# load the video file
file = cv2.VideoCapture('assets/zuck.mp4')

# loop
while True:
	ret, frame = file.read()
	width = int(file.get(3))
	height = int(file.get(4))

	video = np.zeros(frame.shape, np.uint8)
	smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
	video[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
	video[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_90_CLOCKWISE)
	video[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
	video[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_90_CLOCKWISE)
	
	cv2.imshow('frame', video)

	if cv2.waitKey(1) == ord('e'):
		break


# release the file
file.release()

# to distroy all windows
cv2.destroyAllWindows()