import tkinter as tk
import zlib

from PIL import Image, ImageTk
from os import mkdir, path, getcwd
from PyPDF2 import generic


# From Stack Overflow https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python
def extract_images(page):
    images = []  # Array for images.

    if '/XObject' in page['/Resources']:
        xObject = page['/Resources']['/XObject'].getObject()

        # Fetch all images from the PDF.
        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':

                color_space = xObject[obj]['/ColorSpace']

                if color_space == '/DeviceRGB':
                    mode = "RGB"
                elif color_space == '/DeviceCMYK':
                    mode = "CMYK"
                elif color_space == '/DeviceGray':
                    mode = "P"

                if isinstance(color_space, generic.ArrayObject) and color_space[0] == '/ICCBased':
                    color_map = xObject[obj]['/ColorSpace'][1].getObject()['/N']
                    if color_map == 1:
                        mode = "P"
                    elif color_map == 3:
                        mode = "RGB"
                    elif color_map == 4:
                        mode = "CMYK"

                sub_obj = xObject[obj]

                zlib_compressed = '/FlateDecode' in sub_obj.get('/Filter', '')
                if zlib_compressed:
                    sub_obj._data = zlib.decompress(sub_obj._data)

                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])

                data = sub_obj._data #.getData()

                img = Image.frombytes(mode, size, data)
                img = img.convert('RGB')
                images.append(img)

    else:
        img = Image.open(fp="resources/image_not_found.png", mode='r', formats=None)
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


def check_directory(dir_name):
    save_dir = path.join(getcwd(), dir_name)
    if not path.isdir(save_dir):
        mkdir(save_dir)


def save_image(image, idx):
    check_directory('saved_images')
    image.save("saved_images/img" + str(idx) + ".png", format="png")


# Save All Images
def save_all(images):
    check_directory('saved_images')
    counter = 1

    for i in images:
        i.save("saved_images/img" + str(counter) + ".png", format="png")
        counter += 1
