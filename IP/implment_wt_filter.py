import cv2
import numpy as np

def weighted_average_filter(image, kernel):
    # Get the dimensions of the image
    rows, cols = image.shape

    # Get the dimensions of the kernel
    k_rows, k_cols = kernel.shape

    # Define the output image
    output_image = np.zeros((rows, cols), dtype=np.uint8)

    # Define the padding to handle border pixels
    pad_rows = k_rows // 2
    pad_cols = k_cols // 2

    # Pad the image
    padded_image = cv2.copyMakeBorder(image, pad_rows, pad_rows, pad_cols, pad_cols, cv2.BORDER_CONSTANT)

    # Apply the weighted average filter
    for i in range(pad_rows, rows + pad_rows):
        for j in range(pad_cols, cols + pad_cols):
            region_of_interest = padded_image[i - pad_rows:i + pad_rows + 1, j - pad_cols:j + pad_cols + 1]
            weighted_sum = np.sum(region_of_interest * kernel)
            output_image[i - pad_rows, j - pad_cols] = np.clip(weighted_sum, 0, 255).astype(np.uint8)

    return output_image

# Read an example image
original_image = cv2.imread('me.jpg', cv2.IMREAD_GRAYSCALE)

# Define a simple 3x3 kernel (you can adjust the weights based on your requirements)
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]])

# Normalize the kernel to make sure the weights sum to 1
kernel = kernel / np.sum(kernel)

# Apply the weighted average filter
filtered_image = weighted_average_filter(original_image, kernel)

# Display the results
cv2.imshow('Original Image', original_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
