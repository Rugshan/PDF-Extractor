# Imports
import tkinter
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title("PDF Extractor Tool")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(rowspan=3, columnspan=3)

# Logo
logo = Image.open('resources/logo.png')  # Pillow Image
logo = ImageTk.PhotoImage(logo)  # Tkinter Image
logo_label = tk.Label(image=logo)  # Label Widget
logo_label.image = logo  #
logo_label.grid(row=0, column=1)

# Instructions
instructions = tk.Label(root, text="Choose a PDF file and extract its text...", font="AndaleMono")
instructions.grid(columnspan=3, column=0, row=1)



def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Chose a File...", filetypes=[('Pdf file', '*.pdf')])  # Read-only mode.
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # Text Box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_config("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

    browse_text.set("Browse...")


# Browse Button
browse_text = tk.StringVar()
browse_text.set("Browse")
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="AndaleMono", bg="#30cfe5", fg="black", height=2, width=15)
browse_btn.grid(row=2, column=1)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
