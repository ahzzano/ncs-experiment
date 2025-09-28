import openvino as ov
import cv2 as cv
import tensorflow as tf
import numpy as np
from PIL import Image

class_names = ['Cordana', 'Healthy', 'Pestalotiopsis', 'Sigatoka']

def main():
    print("Hello from ncs-experiment!")
    core = ov.Core()
    print(core.available_devices)
    compiled = core.compile_model('ov_model.xml', device_name='CPU')

    img = Image.open('c0.jpeg').resize(( 224, 224 ))
    arr = np.array(img)/255

    img_np = np.expand_dims(arr, axis=0).astype(np.float32)
    features = compiled(img_np)
    print(features)


if __name__ == "__main__":
    main()
