import cv2
import numpy as np


def canny(lane_image) : 
    gray = cv2.cvtColor(lane_image , cv2.COLOR_RGB2GRAY)

    # displaying the grayscale image 
    #cv2.imshow('gray image' , gray)

    # using a gaussian blur to reduce the noice in the grayscale image 
    blur = cv2.GaussianBlur(gray , (5,5) , 0)

    # canny image 
    canny = cv2.Canny(blur , 50 , 150)
    # low threshold => 50
    # high threshold => 150 

    return canny

def regionOfInterest(image) : 
    # return the enclosed region of the field of view
    height = image.shape[0]
    # the height is the image.shape[0]
    polygons = np.array([[(250 , height) , (1100 , height) , (500 , 250)]])
    # (0,500) => width and height
    # we have defined 3 points, and it will form a triangle in the 3 points which will be our region of interest

    mask = np.zeros_like(image)

    # filling the mask with the triangle
    cv2.fillPoly(mask , polygons , 255)

    masked_image = cv2.bitwise_and(image , mask)
    return masked_image


def display_lines(image , lines) : 
    # function to display the hough lines
    line_image = np.zeros_like(image)
    if lines is not None :
        for line in lines : 
            x1 , y1 , x2 , y2 = line.reshape(4)
            # reshaping the line into 4 1D array with 4 elements

            # creating a line connecting these 2 points
            cv2.line(line_image , (x1 , y1) , (x2 , y2) , (255 , 0) , thickness = 10)
    
    return line_image

def make_coordinates(image , line_parameters ) :
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1-intercept)/slope)
    x2 = int((y2-intercept)/slope)
    
    return np.array([x1,y1,x2,y2])



def average_slope_intercept(image , lines ) : 
    left_fit = []
    right_fit = []

    for line in lines : 
        # reshape each line in 1D array 
        x1,y1,x2,y2 = line.reshape(4)
        parameters = np.polyfit((x1 , x2), (y1 , y2) , 1)
        slope = parameters[0]
        intercept = parameters[1]
        
        if slope < 0 : 
            # appending the coordinates in the tuple
            left_fit.append((slope , intercept))
        else : 
            right_fit.append((slope, intercept))
    
    left_fit_average = np.average(left_fit , axis = 0)
    # get the average left fit

    right_fit_average = np.average(right_fit , axis=0)
    # get the average right fit

    print(left_fit_average , ' left')
    print(right_fit_average , ' right')

    left_line = make_coordinates(image , left_fit_average)
    right_line = make_coordinates(image , right_fit_average)

    return np.array([left_line , right_line]) 



def image_processing(image , imageBool ) : 
    lane_image = np.copy(image)
    # creating a copy of the array 
    # any changes made in the lane_image is reflected back in the image
    # passing the image to canny function
    canny_image = canny(lane_image)
    #cv2.imshow('result' , canny)

    # plotting the image
    # NOTE ! => opencv follows BGR format for image, whereas matplotlib follows RGB format
    #plt.imshow(canny_image)
    #plt.show()
    

    cropped_image = regionOfInterest(canny_image)
    #cv2.imshow('cropped image' , cropped_image)

    lines = cv2.HoughLinesP(cropped_image ,2 , np.pi/100 , 100 , np.array([]) , minLineLength = 40 , maxLineGap = 5)
    averaged_lines = average_slope_intercept(lane_image , lines)
    line_image = display_lines(lane_image , averaged_lines)

    overlapImage = cv2.addWeighted(lane_image , 0.8 , line_image ,1 , 1)
    # 1 => weight
    # 1 => gamma value

    # display the line image 
    # cv2.imshow('line image' , overlapImage)

    print(imageBool)

    if(imageBool is True) : 
        # return the image
        return overlapImage
    
    elif(imageBool is False) : 

        # wait time for video to 1ms
        if cv2.waitKey(1) & 0xFF == ord('q') : 
            return True
