from ultralytics import YOLO
import comet_ml
import cv2
import numpy as np
from PIL import Image

# Choosing model
scratch_model = YOLO("yolov8l.yaml")
model = YOLO("yolov8n.pt")
old_model = YOLO("runs/detect/train5.0/weights/best.pt")

# Start training based off of yolov8m
def coco():
    results = model.train(data="orientation_model/orientation.yaml",
                        epochs=100,
                        cache=True,
                        name="train8.0_random",
                        fliplr=0.0)

# Continue training off an existing model
def old():
    results = old_model.train(data="orientation_model/orientation.yaml",
                        epochs=100,
                        cache=True,
                        project="trained_models",
                        name="train1.0",
                        fliplr=0.0,
                        lr0=0.05)

# Start training from scratch
def scratch():
    results = scratch_model.train(data="orientation_model/orientation.yaml",
                        epochs=100,
                        cache=True,
                        name="train6.2_random",
                        fliplr=0.0)

def main():
    print("Running program...")
    coco()
    # old()
    # scratch()

if __name__ == '__main__':
    main()