import processing as p
import cv2
import uuid
import os

id = uuid.uuid1()
# Get global UUID

'''
def storeTarget(frame , out , counter):
    for i in counter : 
        out.write(frame)
    
    directory = os.getcwd()
    print('working directory : ' , directory)
    target_directory = directory + '/generated/videos/' + str(id) + '.mp4'
    print('video target : ' , target_directory )
    cv2.imwrite(target_directory , out)
    # save the image in the target directory


    return target_directory
    
'''

def video_main(videoFile) : 
    frameSize = (500 , 500)

    print('Video file : ' , videoFile)
    cap = cv2.VideoCapture(videoFile)
    img = []
    counter=0
    while(cap.isOpened()) : 
        # decoding every video frame
        _ , frame = cap.read()
        # the _ => value is the boolean value which says if the frame is present or not 
        # the frame gives the frame

        breakValue = p.image_processing(frame , False , out = False)
        

        if(breakValue is True) : 
            #target_directory = storeTarget(img , out , counter)
            
            cap.release()
            cap.destroyAllWindows()

            #return target_directory
    







