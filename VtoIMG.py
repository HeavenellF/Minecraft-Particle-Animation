import cv2
import os



video_ext = ['.mp4','.mkv','.mov','.avi','.wmv']
input_dir = '/input'
for ext in video_ext:
    # make a list contain all of the file with specific extension
    video_files = [file for file in os.listdir(input_dir) if file.endswith(ext)]

    # check if the list is not empty
    if video_files:
        # take the first file from the list
        input_video = os.path.join(input_dir, video_files[0])
        break

        
