from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# Function to create PNG from text
def text_to_png(text, filename):
    # Set the image size (width, height)
    width, height = 500, 100

    # Create a new image with white background
    img = Image.new('RGB', (width, height), color=(255, 255, 255))

    # Set the font and size (you may need to adjust the font path based on your system)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Set text color
    text_color = (0, 0, 0)  # Black

    # Get the bounding box for the text
    text_bbox = draw.textbbox((0, 0), text, font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Position to center the text
    position = ((width - text_width) // 2, (height - text_height) // 2)

    # Add text to image
    draw.text(position, text, font=font, fill=text_color)

    # Save the image as PNG
    img.save(filename)

# Function to trigger the process
def generate_image():
    text = entry.get()
    if text:
        # Open file dialog to save the PNG file
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            text_to_png(text, filename)
            result_label.config(text=f"Image saved as {filename}")
        else:
            result_label.config(text="Save operation was cancelled.")
    else:
        result_label.config(text="Please enter some text.")

# Set up the GUI
root = Tk()
root.title("Text to PNG Converter")

# Create and pack the widgets
label = Label(root, text="Enter text:")
label.pack(pady=10)

entry = Entry(root, width=40)
entry.pack(pady=5)

generate_button = Button(root, text="Generate PNG", command=generate_image)
generate_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=5)

# Run the application
root.mainloop()
