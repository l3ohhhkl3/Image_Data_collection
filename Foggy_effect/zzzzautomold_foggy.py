
import albumentations as A
import cv2
import random
import os


def main():

    #transform object of albumentaion for foggy effext
    transform = A.Compose(
        [A.RandomFog(fog_coef_lower=0.1, fog_coef_upper=0.4, alpha_coef=0.1, p=1)],
    )
    random.seed(7)

    i = 0
    
    j = 3784  #j here means current image number that you want to annotation this will help rename the file

    print(f"current image number is {j}")

    #get all file name from the current director
    all_dir = os.listdir()
    print("fetched dirs")

    #load image using cv2
    def load_img(img_path):
        image = cv2.imread("D:\Programming\mycodes\Foggy_effect"+"\\"+img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    #this function use transform object of albumentation defined above
    def agument(img):
        transformed = transform(image=img)["image"]
        return transformed

    #save files in desired directory
    def writeFiles(image_name,push_image):
        
        os.chdir("D:\Programming\mycodes\Transformed_images")   #get into saving images directory

        cv2.imwrite(image_name, push_image)   # save image

        os.chdir("D:\Programming\mycodes\Foggy_effect")   #get into base images directory


    #loop to call all defined functions
    while i < len(all_dir)-1:
        
        img_name = f"vis{j}.jpg"

        loaded_img = load_img(all_dir[i])

        push = agument(loaded_img)
        print(f"image {j} is agumented")


        writeFiles(img_name,push)
        print(f"image {j} is saved")


        i = i+1
        j = j+1

        

if __name__ == "__main__":
    main()