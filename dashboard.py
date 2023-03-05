import streamlit as st
import pandas as pd
import numpy as np
import cv2

#streamlit stream using webcam
def streamlit_webcam():
    st.title("Webcam Stream")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    while run:
        _, frame = camera.read()
        FRAME_WINDOW.image(frame)
    del(camera)

st.title("Streamlit Dashboard")
#stream the webcam
streamlit_webcam()