import cv2
import pydaisi

image = pydaisi.Daisi('atharva0300/Lane Detection')
print(image)
image2 = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)
cv2.imshow('API Image' , image2)