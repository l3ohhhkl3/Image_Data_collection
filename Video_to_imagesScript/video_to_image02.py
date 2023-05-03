# Python3 program to extract and save video frame
# using OpenCV Python

#import computer vision module
import cv2

# define the video path
file = 'video01.mp4'

# capture the video
cap = cv2.VideoCapture(file)
i = 0  # frame index to save frames

# extract and save the video frames
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('test_frame_'+str(i)+'.jpg', frame)
        print(f"img{i} saved")
        i+=1
        