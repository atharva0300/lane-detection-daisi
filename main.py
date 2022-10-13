from xml.dom import VALIDATION_ERR
import pydaisi as pyd
import streamlit as st
import lanes_image as li
import lanes_video as lv
import numpy as np
import cv2


def st_image_ui() : 
    st.text('Taking image')
    imageFile = st.file_uploader('Upload an image file' , type = "jpg")
    print('imageFile from streamlit : ' , imageFile)
    
    value = st.button('Submit' , 1)

    if imageFile is not None : 
        # convert the file to opencv image 
        file_bytes = np.asarray(bytearray(imageFile.read()) , dtype = np.uint8)
        opencvImage = cv2.imdecode(file_bytes , 1)

        st.image(opencvImage , channels = "BGR")

    if(value==True) :
        outputImage =  li.image_main(imageFile)

        st.text('Output Image')
        st.image(outputImage , channels = "BGR")
        

def st_video_ui() : 
    st.text('Taking video')
    videoFile = st.file_uploader('Upload a video')
    value = st.button('Submit' , 2)
    if(value==True) : 
        # store the file in byte format
        lv.video_main('./test_video/1.mp4')

        # display the vidoe on the ui
        #st.video(videoPath , format='video/mp4' , start_time=0)


def st_ui() : 
    imageUI = False
    with st.sidebar : 
        value = st.selectbox(
            'Select a format for data input',
            ("Image" , "Video")
        )

        print(value)
        if(value == 'Image') :
            imageUI = True

        elif (value == 'Video') :
            imageUI = False
    
    if(imageUI==True) : 
        st_image_ui()
    
    elif(imageUI==False) : 
        st_video_ui()
         



st_ui()