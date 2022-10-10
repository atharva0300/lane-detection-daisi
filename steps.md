1. import cv2 and numpy
2. take an image 
3. convert the image to grayscale image 
4. Reduce noice in the grayscale image using the gaussian blur
5. create a canny image from the blurred image. This will show the edges
6. Create a polygon with the region of interest ( 3 points )
7. Create a mask and fill the mask with the polygon. This new image will be called the polygon image
8. Take the bitwise_and of the canny and the polygon image. The new image will be called the cropped image
9. Use Hough transformation to get the straight line. Get the lines from the HoughLinesP method.
10. Iterate through all the linee, extract the x1,y1,x2,y2 coordinates and create a line image
11. Overlap the line image onto the lane image
