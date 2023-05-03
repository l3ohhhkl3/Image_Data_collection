import os,glob
import cv2
import numpy as np
def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)
path_read=os.getcwd()
dstpath=r'D:\mycodes\Transformed_images'

if __name__=="__main__":
    files=glob.glob(path_read+'/*jpg*')
    for file in files:
        image=cv2.imread(os.path.join(path_read,file))
        gamma = 0.5                                   # change the value here to get different darkness result
        adjusted = adjust_gamma(image, gamma=gamma)
        #The images in the original folder will be darkened,so create a backup and copy the images you want to augment to a separate folder
        cv2.imwrite(os.path.join(dstpath,file),adjusted)
        #The images will be replaced in the original folder. The imwrite function is
        #not working for some but if I remove it the code stops working at all
        #Remember to adjust gamma values as per need