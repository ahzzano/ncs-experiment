import openvino as ov
import cv2 as cv

from ultralytics import YOLO

def main():
    print("Hello from ncs-experiment!")
    core = ov.Core()
    print(core.available_devices)

if __name__ == "__main__":
    main()
