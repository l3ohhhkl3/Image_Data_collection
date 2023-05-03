import os
import pandas as pd



def main():


    curr_path =os.getcwd() 
    dir_list = os.listdir(curr_path)

    file_path = curr_path+"\\"

    

    



    


    #a function the get number of annotations in the file that is opened
    def readAnnotations(column):
        person = 0
        vehicle = 0

        for count in column:
            if count == 0:
                person = person + 1
            elif count == 1:
                vehicle = vehicle + 1

        return [person,vehicle]

    def readFaceAnnotations(column):
        Face = 0

        for count in column:
            if count == 0:
                Face = Face + 1
        return [Face]

    
    
    
    #read all the txt file in a loop and call readAnnotation to get number of annotations for each file 

    def readAndPass():
        
        i = 0

        per = 0
        vehi = 0
        Face = 0

        while i < len(dir_list) - 1:
            file = pd.read_csv(file_path+dir_list[i],sep=' ', header=None, names=['annota', 'i','j','k','l'])

            col = file['annota']

            lis = readFaceAnnotations(col)   #readAnnotations(col)
           

            #per  = per + lis[0]
            #vehi = vehi + lis[1]

            Face = Face + lis[0]

            i = i + 1
            print("running")

        #print(f'person ---->{per} vehicle ---->{vehi}')
        print(f"Face annotation = {Face}")


    
    #calling this function
    readAndPass()



    

    


if __name__ == "__main__":
    main()