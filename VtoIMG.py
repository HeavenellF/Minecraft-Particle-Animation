import cv2
import os
import sys


video_ext = ['.mp4','.mkv','.mov','.avi','.wmv','webm']
video_dir = 'video'

# check if video directory doesnt exist and create one
if not os.path.exists(video_dir):
    os.makedirs(video_dir)
    print(f'video Directory <{video_dir}> created')
    print(f'Please add a Video into <{video_dir}> folder')
    sys.exit(1)

for ext in video_ext:
    # make a list contain all of the file with specific extension
    video_files = [file for file in os.listdir(video_dir) if file.endswith(ext)]

    # check if the list is not empty
    if video_files:
        # take the first file from the list
        video_video = os.path.join(video_dir, video_files[0])
        print(f'video Video : {video_files[0]}')
        break

# exit if there is no video file
if not video_files:
    print(f'Cannot find any Video in Folder <{video_dir}>')
    sys.exit(1)


# check if output directory doesnt exist and create one
output_dir = 'images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f'output Directory <{output_dir}> created')


# split the Video into Images
cap = cv2.VideoCapture(video_video)
desired_fps = 20  # Desired frame rate (20 fps)
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % (int(cap.get(cv2.CAP_PROP_FPS)) // desired_fps) == 0:
        image_filename = os.path.join(output_dir, f'frame_{frame_count // (int(cap.get(cv2.CAP_PROP_FPS)) // desired_fps)}.jpg')
        cv2.imwrite(image_filename, frame)

    frame_count += 1
cap.release()