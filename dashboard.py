import streamlit as st
import pandas as pd
import numpy as np
import cv2

#streamlit stream using webcam
def streamlit_webcam():
    st.title("Webcam Stream")
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    while run:
        _, frame = camera.read()
        #convert BRG to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    del(camera)
st.title("Streamlit WebCam")

streamlit_webcam()
