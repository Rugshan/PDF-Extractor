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
def display_icon(filepath, row, column, sticky, command):
    # Get image file.
    icon = Image.open(filepath)

    # Resize Image
    icon = icon.resize((20, 20))

    # Convert to Tkinter Image
    icon = ImageTk.PhotoImage(icon)

    # Convert to Label Widget
    icon_label = tk.Button(image=icon, width=25, height=25, command=command)
    icon_label.image = icon
    icon_label.grid(column=column, row=row, sticky=sticky)


# Display Textbox
def display_textbox(content, row, column, root):
    text_box = tk.Text(root, height=8, width=30, padx=10, pady=10)
    text_box.insert(1.0, content)
    text_box.tag_config("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=column, row=row, sticky="SW", padx=25, pady=25)


# From Stack Overflow https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python
def extract_images(page):
    images = []  # Array for images.
    if '/XObject' in page['/Resources']:
        xObject = page['/Resources']['/XObject'].getObject()

        # Fetch all images from the PDF.
        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].getData()
                mode = ""

                if xObject[obj]['/ColorSpace'] == 'DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "CMYK"

                img = Image.frombytes(mode, size, data)
                img = img.convert('RGB')
                images.append(img)
    return images


# Resize Image
def resize_image(img):
    width, height = int(img.size[0]), int(img.size[1])

    if width > height:
        height = int(300 / width * height)
        width = 300
    elif height > width:
        width = int(250 / height * width)
        height = 250
    else:
        width, height = 250, 250

    img = img.resize((width, height))

    return img


# Display Images
def display_images(img):
    # Resize Image
    img = resize_image(img)

    # Convert to Tkinter Image
    img = ImageTk.PhotoImage(img)

    # Convert to Label Widget
    image_label = tk.Label(image=img, bg="white")
    image_label.image = img
    image_label.grid(row=4, column=2, rowspan=2)
    return image_label
