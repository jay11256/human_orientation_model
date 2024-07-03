# Given a directory containing a large amount of images, randomly copy X of them into a new folder

# Imports
import os
import shutil
import random

# Global variables
big_directory = "205" # Path to directory containing all of the images
sub_directory = "test_frames" # Path to or name of a new directory
num = 200 # Amount of images to randomly sample from the big directory

# Creates directories, prints if they exist already
def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"Folder at {path} already exists.")

# Creating sub directory
create_path(sub_directory)

# Accessing the images in the big directory
images = os.listdir(big_directory)
images.sort()
# random.seed(20)
# random.shuffle(images)

# Looping through the first X images and copying them
filler = 3000000
for i in range(num):
    shutil.copyfile(f"{big_directory}/{images[-1 - i]}", f"{sub_directory}/{str(filler - i)}.jpg")
