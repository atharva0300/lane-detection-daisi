import cv2
import numpy as np
import matplotlib.pyplot as plt
import processing as p
import uuid
import os


def image_main(image) : 

    # reading the image 
    #image = cv2.imread(imageFile)
    print('image : ' , image)

    #cv2.imshow('original' , image)
    # display the image
    outputImage = p.image_processing(image )
    # take the image and store the image in the generated/images folder

    # storing the image in the generated image folder
    cv2.imwrite(os.getcwd() + '/generated_images/1.jpg' , outputImage)


    return outputImage
    




