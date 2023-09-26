import cv2
import os
import sys


input_dir = 'images'

# check if input directory doesnt exist and create one
if not os.path.exists(input_dir):
    os.makedirs(input_dir)
    print(f'Input Directory <{input_dir}> created')
    print(f'Please add Images into <{input_dir}> folder')
    sys.exit(1)
