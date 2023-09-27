import cv2
import os
import sys
from natsort import natsorted


images_dir = 'images'
i = 0

def imgconvertor(file_path):
    global i
    
    image = cv2.imread(file_path)
    width = 80
    height = 45
    
    # resize the image
    resized_image = cv2.resize(image, (width,height))

    # Loop through each pixel in the resized image
    height, width, _ = resized_image.shape

    with open(f'heaven{i}.mcfunction', 'w') as file:
        # Redirect stdout to the file
        sys.stdout = file

        for y in range(height):
            for x in range(width):
                pixel = resized_image[y, x]

                blue, green, red = pixel

                blue = round(float(blue) * (1/255),1)
                green = round(float(green) * (1/255),1)
                red = round(float(red) * (1/255),1)

                # Print pixel information
                print(f'particle dust {red} {green} {blue} 1 ~0 ~{round(((width-y)/7),2)} ~{round(((x)/7),2)}')

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