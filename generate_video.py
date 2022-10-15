import numpy as np
import cv2
import os
 
def generate() : 

    width = 1280
    height = 720
    channel = 3
    
    fps = 50
    sec = 25

    target_address = f'{os.getcwd()}'


    img = np.random.randint(0,255, (height, width, channel), dtype = np.uint8)
    print('img shape : ' , img.shape)
    print('img dtype : ' , img.dtype)

    
    # Syntax: VideoWriter_fourcc(c1, c2, c3, c4) # Concatenates 4 chars to a fourcc code
    #  cv2.VideoWriter_fourcc('M','J','P','G') or cv2.VideoWriter_fourcc(*'MJPG)
    
    fourcc = cv2.VideoWriter_fourcc('m' , 'p' , '4' , 'v') # FourCC is a 4-byte code used to specify the video codec.
    # A video codec is software or hardware that compresses and decompresses digital video. 
    # In the context of video compression, codec is a portmanteau of encoder and decoder, 
    # while a device that only compresses is typically called an encoder, and one that only 
    # decompresses is a decoder. Source - Wikipedia
    
    #Syntax: cv2.VideoWriter( filename, fourcc, fps, frameSize )
    video = cv2.VideoWriter(target_address + '/generated_video/1.mp4', fourcc, float(fps), (width, height))
    
    print('Generating video...')
    for frame_count in range(fps*sec):
        #img = np.random.randint(0,255, (hieght, width, channel), dtype = np.uint8)
        img = cv2.imread(target_address + '/generated_images/' + str(frame_count) + '.jpg')
        video.write(img)
    
    video.release()


    return True
