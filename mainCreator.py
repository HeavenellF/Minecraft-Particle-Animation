import os
import sys


functions_dir = 'wao'
# functions directory is the directory where all the function located then

# check if the functions directory doesnt exist and force exit
if not os.path.exists(functions_dir):
    print(f'there is no directory called <{functions_dir}')
    print(f'have you run the image-to-particle commands')
    sys.exit(1)

# count how many files(function) in the folder
file_count = len([file for file in os.listdir(functions_dir) if os.path.isfile(os.path.join(functions_dir, file))])
if file_count == 0:
    print(f'there is {file_count} in the folder')
    print('!!force exit!!')
    sys.exit(1)