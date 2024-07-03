from ultralytics import YOLO
import comet_ml
import cv2
import numpy as np
from PIL import Image

# Parameters
yaml_path = "datasets/orientation.yaml"

# Choosing model
model = YOLO("yolov8n.pt")

# Start training based off of yolov8m
def coco():
    results = model.train(data=yaml_path,
                        epochs=100,
                        cache=True,
                        project="training_results",
                        name="train1.0_random_500",
                        fliplr=0.0,
                        label_smoothing=0.1,
                        mosaic=0.0)

def main():
    print("Running program...")
    coco()
    # old()
    # scratch()

if __name__ == '__main__':
    main()