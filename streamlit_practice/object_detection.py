import streamlit as st
import cv2
import numpy as np
from PIL import Image

MODEL = './model/MobileNetSSD_deploy.caffemodel'
PROTOTXT = './model/MobileNetSSD_deploy.prototxt'

def process_image(image):
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300,300)), 0.007843, (300, 300), 127.5)
    net = cv2.dnn.readNetFromCaffe(PROTOTXT,MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections

def annotate_image(image, detections, confidence_threshold=0.5):
    (h,w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7]* np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')
            cv2.rectangle(image, (startX, startY), (endX, endY), 70, 2)
    return image

st.title('Object Detection')
file = st.file_uploader('Upload file to dectect', type=['png', 'jpg', 'jpeg'])

if file is not None:
    st.image(file)
    image = Image.open(file)
    image = np.array(image)
    detections = process_image(image)
    process_image = annotate_image(image, detections)
    st.image(process_image)