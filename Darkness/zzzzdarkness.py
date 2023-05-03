import os
import cv2
import numpy as np




def main():
     # Get path of current directory

    path = 'D:\Programming\mycodes\Darkness'   #os.getcwd()
    print(path)

    # Get all the files available in the folder in a list
    dir_list = os.listdir(path)
    print(dir_list)


    i = 0
    j = 3654
    thres = 40


    def writeFiles(image_name,push_image):

        os.chdir("D:\Programming\mycodes\Transformed_images")

       # os.rename(old_name, image_name)

        cv2.imwrite(image_name, push_image)



        os.chdir("D:\Programming\mycodes\Darkness")



    while i < (len(dir_list)):
    
        x = dir_list[i]

        print(path+"/" + x)
       
        # getting image
        image = cv2.imread(path+"/" + x)

        shape = image.shape
        # Use the function from cv2 the image
        mat = np.ones(shape, dtype = 'uint8')*thres
        darker = cv2.subtract(image,mat)
        
        print(f"image{j}")
 
        
   
        #Renaming
        new_jpg = f"vis{j}.jpg"
             
        #os.rename(x, new_jpg)     

        i = i + 1
        j = j + 1

        writeFiles(new_jpg,darker)

        if i >= len(dir_list) - 1:
            break



#run main

if __name__ == "__main__":
    main()