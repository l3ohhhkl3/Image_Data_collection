import os
import cv2




def main():
     # Get path of current directory

    path = os.getcwd()
    

    # Get all the files available in the folder in a list
    dir_list = os.listdir(path)


    i = 0
    j = 3394


    def writeFiles(image_name,push_image):

        os.chdir("D:\Programming\mycodes\Transformed_images")

        cv2.imwrite(image_name, push_image)

        os.chdir("D:\Programming\mycodes\Grayscale_Scripts")





    while i < (len(dir_list)):
    
        x = dir_list[i]

        print(path+"/" + x)
       
        # getting image
        image = cv2.imread(path+"/" + x)

        


        
        
 
        # Use the cvtColor() function to grayscale the image
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
        
 
        # Window shown waits for any key pressing event
        #cv2.destroyAllWindows()


        
        
        #Renaming
        new_jpg = f"vis{j}.jpg"
        
        
        os.rename(x, new_jpg)
        

        i = i + 1
        j = j + 1

        writeFiles(new_jpg,gray_image)


        if i >= len(dir_list) - 1:
            break









#run main

if __name__ == "__main__":
    main()