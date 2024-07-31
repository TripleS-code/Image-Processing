import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk

# Function to capture image at current glass slide position
def capture_image():
    # Capture image using Raspberry Pi camera
    # For demonstration, let's assume captured_image is already loaded
    captured_image = cv2.imread("captured_image.png", cv2.IMREAD_GRAYSCALE)
    return captured_image

# Function for holographic reconstruction
def holographic_reconstruction(image):
    # Generate reference wave by duplicating and slightly modifying the input image
    reference_wave = image.copy()
    reference_wave = cv2.GaussianBlur(reference_wave, (0, 0), sigmaX=5, sigmaY=5)

    # Perform holographic reconstruction
    complex_wavefront = np.fft.fftshift(np.fft.fft2(image - reference_wave))

    # Compute magnitude for visualization
    magnitude = np.abs(complex_wavefront)

    # Normalize magnitude for display
    magnitude = (magnitude - np.min(magnitude)) / (np.max(magnitude) - np.min(magnitude)) * 255
    magnitude = magnitude.astype(np.uint8)

    return magnitude

# Function to update image display
def update_image():
    # Capture image
    image = capture_image()
    # Perform holographic reconstruction
    reconstructed_image = holographic_reconstruction(image)
    # Display reconstructed image
    cv2.imshow("Holographic Reconstruction", reconstructed_image)
    cv2.waitKey(1)  # Adjust the delay as needed

# Create GUI
root = tk.Tk()
root.title("Holographic Reconstruction")

# Slider for controlling glass slide position
slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=lambda _: update_image())
slider.pack()

# Initialize image display
update_image()

# Run GUI
root.mainloop()
