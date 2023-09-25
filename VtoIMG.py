import cv2
import os
import sys


video_ext = ['.mp4','.mkv','.mov','.avi','.wmv','webm']
input_dir = 'input'

if not os.path.exists(input_dir):
    os.makedirs(input_dir)
    print(f'Input Directory <{input_dir}> created')

for ext in video_ext:
    # make a list contain all of the file with specific extension
    video_files = [file for file in os.listdir(input_dir) if file.endswith(ext)]

    # check if the list is not empty
    if video_files:
        # take the first file from the list
        input_video = os.path.join(input_dir, video_files[0])
        print(f'Input Video : {video_files[0]}')
        break

# exit if there is no input file
if not video_files:
    print(f'Cannot find any Video in Folder <{input_dir}>')
    sys.exit(1)

        
