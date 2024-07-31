import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image (replace 'your_image.jpg' with the path to your image)
image_path = 'sat.png'
image = Image.open(image_path)

# Convert the image to grayscale (if it's not already)
if image.mode != 'L':
    image = image.convert('L')

# Convert the image to a NumPy array
image_array = np.array(image)

# Calculate the intensity values
intensity_values = image_array.flatten()

# Plot the intensity values
plt.hist(intensity_values, bins=256, range=(0, 256), density=True, color='gray', alpha=0.7)
plt.xlabel('Pixel Value')
plt.ylabel('Normalized Frequency')
plt.title('Intensity Histogram')
plt.show()
