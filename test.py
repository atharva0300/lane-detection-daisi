import cv2
import pydaisi

lane_detection = pydaisi.Daisi('atharva0300/Lane Detection')
image = lane_detection.API_image('./test_image/1.jpg')
print(image)
cv2.imshow('API Image' , image)