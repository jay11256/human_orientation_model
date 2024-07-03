# Goal: Turn a directory of images into a video

# Imports
import os
from PIL import Image
import cv2

# Parameters /home/hsw/Desktop/TCQXJ/102
image_directory = "/home/hsw/yolov8_testing/final_product/predict9" # Name of the directory containing the images
video_filename = "/home/hsw/yolov8_testing/103-agnostic-test.mp4" # Filename of the final video result
fps = 1 # Framerate of the video

images = os.listdir(image_directory)
images.sort()
frame = cv2.imread(os.path.join(image_directory, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

i = 1
total = len(images)
for image in images:
    print(f"Processing image {i}/{total}")
    video.write(cv2.imread(os.path.join(image_directory, image)))
    i += 1

cv2.destroyAllWindows()
video.release()

