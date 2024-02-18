#lab5
import cv2
import matplotlib.pyplot as plt

def plot_histogram(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Calculate histogram
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Plot histogram
    plt.plot(hist, color='black')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

if __name__ == "__main__":
    # Replace 'your_image.jpg' with the path to your image file
    image_path = 'biraj.jpeg'

    # Plot the histogram
    plot_histogram(image_path)
