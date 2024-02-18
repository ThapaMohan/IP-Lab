#gamma tranform
import cv2
import numpy as np
img=cv2.imread('biraj.jpeg')
gamma = 0.6
s= np.array(255 * (img / 255) ** gamma, dtype='uint8')
cv2.imshow("Original Image", img)
cv2.imshow("Gamma Image",s)
cv2.waitKey(0)
cv2.destroyAllWindows()