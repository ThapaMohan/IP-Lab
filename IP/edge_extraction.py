import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('biraj.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply the Canny edge detector
edges = cv2.Canny(image, 50, 150)

# Display the original and edge-detected images
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Extraction'), plt.xticks([]), plt.yticks([])

plt.show()
