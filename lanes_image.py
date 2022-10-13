import cv2
import numpy as np
import matplotlib.pyplot as plt
import processing as p
import uuid
import os


def image_main(imageFile) : 

    print('Image File : ' , imageFile)
    # reading the image 
    image = cv2.imread('./test_image/1.jpg')
    print('image : ' , image)

    #cv2.imshow('original' , image)
    # display the image
    image = p.image_processing(image , True )
    # take the image and store the image in the generated/images folder

    return image
    




