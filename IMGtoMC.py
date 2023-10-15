import cv2
import os
import sys
import math
from natsort import natsorted
from PIL import Image


images_dir = 'images'
output_dir = 'wao'
i = 0
dust_size = 0.3
total_pixel = 5000
gap_pixel = 24

# reduce the resolution of a video
def resolution_adjustment(height, width):
    gcd = math.gcd(width,height)
    width = width_ratio = width/gcd
    height = height_ratio = height/gcd
    while True:
        if width * height < total_pixel:
            width = width + width_ratio
            height =  height + height_ratio
        else:
            break
    return height, width

def imgconvertor(file_path):
    global i

    image = cv2.imread(file_path)

    # image resolution adjustment
    height, width, _ = image.shape
    height, width = resolution_adjustment(height, width)

    # resize the image
    resized_image = cv2.resize(image, (int(width),int(height)))

    # Loop through each pixel in the resized image
    height, width, _ = resized_image.shape

    output_dir = 'wao'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f'output Directory <{output_dir}> created')

    with open(f'{output_dir}/heaven{i}.mcfunction', 'w') as file:
        # Redirect stdout to the file
        sys.stdout = file

        for y in range(height):
            for x in range(width):
                pixel = resized_image[y, x]

                blue, green, red = pixel

                blue = round(float(blue) * (1/255),1)
                green = round(float(green) * (1/255),1)
                red = round(float(red) * (1/255),1)
                # if background blue and want to be ignored
                # if blue == 1.0 and green == 0.0 and red == 0.0:
                #     continue
                print(f'particle dust {red} {green} {blue} {dust_size} ~5 ~{round(((width-y)/gap_pixel)-3,2)} ~{round(((x)/gap_pixel),2)}')

    # Reset stdout to its default
    sys.stdout = sys.__stdout__
    i = i + 1

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