#log transform 
import cv2
import numpy as np
img=cv2.imread('biraj.jpeg')
cv2.imshow('input image',img)
c=(255/np.log(1+np.max(img)))
log_trx_img=c*np.log(1+img)
log_trx_img=np.array(log_trx_img,dtype='uint8')
cv2.imshow('log transform image',log_trx_img)
cv2.waitKey(0)
cv2.destroyAllWindows()