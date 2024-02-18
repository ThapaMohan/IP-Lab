# import cv2 Library
import cv2
# provide the source file as you want
img=cv2.imread('biraj.jpeg')
# using cvtcolor we can convert RGB imsge to GRAY
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#using gaussin blure function we can blure the image
imgblur=cv2.GaussianBlur(imggray, (9,9) ,0)
# to show the out put image
cv2.imshow( 'output' , img)
# to show the blure image
cv2.imshow('blur image' ,imgblur)
## to show the blur image
cv2.imshow('gray image', imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()