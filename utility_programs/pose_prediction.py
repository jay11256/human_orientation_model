# Goal is to save prediction annotations in a text file similar to the labels file that is used for training

# Save prediction images in a folder (will serve as the training images for the next model)
# Save bounding box information in a folder of txts (will serve as the training labels after the class is modified)

# Imports
from ultralytics import YOLO
import comet_ml
import cv2
import numpy as np
from PIL import Image

# Choosing model
model = YOLO("yolo_models/yolov8m-pose.pt")

# Predicting from data
# Saves the images with bounding boxes and k eypoints (no class label or confidence)
results = model.predict("data_labeling/sampled_images", save=True, show_labels=False, show_conf=False, project="pose_prediction", name="pose_images", stream=True, max_det = 5)

# Looping through all the results objects
idx = 0
for r in results:
    file_name = r.path.split("/")[-1]
    file_name = file_name.rsplit(".", 1)[0]
    r.save_txt(txt_file=f"pose_labels/{file_name}.txt")

    

# no need to crop the keypoint coordinates, detect training automatically ignores it