# Given a directory containing a large amount of images, randomly copy X of them into a new folder

# Imports
import os
import shutil
import random

# Global variables
big_directory = "/home/hsw/unprocessed_images" # Path to directory containing all of the images
sub_directory = "data_labeling/sampled_images" # Path to or name of a new directory
num = 1000 # Amount of images to randomly sample from the big directory
random.seed(20)

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
copy = images[:-200] # Last 200 images are being used as test data
random.shuffle(copy)
images[:-200] = copy

# Looping through the first X images and copying them
filler = 1000000
for i in range(num):
    shutil.copyfile(f"{big_directory}/{images[i]}", f"{sub_directory}/{str(filler + i)}.jpg")
