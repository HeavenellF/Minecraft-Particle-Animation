import cv2
import os
import sys
from natsort import natsorted


images_dir = 'images'
i = 0

def imgconvertor(file_path):
    # Resize the image to 64x36 pixels
    global i
    
    image = cv2.imread(file_path)


# check if images directory doesnt exist and create one
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
    print(f'Images Directory <{images_dir}> created')
    print(f'Please add Images into <{images_dir}> folder')
    sys.exit(1)

# iterate every file in images directory
sorted_files = natsorted(os.listdir(images_dir))
for file in sorted_files:
    file_path = os.path.join(images_dir, file)
    if os.path.isfile(file_path):
        print(f'File found : {file_path}')
        imgconvertor(file_path)