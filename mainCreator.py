import os
import sys


functions_dir = 'wao'
# functions directory is the directory where all the function located then

# check if the functions directory doesnt exist and force exit
if not os.path.exists(functions_dir):
    print(f'there is no directory called <{functions_dir}')
    print(f'have you run the image-to-particle commands')
    sys.exit(1)
