import os


def main():
    # Get path of current directory

    path = os.getcwd()

    # Get all the files available in the folder in a list
    dir_list = os.listdir(path)

    # iterate through the list of files in the folder
    i = 0
    j = 0

    while i < (len(dir_list)):
        # print(i)

        # print(i <len(dir_list))

        x = dir_list[i]
        y = dir_list[i + 1]

        new_jpg = f"vis{j}.jpg"
        new_txt = f"vis{j}.txt"

        os.rename(x, new_jpg)
        os.rename(y, new_txt)

        i = i + 2
        j = j + 1

        if i >= len(dir_list) - 1:
            break

    print("successfully changed names")


if __name__ == "__main__":
    main()
