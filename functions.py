import tkinter as tk
from PIL import Image, ImageTk


# Display Logo
def display_logo(filepath, row, column):
    # Get image file.
    image = Image.open(filepath)

    # Resize Image
    image = image.resize((int(image.size[0] / 1.5), int(image.size[1] / 1.5)))

    # Convert to Tkinter Image
    image = ImageTk.PhotoImage(image)

    # Convert to Label Widget
    image_label = tk.Label(image=image, bg="white")
    image_label.image = image
    image_label.grid(column=column, row=row, rowspan=2, padx=20, pady=40)


# Display Logo
def display_icon(filepath, row, column, sticky):
    # Get image file.
    icon = Image.open(filepath)

    # Resize Image
    icon = icon.resize((20, 20))

    # Convert to Tkinter Image
    icon = ImageTk.PhotoImage(icon)

    # Convert to Label Widget
    icon_label = tk.Button(image=icon, width=25, height=25)
    icon_label.image = icon
    icon_label.grid(column=column, row=row, sticky=sticky)


# Display Textbox
def display_textbox(content, row, column, root):
    text_box = tk.Text(root, height=10, width=10, padx=10, pady=10)
    text_box.insert(1.0, content)
    text_box.tag_config("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=column, row=row, sticky="SW", padx=25, pady=25)
