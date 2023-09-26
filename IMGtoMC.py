import cv2
import os
import sys


images_dir = 'images'

# check if images directory doesnt exist and create one
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
    print(f'Images Directory <{images_dir}> created')
    print(f'Please add Images into <{images_dir}> folder')
    sys.exit(1)

# iterate every file in images directory
for file in os.listdir(images_dir):
    file_path = os.path.join(images_dir, file)
    if os.path.isfile(file_path):
        print(f'File found : {file_path}')
