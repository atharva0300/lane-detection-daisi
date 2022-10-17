import streamlit as st
import lanes_image as li
import lanes_video as lv
import numpy as np
import cv2
import os
import generate_video


def API_image(imagePath) :
    outputImage = li.image_main(imagePath)
    return outputImage

def delete_all_files() : 
    target_address = os.getcwd() + '/generated_images'
    print(os.listdir(target_address))

    for fileName in os.listdir(target_address) :
        print('removing : ' , fileName) 
        os.remove(target_address + '/' + fileName)
    

    print('Sucessfully removed the generated_images directory')


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
        # converting the uploaded streamlit image into opencv readable image 
        outputImage =  li.image_main(opencvImage)

        st.text('Output Image')
        st.image(outputImage , channels = "BGR")
        # channels is the type of the image which we are passing into the function
        # here the type of the image is a BGR image
        
        RGBImage = cv2.cvtColor(outputImage , cv2.COLOR_BGR2RGB)
        # converting the BGR image to RGB 

        print('RGB Image : ' , RGBImage)
        return RGBImage
        

def st_video_ui() : 
    st.text('Taking video')
    videoFile = st.file_uploader('Upload a video' , type = ["mp4" , "mov"])

    if(videoFile is not None ):
        st.video(str(os.getcwd()) + '/test_video/1.mp4' , format = "video/mp4" , start_time = 0)


    value = st.button('Submit' , 2)
    if(value==True) : 
        video_address =  f'{os.getcwd()}/test_video/1.mp4'
        # store the file in byte format
        finishedsaving = lv.video_main(video_address)

        if finishedsaving==True : 
            # generating the video using the temp_main function from the temp.py file 
            finishedTask = generate_video.generate()
            print(finishedTask)
            
            if finishedTask==True : 
                print('Successfully generated video')
                # display the vidoe on the ui
                target_address = f'{os.getcwd()}/generated_video/1.mp4'

                st.video( target_address, format="video/mp4" , start_time=0)

                # delete all the images in the generated_images folder
                delete_all_files()

                print(target_address)
    


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