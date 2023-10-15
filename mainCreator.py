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

i = 0
t = 0
with open('main.mcfunction', 'w') as file:
    sys.stdout = file
    # thic command is to auto loop
    # print(f'scoreboard players add frame step_counter 1')
    print(f'execute if score frame step_counter matches {file_count}.. run scoreboard players set frame step_counter 0')
    while i <= file_count :
        # print(f'schedule function heaven:wao/heaven{i} {t}t')

        # print(f'execute as @a[scores={{step_counter={i}}}] run function heaven:wao/heaven{i}')
        # print(f'scoreboard players add @a[scores={{step_counter={i}}}] step_counter 1')

        print(f'execute if score frame step_counter matches {i}..{i} run function heaven:{functions_dir}/heaven{i}')

        i = i + 1
        t = t + 1

    sys.stdout = sys.__stdout__