import cv2

# Load the color image
color_image = cv2.imread('biraj.jpeg')

# Convert the color image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Display the color image
cv2.imshow('Color Image', color_image)

# Display the grayscale image
cv2.imshow('outputImage', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
