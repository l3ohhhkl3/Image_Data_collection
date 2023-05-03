import os
import cv2




def main():
     # Get path of current directory

    path = os.getcwd()
    

    # Get all the files available in the folder in a list
    dir_list = os.listdir(path)


    i = 0
    j = 3524


    def writeFiles(image_name,push_image):

        os.chdir("D:\Programming\mycodes\Transformed_images")

       # os.rename(old_name, image_name)

        cv2.imwrite(image_name, push_image)



        os.chdir("D:\Programming\mycodes\Guassian_blurr_script")





    while i < (len(dir_list)):
    
        x = dir_list[i]

        print(path+"/" + x)
       
        # getting image
        image = cv2.imread(path+"/" + x)

        


        
        
 
        # Use the function from cv2 the image
        Gaussian = cv2.GaussianBlur(image, (7,7),0)
        #cv2.imshow('Gaussian Blurring', Gaussian)
        #cv2.waitKey(0)
        print(f"image{j}")
 
        # Window shown waits for any key pressing event
        #cv2.destroyAllWindows()


        
        
        #Renaming
        new_jpg = f"vis{j}.jpg"
        
        
        #os.rename(x, new_jpg)
        

        i = i + 1
        j = j + 1


        writeFiles(new_jpg,Gaussian)


        if i >= len(dir_list) - 1:
            break









#run main

if __name__ == "__main__":
    main()