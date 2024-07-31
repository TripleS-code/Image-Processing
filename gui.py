import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


original_image = None  # Initialize original_image variable


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.jpeg; *.png")])
    entry_path.delete(0, tk.END)
    entry_path.insert(tk.END, file_path)
    display_original_image(file_path)


def display_original_image(file_path):
    if not file_path:
        return

    try:
        # Display the original image
        global original_image
        original_image = plt.imread(file_path)
        ax_original.imshow(original_image)
        ax_original.set_title("Original Image")
        ax_original.axis('off')
        canvas.draw()

        # Display intensity graph of original image
        ax_intensity_original.clear()
        ax_intensity_original.plot(np.mean(original_image, axis=(0, 1)))
        ax_intensity_original.set_title("Intensity Graph (Original)")
        ax_intensity_original.set_xlabel("Pixel Intensity")
        ax_intensity_original.set_ylabel("Frequency")
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def backpropagation():
    if original_image is None:  # Check if original_image has been initialized
        messagebox.showerror("Error", "Please select an image first.")
        return

    try:
        # Placeholder function to simulate backpropagation
        # Here, we'll just display the original image again
        ax_reconstructed.imshow(original_image)
        ax_reconstructed.set_title("Reconstructed Image")
        ax_reconstructed.axis('off')
        canvas.draw()

        # Display intensity graph of reconstructed image
        ax_intensity_reconstructed.clear()
        ax_intensity_reconstructed.plot(np.mean(original_image, axis=(0, 1)))  # Placeholder for reconstructed image
        ax_intensity_reconstructed.set_title("Intensity Graph (Reconstructed)")
        ax_intensity_reconstructed.set_xlabel("Pixel Intensity")
        ax_intensity_reconstructed.set_ylabel("Frequency")
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Backpropagation Simulator")

# Create matplotlib figures and axes
fig, ((ax_original, ax_intensity_original), (ax_reconstructed, ax_intensity_reconstructed)) = plt.subplots(2, 2)
fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

# Embed matplotlib figures in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create label and entry for file path
label_path = tk.Label(root, text="Hologram Image Path:")
label_path.pack(side=tk.LEFT, padx=5, pady=5)
entry_path = tk.Entry(root, width=50)
entry_path.pack(side=tk.LEFT, padx=5, pady=5)

# Create button for file selection
button_browse = tk.Button(root, text="Browse", command=open_file)
button_browse.pack(side=tk.LEFT, padx=5, pady=5)

# Create button for backpropagation
button_backprop = tk.Button(root, text="Backpropagation", command=backpropagation)
button_backprop.pack(side=tk.LEFT, padx=5, pady=5)

# Create sliders and entry boxes for adjusting parameters
label_distance = tk.Label(root, text="Screen Sample Distance:")
label_distance.pack(side=tk.LEFT, padx=5, pady=5)
entry_distance = tk.Entry(root, width=10)
entry_distance.pack(side=tk.LEFT, padx=5, pady=5)

label_pixel_length = tk.Label(root, text="Pixel Length:")
label_pixel_length.pack(side=tk.LEFT, padx=5, pady=5)
entry_pixel_length = tk.Entry(root, width=10)
entry_pixel_length.pack(side=tk.LEFT, padx=5, pady=5)

label_num_pixels = tk.Label(root, text="Number of Pixels:")
label_num_pixels.pack(side=tk.LEFT, padx=5, pady=5)
entry_num_pixels = tk.Entry(root, width=10)
entry_num_pixels.pack(side=tk.LEFT, padx=5, pady=5)

label_planes = tk.Label(root, text="Backpropagation at Different Planes:")
label_planes.pack(side=tk.LEFT, padx=5, pady=5)
slider_planes = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
slider_planes.pack(side=tk.LEFT, padx=5, pady=5)

# Start the GUI
root.mainloop()
