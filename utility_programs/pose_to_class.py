# Goal is to modify the classes for each label so instead of just being 0 (person), it's 0-7 (8 directions)

# GUI
# Annotated image with numbered bounding boxes (numbers = line number in txt file)
# (Optional) Original image with no annotations (in case annotations cover important information)

# Class Changing
# Maybe do it through the terminal?
# Should be very easy and quick

# Other
# Be able to save where annotations left off at
# Shouldn't need to start at the beginning each time

# Imports
import os
from PIL import Image
import matplotlib.pyplot as plt
import pyautogui

# Paths to folders being accessed and used
images_path = "data_labeling/sampled_images" # Path to directory containing images
labels_path = "data_labeling/pose_labels" # Path to directory containing predicted pose labels
results_path = "data_labeling/orientation_labels" # Path to directory containing processed labels

def valid_list(list, n):
    if (len(list) != n):
        return False
    for num in list:
        if (int(num) not in [8, 9, 6, 3, 2, 1, 4, 7]):
            return False
    return True

# Opening images
images = os.listdir(images_path)
images.sort()

# Finding starting point
preserved = open("data_labeling/preserved_data.txt", "r") #552
start_index = int(preserved.read(5))
preserved.close()

# Looping through the images
for image in images[start_index:]:

    # Displaying images
    file_path = os.path.join(images_path, image)
    disp = Image.open(file_path)
    plt.figure(figsize=(12, 12))
    plt.imshow(disp, extent=[0, 1, 1, 0])
    plt.title(image)


    # Opening annotations txt file to obtain bounding box coordinates
    label = file_path.split("/")[-1]
    label = label.rsplit(".", 1)[0]
    fread = open(f"{labels_path}/{label}.txt", "r")

    # Looping through each line in the txt file to plot the text
    i = 1
    for line in fread:
        line = line.split()
        x, y = float(line[1]), float(line[2])
        plt.text(x, y, "█", color="black", fontsize=14, ha="center", va="center", fontweight="bold")
        plt.text(x, y, str(i), color="white", fontsize=12, ha="center", va="center", fontweight="bold")
        print(i, x, y)
        i += 1
    fread.close()

    # Displaying image
    plt.show(block=False)
    plt.pause(1)
    pyautogui.click(1500, 1000)

    # Getting input for new classes
    while True:
        temp = input(f"Orientations ({i - 1}): ")
        classes = [*temp]
        if (valid_list(classes, i - 1)):
            break
        else:
            print("Invalid input")

    # Remapping the input
    for i in range(len(classes)):
        if classes[i] == "8":
            classes[i] = "0"
        elif classes[i] == "9":
            classes[i] = "1"
        elif classes[i] == "6":
            classes[i] = "2"
        elif classes[i] == "3":
            classes[i] = "3"
        elif classes[i] == "2":
            classes[i] = "4"
        elif classes[i] == "1":
            classes[i] = "5"
        elif classes[i] == "4":
            classes[i] = "6"
        else:
            classes[i] = "7"

   # Writing classes to a new file
    fread = open(f"{labels_path}/{label}.txt", "r")
    fwrite = open(f"{results_path}/{label}.txt", "w")
    i = 0
    for line in fread:
        line = line.split()
        x, y = float(line[1]), float(line[2])
        w, h = float(line[3]), float(line[4])
        fwrite.write(f"{classes[i]} {x} {y} {w} {h}\n")
        i += 1

    # Closing files
    fwrite.close()
    fread.close()
    plt.close()

    # Saving current location in all of the data
    preserved = open("orientation_model/preserved_data.txt", "w")
    start_index += 1
    preserved.write(str(start_index))
    preserved.close()