import os
from natsort import natsorted

def main():


    current_path = os.getcwd()
    list_dir = os.listdir(current_path)
    list_dir = natsorted(list_dir)

    i = 0
    j = 3914
    while i < len(list_dir) - 1 :

        name = f"vis{j}.txt"

        os.rename(current_path + "\\" + list_dir[i],name)

        print(f"successfully rename text no.{j} from text no. {list_dir[i]}")

        i = i+1
        j = j+1



if __name__ == "__main__":
    main()