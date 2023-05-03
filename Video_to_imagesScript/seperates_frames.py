import os
from natsort import natsorted
import shutil



path = os.getcwd()
#print(path)

all_dir = os.listdir()

all_dir = natsorted(all_dir)

original_path = path
target_path = 'D:\Programming\mycodes\Frames_fromVideos'


i = 0 

while i < len(all_dir) - 1:

    original_path = path + '\\'+ all_dir[i]
    shutil.copy(original_path,target_path)
    print(f'moved{i}')
    i= i+3


