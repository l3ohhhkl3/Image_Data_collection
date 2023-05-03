import cv2
import os
cam = cv2.VideoCapture("vishal.mp4")
currentframe = 0


def writeFiles(name,imge):
    os.chdir("D:\Programming\mycodes\Frames_fromVideos")

    cv2.imwrite(name, imge)

    os.chdir("D:\Programming\mycodes\Video_to_imagesScript")







while(True):
    ret,frame = cam.read()
    
    if ret:
        name = f'D:\Programming\mycodes\Video_to_imagesScript(' + str(currentframe) + ').jpg'
        

        writeFiles(name,frame)
        print(f"image saved{currentframe}")
        currentframe += 1
        
        #print(os.getcwd())
        #cv2.imshow("image",frame)
    else:
        break
cam.release()
cv2.destroyAllWindows()