#black and white lab3
import cv2

# Load the grayscale image
gray_image = cv2.imread('biraj.jpeg', cv2.IMREAD_GRAYSCALE)

# Set a threshold value (adjust as needed)
threshold_value = 128

# Apply binary thresholding
_, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

# Save the binary (black and white) image
cv2.imwrite('binary_image.jpg', binary_image)

# Display the binary image (optional)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()