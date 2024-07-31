import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Set a default hologram path
hologram_path = 'C:/Users/SATWIK SAHOO/PycharmProjects/pythonProject/pic65.jpg'

# Create a function to capture a photo and update the displayed image
def capture_photo():
    global hologram_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        hologram_path = file_path
        update_captured_photo()


# Create a function to update the displayed image
def update_captured_photo():
    global hologram_path

    try:
        # Load the image
        img = Image.open(hologram_path)

        if img.mode != "L":  # Ensure that the image is grayscale (if not, convert it)
            img = img.convert("L")

        # Resize the image
        img = img.resize((400, 400))

        # Convert the image to a NumPy array of floats
        img_array = np.asarray(img, dtype=float)

        # Display the image in the label
        img = ImageTk.PhotoImage(img)
        captured_photo_label.config(image=img)
        captured_photo_label.image = img  # Keep a reference to avoid garbage collection

        # Update the intensity graph with the loaded image
        update_intensity_graph(img_array)
    except Exception as e:
        messagebox.showerror("Error", f"Error loading image: {str(e)}")


# Create a function to update the intensity graph with the loaded image
def update_intensity_graph(img):
    intensity_plot.clear()

    # Convert the image to a numpy array of floats
    img_array = np.asarray(img, dtype=float)

    intensity_plot.imshow(img_array,
                          cmap='gray')  # Display the loaded image in the intensity graph with a gray colormap
    intensity_plot.set_title("Intensity vs. Distance")  # Update the title
    intensity_plot.axis("off")  # Turn off axes
    intensity_canvas.draw()

# Function to update parameters and plot intensity graph
def update_parameters():
    try:
        # Retrieve entered parameter values
        wavelength = wavelength_scale.get()
        pixel_size = pixel_size_scale.get()
        d1_distance = d1_distance_scale.get()
        d2_distance = d2_distance_scale.get()
        lens1_focal_length = lens1_focal_length_scale.get()
        lens2_focal_length = lens2_focal_length_scale.get()
        num_planes = num_planes_scale.get()

        # Update the intensity graph
        plot_intensity_graph(wavelength, pixel_size, d1_distance, d2_distance, lens1_focal_length, lens2_focal_length,
                             num_planes)

        messagebox.showinfo("Parameters Updated", "Parameters have been updated.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")


# Create the main window
root = tk.Tk()
root.title("Photo Reconstruction GUI")
root.geometry("1000x600")  # Set the initial window size

# Create and configure the main frame
main_frame = ttk.Frame(root)
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)  # Allow the image to expand vertically

# Label for captured photo
captured_photo_label = ttk.Label(main_frame)
captured_photo_label.grid(column=0, row=0, columnspan=2, pady=10, rowspan=2)

# Initialize the "Captured Photo" label with the default image
update_captured_photo()

# Button to capture photo
capture_button = ttk.Button(main_frame, text="Capture Photo", command=capture_photo)
capture_button.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)

# Entry and Label for Wavelength
wavelength_label = ttk.Label(main_frame, text="Wavelength (nm):")
wavelength_label.grid(column=0, row=3, sticky=tk.W)
wavelength_scale = ttk.Scale(main_frame, from_=400, to=700, orient="horizontal")
wavelength_scale.grid(column=1, row=3, sticky=(tk.W, tk.E))
wavelength_scale.set(550)  # Set an initial value

# Entry and Label for Pixel Size
pixel_size_label = ttk.Label(main_frame, text="Pixel Size (microns):")
pixel_size_label.grid(column=0, row=4, sticky=tk.W)
pixel_size_scale = ttk.Scale(main_frame, from_=1, to=10, orient="horizontal")
pixel_size_scale.grid(column=1, row=4, sticky=(tk.W, tk.E))
pixel_size_scale.set(5)  # Set an initial value

# Entry and Label for d1 Distance
d1_distance_label = ttk.Label(main_frame, text="d1 Distance (mm):")
d1_distance_label.grid(column=0, row=5, sticky=tk.W)
d1_distance_scale = ttk.Scale(main_frame, from_=0, to=100, orient="horizontal")
d1_distance_scale.grid(column=1, row=5, sticky=(tk.W, tk.E))
d1_distance_scale.set(50)  # Set an initial value

# Entry and Label for d2 Distance
d2_distance_label = ttk.Label(main_frame, text="d2 Distance (mm):")
d2_distance_label.grid(column=0, row=6, sticky=tk.W)
d2_distance_scale = ttk.Scale(main_frame, from_=0, to=100, orient="horizontal")
d2_distance_scale.grid(column=1, row=6, sticky=(tk.W, tk.E))
d2_distance_scale.set(50)  # Set an initial value

# Entry and Label for Lens 1 Focal Length
lens1_focal_length_label = ttk.Label(main_frame, text="Lens 1 Focal Length (mm):")
lens1_focal_length_label.grid(column=0, row=7, sticky=tk.W)
lens1_focal_length_scale = ttk.Scale(main_frame, from_=10, to=200, orient="horizontal")
lens1_focal_length_scale.grid(column=1, row=7, sticky=(tk.W, tk.E))
lens1_focal_length_scale.set(100)  # Set an initial value

# Entry and Label for Lens 2 Focal Length
lens2_focal_length_label = ttk.Label(main_frame, text="Lens 2 Focal Length (mm):")
lens2_focal_length_label.grid(column=0, row=8, sticky=tk.W)
lens2_focal_length_scale = ttk.Scale(main_frame, from_=10, to=200, orient="horizontal")
lens2_focal_length_scale.grid(column=1, row=8, sticky=(tk.W, tk.E))
lens2_focal_length_scale.set(100)  # Set an initial value

# ...

# Entry and Label for Number of Planes
num_planes_label = ttk.Label(main_frame, text="Number of Planes:")
num_planes_label.grid(column=0, row=9, sticky=tk.W)
num_planes_scale = ttk.Scale(main_frame, from_=1, to=10, orient="horizontal")
num_planes_scale.grid(column=1, row=9, sticky=(tk.W, tk.E))
num_planes_scale.set(5)  # Set an initial value

# Button to update parameters
update_parameters_button = ttk.Button(main_frame, text="Apply", command=update_parameters)
update_parameters_button.grid(column=0, row=10, columnspan=2, pady=10)

# Create a frame for the intensity graph
intensity_frame = ttk.Frame(root)
intensity_frame.grid(column=1, row=0, rowspan=2, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
intensity_frame.columnconfigure(0, weight=1)
intensity_frame.rowconfigure(0, weight=1)

# Create a figure for the intensity graph
intensity_figure = plt.Figure(figsize=(5, 4), dpi=100)
intensity_plot = intensity_figure.add_subplot(111)
intensity_plot.set_xlabel("Intensity")
intensity_plot.set_ylabel("Value")

# Embed the intensity graph in the tkinter window
intensity_canvas = FigureCanvasTkAgg(intensity_figure, master=intensity_frame)
intensity_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Initialize the intensity graph (placeholder)
update_intensity_graph(None)  # Pass None or any other appropriate value to the function

# Customize the appearance of buttons and sliders
style = ttk.Style()
style.configure("TButton", relief="raised", padding=10, font=("Helvetica", 12))
style.configure("TScale", troughcolor="light gray", sliderthickness=20)

# Run the GUI application
root.mainloop()
