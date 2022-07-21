# Imports
import tkinter
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from functions import display_logo, display_textbox, display_icon, extract_images, display_images, resize_image

# Global Variable(s)
page_contents = []
all_images = []


# Copy Text
def copy_text(content):
    root.clipboard_clear()
    root.clipboard_append(content[-1])


# Save All Images
def save_all(images):
    counter = 1
    for i in images:
        i.save("saved_images/img" + str(counter) + ".png", format="png")
        counter += 1


# Root of App
root = tk.Tk()
root.geometry('+%d+%d' % (600, 300))
root.title("PDF Extractor Tool")

# Header: Logo & Browse Button
header = tk.Frame(root, width=800, height=220, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

# Main Content: Text & Image Extraction
main_content = tk.Frame(root, width=800, height=250, bg="#30cfe5")
main_content.grid(columnspan=3, rowspan=2, row=4)


# Open File Button
def open_file():
    # Update Button Text
    browse_text.set("Loading...")

    # Open Filebrowser.
    file = askopenfile(parent=root, mode='rb', title="Chose a File...",
                       filetypes=[('Pdf file', '*.pdf')])  # Read-only mode.

    # File Selected
    if file:
        # Read Page from PDF
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        page_content = page_content.replace('\u2122', "'")
        page_contents.append(page_content)

        # Text Box
        display_textbox(page_content, 4, 0, root)

        # Get Images
        images = extract_images(page)

        for i in images:
            all_images.append(i)

        image = images[0]
        display_images(image)

    browse_text.set("Browse...")

    # Image Navigation
    image_navigation_menu = tk.Frame(root, width=800, height=60, bg="grey")
    image_navigation_menu.grid(columnspan=3, rowspan=1, row=2)

    #
    display_icon("resources/left_arrow.png", 2, 0, "E")
    display_icon("resources/right_arrow.png", 2, 2, "W")

    # Image Count
    what_image = tk.Label(root, text="image X of Y", font=("AndaleMono", 10))
    what_image.grid(row=2, column=1)

    # Save Menu: Copy Text, Cycle Images, Save Image(s)
    save_menu = tk.Frame(root, width=800, height=60, bg="grey")
    save_menu.grid(columnspan=3, rowspan=1, row=3)

    # Save Buttons
    copy_text_btn = tk.Button(root, text="Copy Text", command=lambda: copy_text(page_contents), font=("AndaleMono", 10),
                              height=1, width=15)
    copy_text_btn.grid(row=3, column=0)

    save_all_btn = tk.Button(root, text="Save All Images", command=lambda: save_all(all_images),
                             font=("AndaleMono", 10),
                             height=1, width=15)
    save_all_btn.grid(row=3, column=1)

    save_btn = tk.Button(root, text="Save Image", font=("AndaleMono", 10), height=1, width=15)
    save_btn.grid(row=3, column=2)


# Insert Logo
display_logo("resources/logo.png", 0, 0)

# Instructions
instructions = tk.Label(root, text="Select a PDF File", font=("AndaleMono", 10), bg="white")
instructions.grid(row=0, column=2, sticky="SE", padx=75, pady=5)

# Browse Button
browse_text = tk.StringVar()
browse_text.set("Browse")
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font=("AndaleMono", 12),
                       bg="#30cfe5",
                       fg="black", height=1, width=15)
browse_btn.grid(row=1, column=2, sticky="NE", padx=50)

root.mainloop()
