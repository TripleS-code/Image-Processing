import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def Propagator(M, N, lambda_val, area1, area2, z):
    p = np.zeros((M, N), dtype=np.complex128)
    for ii in range(M):
        for jj in range(N):
            alpha = lambda_val * (ii - M/2 - 1) / area1
            beta = lambda_val * (jj - N/2 - 1) / area2
            if (alpha**2 + beta**2) <= 1:
                p[ii, jj] = np.exp(-2j * np.pi * z * np.sqrt(1 - alpha**2 - beta**2) / lambda_val)
    return p

def create_ellipse_filter(M, N, radius_x, radius_y):
    center_x, center_y = M // 2, N // 2
    y, x = np.ogrid[-center_x:M - center_x, -center_y:N - center_y]
    ellipse_mask = x * x / radius_x ** 2 + y * y / radius_y ** 2 <= 1
    return ellipse_mask

def hologram_reconstruction(reference_image_path, object_image_path, z_start, z_end, z_step, ellipse_radius_x, ellipse_radius_y):
    lambda_val = 635e-9  # Wavelength in meters
    pixel_width = 5.1e-6  # Pixel width

    # Load reference and object images
    reference_image = np.array(Image.open(reference_image_path).convert('L'), dtype=np.float64)
    object_image = np.array(Image.open(object_image_path).convert('L'), dtype=np.float64)

    M, N = reference_image.shape
    h1 = M * pixel_width  # Length of hologram
    h2 = N * pixel_width

    # Create a figure with subplots for enhanced visualization
    fig, axs = plt.subplots(3, 3, figsize=(12, 12))
    fig.suptitle('Hologram Reconstruction', fontsize=16)

    axs[0, 0].imshow(np.abs(object_image), cmap='gray')
    axs[0, 0].set_title('Object Image', fontsize=12)

    # Compute phase difference
    phase_diff = np.angle(object_image) - np.angle(reference_image)

    # Visualize the Phase Difference
    axs[0, 1].imshow(phase_diff, cmap='twilight_shifted', vmin=-np.pi, vmax=np.pi)
    axs[0, 1].set_title('Phase Difference', fontsize=12)

    # Reconstruct object image using phase difference
    reconstructed_object = np.abs(np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(object_image)) * np.exp(1j * phase_diff))))

    # Visualize the Reconstructed Object
    axs[0, 2].imshow(reconstructed_object, cmap='gray')
    axs[0, 2].set_title('Reconstructed Object', fontsize=12)

    ellipse_filter = create_ellipse_filter(M, N, ellipse_radius_x, ellipse_radius_y)

    for z in np.arange(z_start, z_end, z_step):
        prop = Propagator(M, N, lambda_val, h1, h2, -z)

        # Convolve the object wave with the propagator (similar to MATLAB code)
        convolved_object = np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(object_image)) * prop))

        # Visualize the Fourier Spectrum
        spectrum = np.fft.fftshift(np.fft.fft2(object_image))
        axs[1, 0].imshow(np.log(1 + np.abs(spectrum)), cmap='gray')
        axs[1, 0].set_title('Fourier Spectrum', fontsize=12)

        # Visualize the Filtered Spectrum
        filtered_spectrum = spectrum * ellipse_filter
        axs[1, 1].imshow(np.log(1 + np.abs(filtered_spectrum)), cmap='gray')
        axs[1, 1].set_title('Filtered Spectrum', fontsize=12)

        # Visualize the Convolved Object
        axs[1, 2].imshow(np.abs(convolved_object), cmap='gray')
        axs[1, 2].set_title('Convolved Object', fontsize=12)

        plt.pause(0.01)

        if z == z_end - z_step:
            final_reconstruction = np.abs(convolved_object)
            final_reconstruction_image = Image.fromarray(final_reconstruction.astype(np.uint8))
            final_reconstruction_image.save('reco.jpg')

    # Visualize the Reconstruction at z_end
    axs[2, 0].imshow(np.abs(convolved_object), cmap='gray')
    axs[2, 0].set_title('Reconstruction at z_end', fontsize=12)

    plt.show()

# Paths to reference and object images
reference_image_path = 'reff1.png'
object_image_path = 'test4.png'

# Parameters for hologram reconstruction
z_start = 0.005  # Start distance in meters
z_end = 0.010  # End distance in meters
z_step = 0.0001  # Step size in meters

# Parameters for the ellipse filter
ellipse_radius_x = 221  # Adjust the size of the ellipse along the x-axis
ellipse_radius_y = 219  # Adjust the size of the ellipse along the y-axis

# Perform hologram reconstruction
hologram_reconstruction(reference_image_path, object_image_path, z_start, z_end, z_step, ellipse_radius_x, ellipse_radius_y)
