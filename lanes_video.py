import processing as p
import cv2

def main() : 
    cap = cv2.VideoCapture('./test_video/1.mp4')
    while(cap.isOpened()) : 
        # decoding every video frame
        _ , frame = cap.read()
        # the _ => value is the boolean value which says if the frame is present or not 
        # the frame gives the frame

        breakValue = p.image_processing(frame , False)
        if(breakValue is True) : 
            cap.release()
            cap.destroyAllWindows()



main()



