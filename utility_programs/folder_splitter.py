# Creates all the directories neccesary for a dataset
# Splits 2 directories (images and labels) into train, valid, and test directories according to a specific ratio

# Imports
import os
import shutil
import random

# Parameters
dataset_dir = "datasets" # Name of the datasets directory
dataset_name = "500" # Name of the dataset 
train_ratio, valid_ratio, test_ratio = 0.9, 0.1, 0.0 # Ratio
images_dir = "data_labeling/pose_images" # Folder containing the pose annotated images
labels_dir = "data_labeling/orientation_labels" # Folder containing the labels
random.seed(20)

# Creates directories, prints if they exist already
def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"Folder at {path} already exists.")


# Determining the rv threshold to achieve the intended ratio
train_th = train_ratio
valid_th = train_th + valid_ratio
test_th = valid_th + test_ratio

# Creating directories
# Training folders
create_path(f"{dataset_dir}/{dataset_name}/train/images")
create_path(f"{dataset_dir}/{dataset_name}/train/labels")
# Validation folders
create_path(f"{dataset_dir}/{dataset_name}/valid/images")
create_path(f"{dataset_dir}/{dataset_name}/valid/labels")
# Testing folders
create_path(f"{dataset_dir}/{dataset_name}/test/images")
create_path(f"{dataset_dir}/{dataset_name}/test/labels")

# Accessing the images
images = os.listdir(images_dir)
images.sort()

# Looping through all the images and the associated label
for image in images:
    data_name = image.rsplit(".", 1)[0]
    image_path = f"{images_dir}/{data_name}.jpg"
    label_path = f"{labels_dir}/{data_name}.txt"

    # Determining which folder to assign the data to
    ran = random.random()
    if ran <= train_th:
        shutil.copyfile(image_path, f"{dataset_dir}/{dataset_name}/train/images/{data_name}.jpg")
        shutil.copyfile(label_path, f"{dataset_dir}/{dataset_name}/train/labels/{data_name}.txt")
    elif ran <= valid_th:
        shutil.copyfile(image_path, f"{dataset_dir}/{dataset_name}/valid/images/{data_name}.jpg")
        shutil.copyfile(label_path, f"{dataset_dir}/{dataset_name}/valid/labels/{data_name}.txt")
    else:
        shutil.copyfile(image_path, f"{dataset_dir}/{dataset_name}/test/images/{data_name}.jpg")
        shutil.copyfile(label_path, f"{dataset_dir}/{dataset_name}/test/labels/{data_name}.txt")