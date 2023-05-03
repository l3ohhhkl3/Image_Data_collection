import os
from PIL import Image
from natsort import natsorted
import shutil



def main():
    path = os.getcwd()
    all_dir = os.listdir()
    all_dir = natsorted(all_dir)
    
    i = 0
    j = 1

    #des_path = r'D:\Programming\mycodes\resized_images'


    def writeFiles(img, j):

        os.chdir(r'D:\Programming\mycodes\resized_images')

        img.save(f'vis{j}.jpg')
        print(f'image {j} saved')

        os.chdir(r'D:\Programming\mycodes\image_resize')



    while i < len(all_dir)-1:
        image = Image.open(all_dir[i], mode= 'r', formats= None )

        resized_img = image.resize((1333,800))


        writeFiles(resized_img,j)


        i = i+1
        j = j+1


if __name__ == '__main__':
    main()