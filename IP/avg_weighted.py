import numpy as np
import cv2

def weighted_average_filter(image, kernel_size=3):
    # Ensure the kernel size is odd
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be an odd number")

    # Create a kernel with weights (center pixel has the highest weight)
    weights = np.arange(1, kernel_size**2 + 1).reshape((kernel_size, kernel_size))
    kernel = weights / np.sum(weights)

    # Apply the filter to each channel (if the image is color)
    if len(image.shape) == 3:
        result = np.zeros_like(image, dtype=np.float32)
        for channel in range(image.shape[2]):
            result[:, :, channel] = cv2.filter2D(image[:, :, channel], -1, kernel)
    else:
        result = cv2.filter2D(image, -1, kernel)

    return result.astype(np.uint8)

# Example usage:
input_image = cv2.imread("biraj.jpeg")

# Apply weighted average filtering with a 3x3 kernel
output_image = weighted_average_filter(input_image, kernel_size=3)

# Display the results
cv2.imshow("Original Image", input_image)
cv2.imshow("Filtered Image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
