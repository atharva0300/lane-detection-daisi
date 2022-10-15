from socket import ALG_SET_AEAD_ASSOCLEN
import processing as p
import cv2
import os


def video_main(videoFile) : 

    print('Video file : ' , videoFile)
    cap = cv2.VideoCapture(videoFile)
    target_address = f'{os.getcwd()}/generated_images'
    counter=0

    while(cap.isOpened()) : 
        # decoding every video frame
        _ , frame = cap.read()
        # the _ => value is the boolean value which says if the frame is present or not 
        # the frame gives the frame


        if(_== False) : 
            # if the video has reached the frame after the last frame ( ie- if completed the video )
            # then break the loop and return 
            cap.release()  
            cv2.destroyAllWindows() 
            print('counter : ' , counter )
            print('all images stored')
            print('target_address : ' , target_address)

            return True

        outputImage = p.image_processing(frame)

        # writing the images in the disk
        cv2.imwrite(target_address + '/' + str(counter) + '.jpg' , outputImage)
        
        counter += 1 

    







