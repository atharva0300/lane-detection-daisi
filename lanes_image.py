from asyncio import constants
import cv2
import numpy as np
import matplotlib.pyplot as plt
import processing as p



def main() : 
    # reading the image 
    image = cv2.imread('./test_image/1.jpg')
    #cv2.imshow('original' , image)
    # display the image
    p.image_processing(image , True)

main()


