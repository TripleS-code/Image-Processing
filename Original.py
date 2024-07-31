import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt
from PIL import Image

# Define the Propagator function
def Propagator(M, N, lambda_, area1, area2, z):
    p = np.zeros((M, N), dtype=complex)

    for ii in range(M):
        for jj in range(N):
            alpha = lambda_ * (ii - M / 2 - 1) / area1
            beta = lambda_ * (jj - N / 2 - 1) / area2
            if (alpha**2 + beta**2) <= 1:
                p[ii, jj] = np.exp(-2 * np.pi * 1j * z * np.sqrt(1 - alpha**2 - beta**2) / lambda_)

    return p

# Load the recorded image (assuming it's in PNG format)
recorded_image = np.array(Image.open('test2.png').convert('L'))

# Fourier transform of the recorded image
fourier_transform = fft.fftshift(fft.fft2(recorded_image))

# Propagation compensation
propagator = Propagator(*recorded_image.shape, 500e-9, recorded_image.shape[0], recorded_image.shape[1], 0.008)
compensated_spectrum = fourier_transform / propagator

# Reconstructed image after inverse Fourier transform
reconstructed_image = np.abs(fft.ifft2(fft.ifftshift(compensated_spectrum)))

# Create a figure with multiple subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Display the recorded image
axs[0, 0].imshow(recorded_image, cmap='gray')
axs[0, 0].set_title('Recorded Image')

# Display the Fourier transform of the recorded image
axs[0, 1].imshow(np.log(1 + np.abs(fourier_transform)), cmap='gray')
axs[0, 1].set_title('Fourier Transform')

# Display the propagation compensated Fourier spectrum
axs[0, 2].imshow(np.log(1 + np.abs(compensated_spectrum)), cmap='gray')
axs[0, 2].set_title('Compensated Spectrum')

# Display the reconstructed image
axs[1, 0].imshow(reconstructed_image, cmap='gray')
axs[1, 0].set_title('Reconstructed Image')

# Hide the empty subplot
axs[1, 1].axis('off')

# Adjust spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
