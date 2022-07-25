import tkinter as tk
from PIL import Image, ImageTk
from os import mkdir, path, getcwd
import io


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

                if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                    mode = "RGB"
                else:
                    mode = "CMYK"
                    print("mode 2 " + str(xObject[obj]['/ColorSpace']))
                img = Image.frombytes(mode, size, data)
                img = img.convert('RGB')
                images.append(img)

    else:
        img = Image.open(fp="resources/image_not_found.png", mode='r', formats=None)
        img = img.convert('RGB')
        # print('else')
        # img = Image.new("RGB", (100, 100), (255, 255, 255))
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
