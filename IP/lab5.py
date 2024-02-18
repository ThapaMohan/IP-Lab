#constrast stretching
import cv2
import numpy as np
#function
def pixelVal(pix,r1,s1,r2,s2):
    if(0<=pix and pix<=r1):
        return(s1/r1)*pix
    elif(r1<pix and pix<=r2):
        return (s2-s1)/(r2-r1)*(pix-r1)+s1
    else:
        return ((255-s2)/(255-r2))*(pix-r2)+s2
img=cv2.imread('me.jpg')
 #parameter defined
r1=70
s1=0
r2=140
s2=255
#to use in numpy array
pixelVal_vec=np.vectorize(pixelVal)
cont_stretching=pixelVal_vec(img,r1,s1,r2,s2)
cv2.imshow('input image',img)
cv2.imshow('output image',cont_stretching)
cv2.waitKey(0)
cv2.destroyAllWindows()